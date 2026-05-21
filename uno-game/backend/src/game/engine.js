// Real-Time Game Engine & State Management
const { createDeck, isPlayable, calculateHandScore } = require('./cards');
const db = require('../db');

function formatDragonCard(card) {
  if (!card) return 'unknown card';
  const clanNames = {
    red: 'Fire Clan',
    blue: 'Ice Clan',
    green: 'Forest Clan',
    yellow: 'Thunder Clan',
    wild: 'Elder Dragon'
  };
  const valNames = {
    skip: 'Dragon Freeze',
    reverse: 'Dragon Turn',
    draw2: 'Dragon Bite +2',
    wild: 'Elder Dragon',
    wild4: 'Chaos Dragon +4'
  };
  
  if (card.color === 'wild') {
    return valNames[card.value] || 'Elder Dragon';
  }
  
  const clan = clanNames[card.color] || card.color;
  const val = valNames[card.value] || card.value;
  return `${clan} ${val}`;
}

// In-memory room manager
const rooms = new Map();

class Room {
  constructor(id, isPrivate = false) {
    this.id = id;
    this.status = 'waiting'; // 'waiting', 'playing', 'ended'
    this.players = [];       // Array of Player objects
    this.spectators = new Set(); // Set of admin socket IDs
    this.isPrivate = isPrivate;
    this.deck = [];
    this.discardPile = [];
    this.currentColor = null;
    this.currentTurn = 0;
    this.direction = 1;      // 1: Normal, -1: Reversed
    this.startedAt = null;
    
    this.turnTimer = null;
    this.secondsRemaining = 30;
    this.unoPressed = false;
    this.penaltyActive = false; // Player has 1 card left but forgot to press UNO
    this.wildAwaitingColor = false; // Waiting for wild color choice
    
    this.logs = [];
    this.reconnectGracePeriod = 60000; // 60 seconds to reconnect
    this.chatMessages = [];
  }

  addLog(message) {
    const log = {
      timestamp: new Date().toLocaleTimeString(),
      message
    };
    this.logs.push(log);
    return log;
  }

  getPlayersData(maskCards = true) {
    return this.players.map(p => ({
      username: p.username,
      cardsCount: p.cards.length,
      cards: maskCards ? [] : p.cards,
      isReady: p.isReady,
      isHost: p.isHost,
      active: p.active
    }));
  }

  getGameState(clientUsername) {
    const activePlayer = this.players[this.currentTurn];
    const isClientTurn = activePlayer && activePlayer.username === clientUsername;
    
    // Mask cards of other players
    const playersList = this.players.map(p => {
      const isSelf = p.username === clientUsername;
      return {
        username: p.username,
        cardsCount: p.cards.length,
        cards: isSelf ? p.cards : [], // Only show client's own cards
        isReady: p.isReady,
        isHost: p.isHost,
        active: p.active
      };
    });

    return {
      roomId: this.id,
      status: this.status,
      players: playersList,
      currentColor: this.currentColor,
      topCard: this.discardPile[this.discardPile.length - 1] || null,
      currentTurn: this.currentTurn,
      activePlayerName: activePlayer ? activePlayer.username : null,
      direction: this.direction,
      secondsRemaining: this.secondsRemaining,
      unoPressed: this.unoPressed,
      penaltyActive: this.penaltyActive,
      wildAwaitingColor: this.wildAwaitingColor,
      logs: this.logs.slice(-10), // Send last 10 logs
      isPrivate: this.isPrivate,
      chatMessages: this.chatMessages.slice(-20)
    };
  }

  // Add a player to the waiting room
  addPlayer(socketId, username, ipAddress) {
    // Check if player is already in room (reconnection)
    const existingPlayer = this.players.find(p => p.username === username);
    
    if (existingPlayer) {
      existingPlayer.socketId = socketId;
      existingPlayer.active = true;
      if (existingPlayer.disconnectTimer) {
        clearTimeout(existingPlayer.disconnectTimer);
        existingPlayer.disconnectTimer = null;
      }
      this.addLog(`${username} re-entered the dragon arena.`);
      return true;
    }

    if (this.players.length >= 8) {
      throw new Error('Room is full (max 8 players).');
    }

    if (this.status !== 'waiting') {
      throw new Error('Game has already started in this room.');
    }

    const isHost = this.players.length === 0;
    this.players.push({
      socketId,
      username,
      ipAddress,
      cards: [],
      isReady: isHost, // Host is ready by default
      isHost,
      active: true,
      disconnectTimer: null
    });

    this.addLog(`${username} joined the dragon arena.`);
    return true;
  }

  // Remove player or start reconnect grace period
  removePlayer(socketId, callbackOnEmpty) {
    const playerIndex = this.players.findIndex(p => p.socketId === socketId);
    if (playerIndex === -1) return null;

    const player = this.players[playerIndex];

    if (this.status === 'waiting') {
      // Remove immediately in waiting lobby
      this.players.splice(playerIndex, 1);
      this.addLog(`${player.username} left the dragon arena.`);
      
      // Pass host authority to next player if host left
      if (player.isHost && this.players.length > 0) {
        this.players[0].isHost = true;
        this.players[0].isReady = true;
        this.addLog(`${this.players[0].username} is now the host.`);
      }

      if (this.players.length === 0) {
        callbackOnEmpty(this.id);
      }
      return player.username;
    } else {
      // Mark inactive in active game and wait for reconnect
      player.active = false;
      this.addLog(`${player.username} disconnected. Waiting 60s to reconnect...`);

      player.disconnectTimer = setTimeout(() => {
        // Grace period expired, remove permanently
        const activeIdx = this.players.findIndex(p => p.username === player.username);
        if (activeIdx !== -1) {
          const removedPlayer = this.players[activeIdx];
          
          // Return cards to draw deck bottom to clean hand
          this.deck.push(...removedPlayer.cards);
          this.players.splice(activeIdx, 1);
          this.addLog(`${removedPlayer.username} left the dragon arena (timeout).`);

          if (this.players.length < 2) {
            this.forceEndGame('Not enough active players remaining.');
          } else {
            // Adjust turn tracker
            if (this.currentTurn >= this.players.length) {
              this.currentTurn = 0;
            }
            this.resetTurnTimer();
          }

          if (this.players.length === 0) {
            callbackOnEmpty(this.id);
          }
        }
      }, this.reconnectGracePeriod);

      return player.username;
    }
  }

  // Start the UNO game
  startGame() {
    if (this.players.length < 2) {
      throw new Error('Need at least 2 players to start.');
    }
    
    this.status = 'playing';
    this.startedAt = Date.now();
    this.deck = createDeck();
    this.discardPile = [];
    this.direction = 1;
    this.currentTurn = 0;
    this.unoPressed = false;
    this.penaltyActive = false;
    this.wildAwaitingColor = false;

    // Deal 7 cards to each player
    for (const player of this.players) {
      player.cards = this.deck.splice(0, 7);
    }

    // Draw first card onto discard pile (must not be wild Draw Four)
    let firstCard = this.deck.shift();
    while (firstCard.value === 'wild4') {
      this.deck.push(firstCard);
      firstCard = this.deck.shift();
    }
    this.discardPile.push(firstCard);
    
    // Set initial matching color
    this.currentColor = firstCard.color === 'wild' ? 'red' : firstCard.color;
    
    this.addLog('Dragon battle started! Cards dealt.');
    this.addLog(`First card is [${formatDragonCard(firstCard)}].`);

    // Apply immediate action effects if first card is special
    this.applyCardEffects(firstCard, true);

    this.startTimer();
  }

  // Handle playing a card
  playCard(username, cardId, chosenColor) {
    if (this.status !== 'playing') throw new Error('Game is not active.');
    if (this.wildAwaitingColor) throw new Error('Awaiting color selection.');

    const activePlayer = this.players[this.currentTurn];
    if (activePlayer.username !== username) throw new Error("It's not your turn!");

    const cardIdx = activePlayer.cards.findIndex(c => c.id === cardId);
    if (cardIdx === -1) throw new Error('Card not found in your hand.');

    const card = activePlayer.cards[cardIdx];
    const topCard = this.discardPile[this.discardPile.length - 1];

    if (!isPlayable(card, topCard, this.currentColor)) {
      throw new Error('Card is not playable.');
    }

    // Play card
    activePlayer.cards.splice(cardIdx, 1);
    this.discardPile.push(card);
    
    // Set current active color
    if (card.color !== 'wild') {
      this.currentColor = card.color;
    } else {
      this.wildAwaitingColor = true;
    }

    let playedMsg = '';
    if (card.value === 'wild') {
      playedMsg = `${username} summoned Elder Dragon.`;
    } else if (card.value === 'wild4') {
      playedMsg = `${username} summoned Chaos Dragon +4.`;
    } else if (card.value === 'skip') {
      playedMsg = `${username} used Dragon Freeze.`;
    } else if (card.value === 'reverse') {
      playedMsg = `${username} used Dragon Turn.`;
    } else if (card.value === 'draw2') {
      playedMsg = `${username} used Dragon Bite +2.`;
    } else {
      playedMsg = `${username} played ${formatDragonCard(card)}.`;
    }
    this.addLog(playedMsg);

    // Check if player is down to 1 card and check UNO rules
    if (activePlayer.cards.length === 1) {
      if (!this.unoPressed) {
        this.penaltyActive = true;
        this.addLog(`⚠️  ${username} forgot to ROAR and received penalty cards.`);
      }
    } else {
      this.unoPressed = false; // Reset UNO trigger for next rounds
    }

    // Check Win Condition
    if (activePlayer.cards.length === 0) {
      this.endGame(username);
      return;
    }

    // Resolve Card Actions
    if (!this.wildAwaitingColor) {
      this.applyCardEffects(card, false);
      this.nextTurn();
    } else {
      // If wild card, active player must choose color before turn shifts
      if (chosenColor) {
        this.resolveColorSelection(chosenColor);
      }
    }
  }

  // Handle color selection for wild cards
  resolveColorSelection(chosenColor) {
    const validColors = ['red', 'yellow', 'green', 'blue'];
    if (!validColors.includes(chosenColor)) throw new Error('Invalid color chosen.');

    const clanNames = {
      red: 'Fire Clan',
      blue: 'Ice Clan',
      green: 'Forest Clan',
      yellow: 'Thunder Clan'
    };
    this.currentColor = chosenColor;
    this.wildAwaitingColor = false;
    this.addLog(`Clan changed to ${clanNames[chosenColor] || chosenColor}.`);

    // Retrieve the wild card played
    const topCard = this.discardPile[this.discardPile.length - 1];
    
    // Apply wild draw 4 consequences
    if (topCard.value === 'wild4') {
      const nextPlayerIdx = this.getNextPlayerIndex();
      const nextPlayer = this.players[nextPlayerIdx];
      const drawn = this.drawCardsFromDeck(4);
      nextPlayer.cards.push(...drawn);
      this.addLog(`${nextPlayer.username} draws 4 cards and is skipped!`);
      // Skip the next player
      this.currentTurn = nextPlayerIdx;
    }

    this.nextTurn();
  }

  // Apply Action card penalties and switches
  applyCardEffects(card, isFirstPlay = false) {
    const nextPlayerIdx = this.getNextPlayerIndex();
    const nextPlayer = this.players[nextPlayerIdx];

    switch (card.value) {
      case 'skip':
        this.addLog(`${nextPlayer.username} was frozen and skipped.`);
        // Increment turn index past next player
        this.currentTurn = nextPlayerIdx;
        break;
      case 'reverse':
        this.direction *= -1;
        this.addLog(`Play direction turned.`);
        // If 2 players, reverse acts like Skip
        if (this.players.length === 2 && !isFirstPlay) {
          this.currentTurn = nextPlayerIdx;
          this.addLog(`${nextPlayer.username} was frozen and skipped.`);
        }
        break;
      case 'draw2':
        const drawn = this.drawCardsFromDeck(2);
        nextPlayer.cards.push(...drawn);
        this.addLog(`${nextPlayer.username} draws 2 cards and is skipped!`);
        // Skip the penalized player
        this.currentTurn = nextPlayerIdx;
        break;
    }
  }

  // Handle drawing a card
  drawCard(username) {
    if (this.status !== 'playing') throw new Error('Game not active.');
    if (this.wildAwaitingColor) throw new Error('Choose wild card color first.');

    const activePlayer = this.players[this.currentTurn];
    if (activePlayer.username !== username) throw new Error("It's not your turn!");

    // If player has a penalty for forgetting UNO, force draw 2 cards and clear penalty
    if (this.penaltyActive) {
      const penaltyCards = this.drawCardsFromDeck(2);
      activePlayer.cards.push(...penaltyCards);
      this.penaltyActive = false;
      this.unoPressed = false;
      this.addLog(`${username} forgot to ROAR and received penalty cards.`);
      this.nextTurn();
      return;
    }

    // Draw single card
    const card = this.drawCardsFromDeck(1)[0];
    activePlayer.cards.push(card);
    this.addLog(`${username} drew a card.`);

    // If the card is playable, let them play it immediately, otherwise skip turn
    const topCard = this.discardPile[this.discardPile.length - 1];
    if (isPlayable(card, topCard, this.currentColor)) {
      // Return details letting client know they can choose to play it or keep it
      return card;
    } else {
      // Auto-skip to next player
      this.addLog(`${username} passed.`);
      this.nextTurn();
      return null;
    }
  }

  // Declare UNO
  pressUno(username) {
    if (this.status !== 'playing') throw new Error('Game not active.');
    
    // Find player index who clicked UNO
    const player = this.players.find(p => p.username === username);
    if (!player) return;

    const isOwnTurn = this.players[this.currentTurn].username === username;

    if (player.cards.length === 2 && isOwnTurn) {
      // Declaring UNO preemptively before playing the 2nd to last card
      this.unoPressed = true;
      this.addLog(`${username} shouted ROAR.`);
    } else if (player.cards.length === 1) {
      // Declaring UNO right after turn play
      this.unoPressed = true;
      this.penaltyActive = false;
      this.addLog(`${username} shouted ROAR.`);
    } else {
      throw new Error("You can only ROAR when you have 1 or 2 cards.");
    }
  }

  // Fetch cards from deck pile, shuffling discard pile if deck empty
  drawCardsFromDeck(count) {
    const drawn = [];
    for (let i = 0; i < count; i++) {
      if (this.deck.length === 0) {
        // Save the top card, and shuffle discard pile back to deck
        const topCard = this.discardPile.pop();
        this.deck = createDeck(); // Easy recreate & reshuffle
        this.discardPile = [topCard];
        this.addLog('Deck empty. Reshuffled discard pile back to deck.');
      }
      if (this.deck.length > 0) {
        drawn.push(this.deck.shift());
      }
    }
    return drawn;
  }

  // Shift turns
  nextTurn() {
    this.currentTurn = this.getNextPlayerIndex();
    this.resetTurnTimer();
  }

  getNextPlayerIndex() {
    let nextIndex = this.currentTurn + this.direction;
    if (nextIndex >= this.players.length) nextIndex = 0;
    if (nextIndex < 0) nextIndex = this.players.length - 1;
    return nextIndex;
  }

  // Timer controls
  startTimer() {
    this.secondsRemaining = 30;
    clearInterval(this.turnTimer);
    this.turnTimer = setInterval(() => {
      this.secondsRemaining--;
      if (this.secondsRemaining <= 0) {
        this.handleTimeout();
      }
    }, 1000);
  }

  resetTurnTimer() {
    this.unoPressed = false;
    this.penaltyActive = false;
    this.startTimer();
  }

  // Auto-skip or auto-draw when player timer hits 0
  handleTimeout() {
    const activePlayer = this.players[this.currentTurn];
    if (!activePlayer) return;

    this.addLog(`${activePlayer.username} turn timed out.`);

    try {
      if (this.wildAwaitingColor) {
        // Pick red by default for them to unblock turns
        this.resolveColorSelection('red');
      } else {
        // Draw card for player
        const topCard = this.discardPile[this.discardPile.length - 1];
        const drawn = this.drawCardsFromDeck(1)[0];
        activePlayer.cards.push(drawn);
        
        // If playable, play it, else pass
        if (isPlayable(drawn, topCard, this.currentColor)) {
          activePlayer.cards.pop();
          this.discardPile.push(drawn);
          this.currentColor = drawn.color === 'wild' ? 'red' : drawn.color;
          this.addLog(`System played [${formatDragonCard(drawn)}] for ${activePlayer.username}.`);
          this.applyCardEffects(drawn, false);
        }
        
        this.nextTurn();
      }
    } catch (e) {
      console.error('Error handling player timeout:', e.message);
      this.nextTurn();
    }
  }

  // Complete game normally
  async endGame(winnerName) {
    clearInterval(this.turnTimer);
    this.status = 'ended';

    // Calculate score points (Score = sum of remaining cards of all other players)
    let roundScore = 0;
    const playerStatsList = [];

    for (const player of this.players) {
      const score = calculateHandScore(player.cards);
      playerStatsList.push({
        username: player.username,
        cardsCount: player.cards.length,
        score
      });
      if (player.username !== winnerName) {
        roundScore += score;
      }
    }

    // Default to at least 50 points if other players' hands score zero
    if (roundScore === 0) roundScore = 50;

    this.addLog(`🏆 ${winnerName} won the dragon battle.`);

    try {
      // Save stats to database (async, fails silently to in-memory fallback if pg offline)
      await db.query(
        `INSERT INTO game_history (room_id, winner, score_awarded, players, duration_seconds) 
         VALUES ($1, $2, $3, $4, $5)`,
        [
          this.id,
          winnerName,
          roundScore,
          JSON.stringify(playerStatsList),
          Math.floor((Date.now() - this.startedAt) / 1000)
        ]
      );

      // Update Winner Score
      await db.query(
        `INSERT INTO leaderboard (username, wins, games_played, score)
         VALUES ($1, 1, 1, $2)
         ON CONFLICT (username) DO UPDATE 
         SET wins = leaderboard.wins + 1,
             games_played = leaderboard.games_played + 1,
             score = leaderboard.score + $2,
             updated_at = CURRENT_TIMESTAMP`,
        [winnerName, roundScore]
      );

      // Update Losers Stats (only increments games_played)
      for (const player of this.players) {
        if (player.username !== winnerName) {
          await db.query(
            `INSERT INTO leaderboard (username, wins, games_played, score)
             VALUES ($1, 0, 1, 0)
             ON CONFLICT (username) DO UPDATE 
             SET games_played = leaderboard.games_played + 1,
                 updated_at = CURRENT_TIMESTAMP`,
            [player.username]
          );
        }
      }
    } catch (e) {
      console.error('Failed to save game statistics to database:', e.message);
    }
  }

  // Force close game from admin
  forceEndGame(reason = 'Game ended by administrator.') {
    clearInterval(this.turnTimer);
    this.status = 'ended';
    this.addLog(`❌ Game force ended. Reason: ${reason}`);
  }

  destroy() {
    clearInterval(this.turnTimer);
    this.players.forEach(p => {
      if (p.disconnectTimer) clearTimeout(p.disconnectTimer);
    });
  }
}

// Global API export utilities
function getOrCreateRoom(roomId, isPrivate = false) {
  let room = rooms.get(roomId);
  if (!room) {
    room = new Room(roomId, isPrivate);
    rooms.set(roomId, room);
  }
  return room;
}

function getRoom(roomId) {
  return rooms.get(roomId);
}

function deleteRoom(roomId) {
  const room = rooms.get(roomId);
  if (room) {
    room.destroy();
    rooms.delete(roomId);
  }
}

function listActiveRooms() {
  return Array.from(rooms.values()).map(r => ({
    roomId: r.id,
    status: r.status,
    players: r.players.map(p => ({ username: p.username, active: p.active, cardsCount: p.cards.length })),
    spectatorsCount: r.spectators.size,
    isPrivate: r.isPrivate,
    durationSeconds: r.startedAt ? Math.floor((Date.now() - r.startedAt) / 1000) : 0
  }));
}

module.exports = {
  getOrCreateRoom,
  getRoom,
  deleteRoom,
  listActiveRooms
};
