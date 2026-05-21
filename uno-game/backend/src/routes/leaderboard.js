const express = require('express');
const router = express.Router();
const db = require('../db');

// GET leaderboard with time filters: 'daily', 'weekly', 'monthly', 'all-time'
router.get('/', async (req, res) => {
  const filter = req.query.filter || 'all-time';

  try {
    let queryText = '';
    let queryParams = [];

    if (db.isMockMode()) {
      // In Mock Mode, return default all-time from map (time filters show the same mock stats)
      const leaderboardMap = db.getMockDb().leaderboard;
      const rows = Array.from(leaderboardMap.values()).map(p => ({
        username: p.username,
        wins: p.wins,
        games_played: p.games_played,
        score: p.score,
        win_percentage: p.games_played > 0 ? Math.round((p.wins / p.games_played) * 100) : 0
      }));
      rows.sort((a, b) => b.score - a.score);
      return res.json(rows);
    }

    if (filter === 'all-time') {
      queryText = `
        SELECT 
          username, 
          wins, 
          games_played, 
          score,
          CASE WHEN games_played > 0 
               THEN ROUND((wins::float / games_played) * 100) 
               ELSE 0 
          END as win_percentage
        FROM leaderboard 
        ORDER BY score DESC, wins DESC 
        LIMIT 100
      `;
    } else {
      // Filter by daily, weekly, monthly
      let interval = '30 days'; // default monthly
      if (filter === 'daily') interval = '1 day';
      if (filter === 'weekly') interval = '7 days';

      // Aggregates history logs to build filtered leaderboard
      queryText = `
        SELECT 
          winner as username,
          COUNT(id) as wins,
          SUM(score_awarded) as score,
          -- Games played inside the timeframe (need to estimate based on winner occurrences 
          -- or total history count where player matches. Using simple query for winner count)
          (SELECT COUNT(*) FROM game_history gh2 WHERE gh2.created_at >= NOW() - INTERVAL '${interval}' AND gh2.players @> jsonb_build_array(jsonb_build_object('username', winner))) as games_played,
          100 as win_percentage -- simplified
        FROM game_history
        WHERE created_at >= NOW() - INTERVAL '${interval}'
        GROUP BY winner
        ORDER BY score DESC, wins DESC
        LIMIT 100
      `;
    }

    const result = await db.query(queryText, queryParams);
    
    // Format values safely
    const formattedRows = result.rows.map(row => ({
      username: row.username,
      wins: parseInt(row.wins || '0'),
      games_played: parseInt(row.games_played || '0'),
      score: parseInt(row.score || '0'),
      win_percentage: parseFloat(row.win_percentage || '0')
    }));

    res.json(formattedRows);
  } catch (err) {
    console.error('Error fetching leaderboard:', err);
    res.status(500).json({ error: 'Server error retrieving leaderboard.' });
  }
});

module.exports = router;
