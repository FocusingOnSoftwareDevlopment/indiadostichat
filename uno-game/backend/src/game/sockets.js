// Socket.IO Multiplayer Game Event Handlers
const { getOrCreateRoom, getRoom, deleteRoom, listActiveRooms } = require('./engine');
const db = require('../db');
const jwt = require('jsonwebtoken');

const JWT_SECRET = process.env.JWT_SECRET || 'supersecretchangeinproduction';
const ADMIN_USERNAME = process.env.ADMIN_USERNAME || 'Heisenberg';

function handleSocketConnections(io) {
  io.on('connection', (socket) => {
    // Retrieve connection IP address (checking headers for proxy configurations)
    const ipAddress = socket.handshake.headers['x-forwarded-for'] || socket.handshake.address;
    
    // Save state context on connection
    socket.username = null;
    socket.roomId = null;
    socket.isAdminSpectator = false;

    console.log(`🔌 New client socket connection: ${socket.id} (IP: ${ipAddress})`);

    // 1. Join Lobby (Creates room or registers player in waiting room)
    socket.on('join_lobby', async ({ username, roomId, isPrivate }, callback) => {
      // Input sanitation
      if (!username || !roomId) {
        return callback({ error: 'Username and Room ID are required.' });
      }

      const cleanUsername = username.trim().substring(0, 20);
      const cleanRoomId = roomId.trim().toLowerCase().replace(/[^a-z0-9]/g, '');

      if (!cleanUsername || !cleanRoomId) {
        return callback({ error: 'Invalid room credentials.' });
      }

      try {
        // Security checks: Validate IP & Username Bans
        const ipBanResult = await db.query('SELECT 1 FROM bans WHERE ban_type = \'ip\' AND ban_value = $1', [ipAddress]);
        if (ipBanResult.rows.length > 0) {
          return callback({ error: 'Your IP address has been banned by the administrator.' });
        }

        const userBanResult = await db.query('SELECT 1 FROM bans WHERE ban_type = \'username\' AND ban_value = $1', [cleanUsername]);
        if (userBanResult.rows.length > 0) {
          return callback({ error: 'This username is banned.' });
        }

        // Room allocation
        const room = getOrCreateRoom(cleanRoomId, isPrivate);

        // Check if player already exists in room with same name (reconnect checks)
        const playerInRoom = room.players.find(p => p.username === cleanUsername);
        
        // Prevent multi-boxing (same name active on a different socket)
        if (playerInRoom && playerInRoom.active && playerInRoom.socketId !== socket.id) {
          return callback({ error: 'Username is already active in this room.' });
        }

        // Register player to engine
        room.addPlayer(socket.id, cleanUsername, ipAddress);

        // Bind socket context
        socket.username = cleanUsername;
        socket.roomId = cleanRoomId;

        // Join socket channel
        socket.join(cleanRoomId);

        // Callback state success
        callback({ success: true, username: cleanUsername, roomId: cleanRoomId });

        // Broadcast updates to room
        if (room.status === 'playing') {
          // Reconnecting player immediately gets game state
          broadcastGameState(room);
        } else {
          // Normal lobby player list update
          io.to(cleanRoomId).emit('lobby_updated', {
            players: room.getPlayersData()
          });
        }
      } catch (err) {
        callback({ error: err.message });
      }
    });

    // 2. Toggle Ready Status
    socket.on('toggle_ready', () => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room || room.status !== 'waiting') return;

      const player = room.players.find(p => p.username === username);
      if (player) {
        // Toggle (host remains always ready)
        player.isReady = player.isHost ? true : !player.isReady;
        
        io.to(roomId).emit('lobby_updated', {
          players: room.getPlayersData()
        });
      }
    });

    // 3. Start Game
    socket.on('start_game', (callback) => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room) return;

      const player = room.players.find(p => p.username === username);
      if (!player || !player.isHost) {
        return callback({ error: 'Only the room host can start the game.' });
      }

      // Check if all players are ready
      const allReady = room.players.every(p => p.isReady);
      if (!allReady) {
        return callback({ error: 'All players must be ready to start.' });
      }

      try {
        room.startGame();
        io.to(roomId).emit('game_started');
        broadcastGameState(room);
      } catch (err) {
        callback({ error: err.message });
      }
    });

    // 4. Play Card Action
    socket.on('play_card', ({ cardId, chosenColor }, callback) => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room || room.status !== 'playing') return;

      try {
        room.playCard(username, cardId, chosenColor);
        callback({ success: true });

        if (room.status === 'ended') {
          // Game finished! Send final winner stats
          io.to(roomId).emit('game_ended', {
            winner: username,
            logs: room.logs
          });
          deleteRoom(roomId);
        } else {
          // Shift active turns and update states
          broadcastGameState(room);
        }
      } catch (err) {
        callback({ error: err.message });
      }
    });

    // 5. Draw Card Action
    socket.on('draw_card', (callback) => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room || room.status !== 'playing') return;

      try {
        const playableCard = room.drawCard(username);
        
        // Return drawn card to client. If playable, they choose to play/keep
        callback({ 
          success: true, 
          playableCard: playableCard || null 
        });

        broadcastGameState(room);
      } catch (err) {
        callback({ error: err.message });
      }
    });

    // 6. Play Drawn Card Decision
    socket.on('play_drawn_card', ({ playCard, chosenColor }, callback) => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room || room.status !== 'playing') return;

      const activePlayer = room.players[room.currentTurn];
      if (!activePlayer || activePlayer.username !== username) return;

      try {
        if (playCard) {
          // Play the last drawn card (which is the last card in player's hand)
          const lastCard = activePlayer.cards[activePlayer.cards.length - 1];
          room.playCard(username, lastCard.id, chosenColor);
        } else {
          // Keep it and pass turn
          room.addLog(`${username} chose to keep card. Turn passed.`);
          room.nextTurn();
        }

        callback({ success: true });

        if (room.status === 'ended') {
          io.to(roomId).emit('game_ended', {
            winner: username,
            logs: room.logs
          });
          deleteRoom(roomId);
        } else {
          broadcastGameState(room);
        }
      } catch (err) {
        callback({ error: err.message });
      }
    });

    // 7. Call UNO Warning
    socket.on('call_uno', (callback) => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room) return;

      try {
        room.pressUno(username);
        callback({ success: true });
        broadcastGameState(room);
      } catch (err) {
        callback({ error: err.message });
      }
    });

    // 8. Send Chat Message
    socket.on('send_chat', (text) => {
      const { roomId, username } = socket;
      if (!roomId || !username) return;

      const room = getRoom(roomId);
      if (!room) return;

      const chatMsg = {
        username,
        text: text.substring(0, 100), // Max 100 chars
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      
      room.chatMessages.push(chatMsg);
      if (room.chatMessages.length > 50) room.chatMessages.shift(); // Cap logs

      io.to(roomId).emit('chat_received', chatMsg);
    });

    // 9. Admin Join Room Spectating (Invisible)
    socket.on('admin_spectate_join', ({ token, roomId }, callback) => {
      if (!token || !roomId) return callback({ error: 'Missing token or roomId.' });

      try {
        const decoded = jwt.verify(token, JWT_SECRET);
        if (decoded.username !== ADMIN_USERNAME) {
          return callback({ error: 'Access denied.' });
        }

        const room = getRoom(roomId);
        if (!room) return callback({ error: 'Room not found.' });

        // Join room invisibly (add to spectators, do not add to players array)
        room.spectators.add(socket.id);
        socket.roomId = roomId;
        socket.isAdminSpectator = true;
        socket.join(roomId);

        callback({ success: true });

        // Send spectator the full reveal layout
        sendAdminSpectateState(room, socket.id);
      } catch (err) {
        callback({ error: 'Invalid admin credentials.' });
      }
    });

    // 10. Manual Leave Game
    socket.on('leave_game', () => {
      handleDisconnectOrLeave(socket);
    });

    // 11. Connection Drop
    socket.on('disconnect', () => {
      handleDisconnectOrLeave(socket);
    });
  });

  // Helper: Broadcast game state to each individual socket to mask hand selections
  function broadcastGameState(room) {
    room.players.forEach(p => {
      const playerSocket = io.sockets.sockets.get(p.socketId);
      if (playerSocket) {
        playerSocket.emit('game_state_updated', room.getGameState(p.username));
      }
    });

    // Send state to invisible admin spectators (full reveal)
    room.spectators.forEach(spectatorSocketId => {
      sendAdminSpectateState(room, spectatorSocketId);
    });
  }

  // Helper: Send admin spectator update
  function sendAdminSpectateState(room, spectatorSocketId) {
    const spectatorSocket = io.sockets.sockets.get(spectatorSocketId);
    if (spectatorSocket) {
      spectatorSocket.emit('admin_spectate_update', {
        roomId: room.id,
        status: room.status,
        players: room.players.map(p => ({
          username: p.username,
          cards: p.cards,
          cardsCount: p.cards.length,
          active: p.active
        })),
        currentColor: room.currentColor,
        topCard: room.discardPile[room.discardPile.length - 1] || null,
        currentTurn: room.currentTurn,
        direction: room.direction,
        secondsRemaining: room.secondsRemaining,
        logs: room.logs
      });
    }
  }

  // Handle player leaving or connection dropouts
  function handleDisconnectOrLeave(socket) {
    const { roomId, username, isAdminSpectator } = socket;
    if (!roomId) return;

    const room = getRoom(roomId);
    if (!room) return;

    if (isAdminSpectator) {
      // Remove admin spectator silently
      room.spectators.delete(socket.id);
      socket.leave(roomId);
      return;
    }

    // Process user disconnection
    const disconnectedUser = room.removePlayer(socket.id, (emptyRoomId) => {
      // Callback if room is completely empty (destroy it)
      deleteRoom(emptyRoomId);
      console.log(`🏠 Room ${emptyRoomId} deleted (all players left).`);
    });

    if (disconnectedUser) {
      socket.leave(roomId);
      socket.roomId = null;
      socket.username = null;

      if (room.status === 'playing') {
        broadcastGameState(room);
      } else {
        io.to(roomId).emit('lobby_updated', {
          players: room.getPlayersData()
        });
      }
    }
  }
}

module.exports = handleSocketConnections;
