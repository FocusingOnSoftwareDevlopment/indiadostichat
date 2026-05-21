import React, { createContext, useContext, useState, useEffect } from 'react';
import { io } from 'socket.io-client';
import soundManager from '../utils/SoundManager';

const SocketContext = createContext(null);

export const useSocket = () => {
  const context = useContext(SocketContext);
  if (!context) {
    throw new Error('useSocket must be used within a SocketProvider');
  }
  return context;
};

export const SocketProvider = ({ children }) => {
  const [socket, setSocket] = useState(null);
  const [connected, setConnected] = useState(false);
  const [username, setUsername] = useState(() => sessionStorage.getItem('dosti_username') || '');
  const [roomId, setRoomId] = useState(() => sessionStorage.getItem('dosti_room_id') || '');
  const [gameState, setGameState] = useState(null);
  const [lobbyPlayers, setLobbyPlayers] = useState([]);
  const [error, setError] = useState('');
  const [chatMessages, setChatMessages] = useState([]);

  const socketUrl = import.meta.env.VITE_API_URL || 
    (window.location.hostname === 'localhost' ? 'http://localhost:5000' : 
     (window.location.hostname.includes('indiadostichat.com') ? 'http://103.86.176.185' : window.location.origin));

  useEffect(() => {
    const newSocket = io(socketUrl, {
      path: '/Duno-room/socket.io',
      transports: ['websocket', 'polling'],
      autoConnect: true,
      reconnection: true,
      reconnectionAttempts: 10,
      reconnectionDelay: 2000,
    });

    newSocket.on('connect', () => {
      console.log('🔌 Connected to game server:', newSocket.id);
      setConnected(true);
      setError('');
      
      // Auto-reconnect if username and roomId were cached
      const savedUser = sessionStorage.getItem('dosti_username');
      const savedRoom = sessionStorage.getItem('dosti_room_id');
      if (savedUser && savedRoom) {
        newSocket.emit('join_lobby', { username: savedUser, roomId: savedRoom }, (res) => {
          if (res.error) {
            console.warn('Auto-reconnect failed:', res.error);
            sessionStorage.removeItem('dosti_username');
            sessionStorage.removeItem('dosti_room_id');
            setUsername('');
            setRoomId('');
          } else {
            console.log('🔄 Reconnected successfully to room:', savedRoom);
          }
        });
      }
    });

    newSocket.on('disconnect', (reason) => {
      console.log('🔌 Disconnected from server:', reason);
      setConnected(false);
    });

    newSocket.on('connect_error', (err) => {
      console.error('Connection error:', err.message);
      setError('Cannot connect to server. Trying to reconnect...');
    });

    // Handle lobby update event
    newSocket.on('lobby_updated', ({ players }) => {
      setLobbyPlayers(players);
      setGameState(null); // Clear active game board while in lobby
    });

    // Handle game started event
    newSocket.on('game_started', () => {
      soundManager.play('deal');
    });

    // Handle game state updates (for active play)
    newSocket.on('game_state_updated', (state) => {
      setGameState((prev) => {
        // Trigger sound events on phase transitions
        if (state.status === 'playing') {
          // Check if top card changed
          if (prev?.topCard?.id !== state.topCard?.id) {
            if (state.topCard?.color === 'wild') {
              soundManager.play('wild');
            } else {
              soundManager.play('play');
            }
          }
          // Check if cards drawn
          const selfPrev = prev?.players.find(p => p.username === username);
          const selfCurrent = state.players.find(p => p.username === username);
          if (selfCurrent && selfPrev && selfCurrent.cardsCount > selfPrev.cardsCount) {
            soundManager.play('draw');
          }
          // Turn alert sound
          if (state.activePlayerName === username && prev?.activePlayerName !== username) {
            // Vibrotactile feedback if supported
            if (navigator.vibrate) navigator.vibrate(100);
          }
          // Low time alert (warn every tick when <= 5 seconds remain on player's own turn)
          if (state.activePlayerName === username && state.secondsRemaining <= 5 && state.secondsRemaining > 0) {
            soundManager.play('warning');
          }
        }
        return state;
      });
      if (state.chatMessages) {
        setChatMessages(state.chatMessages);
      }
    });

    // Handle chat message received
    newSocket.on('chat_received', (msg) => {
      setChatMessages((prev) => [...prev, msg].slice(-30));
    });

    // Handle game completion
    newSocket.on('game_ended', ({ winner }) => {
      if (winner === username) {
        soundManager.play('win');
      }
    });

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [socketUrl, username]);

  // Join Room / Lobby
  const joinRoom = (name, room, isPrivate = false) => {
    return new Promise((resolve, reject) => {
      if (!socket || !connected) {
        return reject(new Error('Socket is not connected.'));
      }

      socket.emit('join_lobby', { username: name, roomId: room, isPrivate }, (response) => {
        if (response.error) {
          setError(response.error);
          reject(new Error(response.error));
        } else {
          setUsername(response.username);
          setRoomId(response.roomId);
          sessionStorage.setItem('dosti_username', response.username);
          sessionStorage.setItem('dosti_room_id', response.roomId);
          setError('');
          resolve(response);
        }
      });
    });
  };

  // Toggle Ready
  const toggleReady = () => {
    if (socket) socket.emit('toggle_ready');
  };

  // Start Game
  const startGame = () => {
    return new Promise((resolve, reject) => {
      if (!socket) return reject(new Error('Socket offline.'));
      socket.emit('start_game', (res) => {
        if (res && res.error) {
          reject(new Error(res.error));
        } else {
          resolve();
        }
      });
    });
  };

  // Play Card
  const playCard = (cardId, chosenColor = null) => {
    return new Promise((resolve, reject) => {
      if (!socket) return reject(new Error('Socket offline.'));
      socket.emit('play_card', { cardId, chosenColor }, (res) => {
        if (res.error) {
          soundManager.play('error');
          reject(new Error(res.error));
        } else {
          resolve();
        }
      });
    });
  };

  // Draw Card
  const drawCard = () => {
    return new Promise((resolve, reject) => {
      if (!socket) return reject(new Error('Socket offline.'));
      socket.emit('draw_card', (res) => {
        if (res.error) {
          soundManager.play('error');
          reject(new Error(res.error));
        } else {
          resolve(res.playableCard); // Returns Card if playable
        }
      });
    });
  };

  // Play drawn card decision
  const playDrawnCard = (playCardBool, chosenColor = null) => {
    return new Promise((resolve, reject) => {
      if (!socket) return reject(new Error('Socket offline.'));
      socket.emit('play_drawn_card', { playCard: playCardBool, chosenColor }, (res) => {
        if (res.error) {
          soundManager.play('error');
          reject(new Error(res.error));
        } else {
          resolve();
        }
      });
    });
  };

  // Declare UNO
  const callUno = () => {
    return new Promise((resolve, reject) => {
      if (!socket) return reject(new Error('Socket offline.'));
      socket.emit('call_uno', (res) => {
        if (res.error) {
          soundManager.play('error');
          reject(new Error(res.error));
        } else {
          resolve();
        }
      });
    });
  };

  // Send Chat
  const sendChat = (text) => {
    if (socket && text.trim()) {
      socket.emit('send_chat', text.trim());
    }
  };

  // Leave Game
  const leaveGame = () => {
    if (socket) {
      socket.emit('leave_game');
      sessionStorage.removeItem('dosti_username');
      sessionStorage.removeItem('dosti_room_id');
      setUsername('');
      setRoomId('');
      setGameState(null);
      setLobbyPlayers([]);
    }
  };

  return (
    <SocketContext.Provider
      value={{
        socket,
        connected,
        username,
        roomId,
        gameState,
        lobbyPlayers,
        error,
        setError,
        chatMessages,
        joinRoom,
        toggleReady,
        startGame,
        playCard,
        drawCard,
        playDrawnCard,
        callUno,
        sendChat,
        leaveGame,
      }}
    >
      {children}
    </SocketContext.Provider>
  );
};
