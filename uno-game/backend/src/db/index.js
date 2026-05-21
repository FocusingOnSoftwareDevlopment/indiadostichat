const { Pool } = require('pg');
require('dotenv').config();

// Pool configuration
const config = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5432'),
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'yourpassword',
  database: process.env.DB_NAME || 'dostichat_uno',
};

let pool;
let isMock = false;

// In-memory mock database fallback for development/testing without PG instance
const mockDb = {
  leaderboard: new Map(), // username -> { username, wins, games_played, score }
  game_history: [],
  bans: new Map(), // ban_value -> { ban_type, ban_value, reason }
};

try {
  pool = new Pool(config);
  
  // Test connection
  pool.query('SELECT NOW()', (err, res) => {
    if (err) {
      console.warn('⚠️  PostgreSQL connection failed. Falling back to IN-MEMORY Mock Database Mode.', err.message);
      isMock = true;
    } else {
      console.log('✅ PostgreSQL connected successfully at', config.host);
    }
  });
} catch (e) {
  console.warn('⚠️  Could not initialize pg pool. Falling back to IN-MEMORY Mock Database Mode.', e.message);
  isMock = true;
}

// Wrapper query function supporting fallback
async function query(text, params) {
  if (isMock) {
    return handleMockQuery(text, params);
  }
  try {
    return await pool.query(text, params);
  } catch (err) {
    console.error('Database query error:', err.message, '\nText:', text);
    throw err;
  }
}

// Helper to simulate DB queries for in-memory mode
async function handleMockQuery(text, params) {
  // Normalize query whitespace to make matching easy
  const sql = text.replace(/\s+/g, ' ').trim().toLowerCase();
  
  // 1. Check if user is banned
  if (sql.includes('select 1 from bans') || sql.includes('select * from bans')) {
    const val = params[0];
    const ban = mockDb.bans.get(val);
    return { rows: ban ? [ban] : [] };
  }
  
  // 2. Fetch Leaderboard query
  if (sql.includes('from leaderboard')) {
    let rows = Array.from(mockDb.leaderboard.values());
    
    // Sort
    rows.sort((a, b) => b.score - a.score);
    
    // Check if there is a daily/weekly/monthly filter (mocking it by returning same stats)
    return { rows };
  }

  // 3. Upsert Leaderboard stats
  if (sql.includes('insert into leaderboard') || sql.includes('update leaderboard')) {
    const username = params[0];
    const winsDelta = params[1] || 0;
    const gamesDelta = params[2] || 0;
    const scoreDelta = params[3] || 0;

    let player = mockDb.leaderboard.get(username);
    if (!player) {
      player = { username, wins: 0, games_played: 0, score: 0 };
    }
    player.wins += winsDelta;
    player.games_played += gamesDelta;
    player.score += scoreDelta;
    mockDb.leaderboard.set(username, player);
    return { rows: [player] };
  }

  // 4. Save Game History
  if (sql.includes('insert into game_history')) {
    // params: [room_id, winner, score_awarded, players (JSON), duration]
    const historyItem = {
      id: mockDb.game_history.length + 1,
      room_id: params[0],
      winner: params[1],
      score_awarded: params[2],
      players: JSON.parse(params[3]),
      duration_seconds: params[4],
      created_at: new Date()
    };
    mockDb.game_history.push(historyItem);
    return { rows: [historyItem] };
  }

  // 5. Add Ban
  if (sql.includes('insert into bans')) {
    const type = params[0];
    const value = params[1];
    const reason = params[2] || '';
    const ban = { ban_type: type, ban_value: value, reason };
    mockDb.bans.set(value, ban);
    return { rows: [ban] };
  }

  // 6. Remove Ban
  if (sql.includes('delete from bans')) {
    const value = params[0];
    const deleted = mockDb.bans.delete(value);
    return { rowCount: deleted ? 1 : 0 };
  }

  // 7. Get ban list
  if (sql.includes('select * from bans')) {
    return { rows: Array.from(mockDb.bans.values()) };
  }

  // Default response
  return { rows: [], rowCount: 0 };
}

module.exports = {
  query,
  isMockMode: () => isMock,
  getMockDb: () => mockDb,
};
