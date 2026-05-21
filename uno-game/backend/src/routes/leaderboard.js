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
      if (filter === 'all-time') {
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
      } else {
        // Daily, weekly, monthly aggregation from mock history
        let cutoff = new Date();
        if (filter === 'daily') cutoff.setDate(cutoff.getDate() - 1);
        else if (filter === 'weekly') cutoff.setDate(cutoff.getDate() - 7);
        else cutoff.setDate(cutoff.getDate() - 30); // monthly

        const history = db.getMockDb().game_history.filter(g => new Date(g.created_at) >= cutoff);
        
        // Aggregate statistics per player
        const playerStats = {};
        for (const game of history) {
          // Initialize winner stats
          if (!playerStats[game.winner]) {
            playerStats[game.winner] = { username: game.winner, wins: 0, games_played: 0, score: 0 };
          }
          playerStats[game.winner].wins += 1;
          playerStats[game.winner].score += game.score_awarded;

          // Increment games_played count for all players in this game
          for (const p of game.players) {
            if (!playerStats[p.username]) {
              playerStats[p.username] = { username: p.username, wins: 0, games_played: 0, score: 0 };
            }
            playerStats[p.username].games_played += 1;
          }
        }

        const rows = Object.values(playerStats).map(p => ({
          username: p.username,
          wins: p.wins,
          games_played: p.games_played,
          score: p.score,
          win_percentage: p.games_played > 0 ? Math.round((p.wins / p.games_played) * 100) : 0
        }));
        rows.sort((a, b) => b.score - a.score);
        return res.json(rows);
      }
    }

    if (filter === 'all-time') {
      queryText = `
        SELECT 
          username, 
          wins, 
          games_played, 
          score
        FROM leaderboard 
        ORDER BY score DESC, wins DESC 
        LIMIT 100
      `;
    } else {
      // Filter by daily, weekly, monthly
      let interval = '30 days'; // default monthly
      if (filter === 'daily') interval = '1 day';
      if (filter === 'weekly') interval = '7 days';

      // Aggregates history logs to build filtered leaderboard using correct jsonb parsing
      queryText = `
        SELECT 
          winner as username,
          COUNT(id) as wins,
          SUM(score_awarded) as score,
          (
            SELECT COUNT(*) 
            FROM game_history gh2 
            WHERE gh2.created_at >= NOW() - INTERVAL '${interval}' 
              AND EXISTS (
                SELECT 1 FROM jsonb_to_recordset(gh2.players) as p(username text) 
                WHERE p.username = game_history.winner
              )
          ) as games_played
        FROM game_history
        WHERE created_at >= NOW() - INTERVAL '${interval}'
        GROUP BY winner
        ORDER BY score DESC, wins DESC
        LIMIT 100
      `;
    }

    const result = await db.query(queryText, queryParams);
    
    // Format values safely and calculate win percentage dynamically
    const formattedRows = result.rows.map(row => {
      const wins = parseInt(row.wins || '0');
      const games_played = parseInt(row.games_played || '0');
      return {
        username: row.username,
        wins,
        games_played,
        score: parseInt(row.score || '0'),
        win_percentage: games_played > 0 ? Math.round((wins / games_played) * 100) : 0
      };
    });

    res.json(formattedRows);
  } catch (err) {
    console.error('Error fetching leaderboard:', err);
    res.status(500).json({ error: 'Server error retrieving leaderboard.' });
  }
});

module.exports = router;
