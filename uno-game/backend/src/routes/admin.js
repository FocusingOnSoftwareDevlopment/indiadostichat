const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const db = require('../db');
const { getRoom, listActiveRooms, deleteRoom } = require('../game/engine');
const { authenticateAdmin } = require('../middleware/auth');

const JWT_SECRET = process.env.JWT_SECRET || 'supersecretchangeinproduction';
const ADMIN_USERNAME = process.env.ADMIN_USERNAME || 'Heisenberg';

// Admin Login Route (Requires username Heisenberg and matches configured hash)
router.post('/login', async (req, res) => {
  const { username, password } = req.body;
  
  if (!username || !password) {
    return res.status(400).json({ error: 'Please enter both username and password.' });
  }

  if (username !== ADMIN_USERNAME) {
    return res.status(401).json({ error: 'Invalid admin credentials.' });
  }

  // Get configured hash from .env (fallback hash is for password: 'heisenberg123')
  const defaultHash = '$2a$10$zuPdbN2NiyuvH/II8aclNeA9nn6KxTkJxoVGx5JkcWJeuQHuK4pjK';
  const adminHash = process.env.ADMIN_PASSWORD_HASH || defaultHash;

  try {
    const isMatch = await bcrypt.compare(password, adminHash);
    if (!isMatch) {
      return res.status(401).json({ error: 'Invalid admin credentials.' });
    }

    const token = jwt.sign({ username: ADMIN_USERNAME }, JWT_SECRET, { expiresIn: '12h' });
    res.json({ token, username: ADMIN_USERNAME });
  } catch (err) {
    console.error('Admin login error:', err);
    res.status(500).json({ error: 'Server error during authentication.' });
  }
});

// GET all active games (secured)
router.get('/active-rooms', authenticateAdmin, (req, res) => {
  const activeRooms = listActiveRooms();
  res.json(activeRooms);
});

// POST to spectate/retrieve full player card hands of a room (secured)
router.get('/spectate/:roomId', authenticateAdmin, (req, res) => {
  const room = getRoom(req.params.roomId);
  if (!room) {
    return res.status(404).json({ error: 'Room not found.' });
  }
  
  // Return state WITHOUT masking hands (admin spectate mode)
  res.json({
    roomId: room.id,
    status: room.status,
    players: room.players.map(p => ({
      username: p.username,
      cards: p.cards, // Full cards revealed!
      cardsCount: p.cards.length,
      active: p.active,
      ipAddress: p.ipAddress
    })),
    currentColor: room.currentColor,
    topCard: room.discardPile[room.discardPile.length - 1] || null,
    currentTurn: room.currentTurn,
    direction: room.direction,
    secondsRemaining: room.secondsRemaining,
    logs: room.logs
  });
});

// POST force end game (secured)
router.post('/force-end/:roomId', authenticateAdmin, (req, res) => {
  const room = getRoom(req.params.roomId);
  if (!room) {
    return res.status(404).json({ error: 'Room not found.' });
  }

  const { reason } = req.body;
  room.forceEndGame(reason || 'Terminated by administrator.');
  
  // Trigger delete room after cleanup
  deleteRoom(room.id);
  res.json({ message: 'Game terminated successfully.' });
});

// POST Kick player (secured)
router.post('/kick', authenticateAdmin, (req, res) => {
  const { roomId, username } = req.body;
  if (!roomId || !username) {
    return res.status(400).json({ error: 'Missing roomId or username.' });
  }

  const room = getRoom(roomId);
  if (!room) {
    return res.status(404).json({ error: 'Room not found.' });
  }

  const player = room.players.find(p => p.username === username);
  if (!player) {
    return res.status(404).json({ error: 'Player not found in this room.' });
  }

  // Force socket disconnect if open
  const io = req.app.get('io');
  if (io && player.socketId) {
    const socket = io.sockets.sockets.get(player.socketId);
    if (socket) {
      socket.emit('kicked', { reason: 'You have been kicked by an administrator.' });
      socket.leave(roomId);
      socket.disconnect();
    }
  }

  // Trigger permanent removal
  room.addLog(`${username} kicked by administrator.`);
  const idx = room.players.findIndex(p => p.username === username);
  if (idx !== -1) {
    room.deck.push(...room.players[idx].cards);
    room.players.splice(idx, 1);
  }

  if (room.players.length < 2 && room.status === 'playing') {
    room.forceEndGame('Not enough active players remaining.');
    deleteRoom(room.id);
  } else if (room.players.length === 0) {
    deleteRoom(room.id);
  } else {
    if (room.currentTurn >= room.players.length) {
      room.currentTurn = 0;
    }
    room.resetTurnTimer();
  }

  res.json({ message: `Kicked player ${username}.` });
});

// GET Completed Game History (secured)
router.get('/history', authenticateAdmin, async (req, res) => {
  try {
    const result = await db.query('SELECT * FROM game_history ORDER BY created_at DESC LIMIT 100');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: 'Database fetch error.' });
  }
});

// GET list of active bans (secured)
router.get('/bans', authenticateAdmin, async (req, res) => {
  try {
    const result = await db.query('SELECT * FROM bans ORDER BY created_at DESC');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: 'Database fetch error.' });
  }
});

// POST Ban user or IP (secured)
router.post('/ban', authenticateAdmin, async (req, res) => {
  const { banType, banValue, reason } = req.body;
  if (!banType || !banValue) {
    return res.status(400).json({ error: 'Missing banType (username/ip) or banValue.' });
  }

  try {
    await db.query(
      'INSERT INTO bans (ban_type, ban_value, reason) VALUES ($1, $2, $3) ON CONFLICT (ban_value) DO NOTHING',
      [banType, banValue, reason || 'Banned by Admin']
    );

    // If username ban, kick them from any active room they are currently playing in
    if (banType === 'username') {
      const activeRooms = listActiveRooms();
      for (const roomInfo of activeRooms) {
        const room = getRoom(roomInfo.roomId);
        const player = room.players.find(p => p.username === banValue);
        if (player) {
          const io = req.app.get('io');
          if (io && player.socketId) {
            const socket = io.sockets.sockets.get(player.socketId);
            if (socket) {
              socket.emit('banned', { reason: 'Your account has been banned.' });
              socket.leave(room.id);
              socket.disconnect();
            }
          }
          const idx = room.players.findIndex(p => p.username === banValue);
          room.players.splice(idx, 1);
          room.addLog(`${banValue} kicked (account banned by admin).`);
          if (room.players.length < 2 && room.status === 'playing') {
            room.forceEndGame('Not enough active players.');
            deleteRoom(room.id);
          }
        }
      }
    }

    res.json({ message: `Successfully banned ${banValue}.` });
  } catch (err) {
    res.status(500).json({ error: 'Database save error.' });
  }
});

// POST Unban (secured)
router.post('/unban', authenticateAdmin, async (req, res) => {
  const { banValue } = req.body;
  if (!banValue) {
    return res.status(400).json({ error: 'Missing banValue.' });
  }

  try {
    const result = await db.query('DELETE FROM bans WHERE ban_value = $1', [banValue]);
    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'Ban record not found.' });
    }
    res.json({ message: `Successfully unbanned ${banValue}.` });
  } catch (err) {
    res.status(500).json({ error: 'Database delete error.' });
  }
});

// POST Reset Leaderboard (secured)
router.post('/reset-leaderboard', authenticateAdmin, async (req, res) => {
  try {
    // If PG is Mock Mode, clear local Map
    if (db.isMockMode()) {
      db.getMockDb().leaderboard.clear();
    } else {
      await db.query('TRUNCATE TABLE leaderboard RESTART IDENTITY');
    }
    res.json({ message: 'Leaderboard reset completed successfully.' });
  } catch (err) {
    res.status(500).json({ error: 'Database truncate error.' });
  }
});

module.exports = router;
