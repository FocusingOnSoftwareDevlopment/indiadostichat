-- Database Schema for Dosti Cards (UNO-style multiplayer game)

-- 1. Leaderboard Stats (Aggregated player statistics)
CREATE TABLE IF NOT EXISTS leaderboard (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    wins INTEGER DEFAULT 0,
    games_played INTEGER DEFAULT 0,
    score INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for leaderboard query sorting (fast loading)
CREATE INDEX IF NOT EXISTS idx_leaderboard_score ON leaderboard(score DESC);
CREATE INDEX IF NOT EXISTS idx_leaderboard_wins ON leaderboard(wins DESC);

-- 2. Game History Logs
CREATE TABLE IF NOT EXISTS game_history (
    id SERIAL PRIMARY KEY,
    room_id VARCHAR(50) NOT NULL,
    winner VARCHAR(50) NOT NULL,
    score_awarded INTEGER NOT NULL,
    players JSONB NOT NULL, -- Array of player objects {username, cardsRemaining}
    duration_seconds INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for time filters
CREATE INDEX IF NOT EXISTS idx_game_history_created ON game_history(created_at DESC);

-- 3. Bans (By Username or IP Address to protect the site from abuse)
CREATE TABLE IF NOT EXISTS bans (
    id SERIAL PRIMARY KEY,
    ban_type VARCHAR(20) NOT NULL CHECK (ban_type IN ('username', 'ip')),
    ban_value VARCHAR(100) UNIQUE NOT NULL,
    reason TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index for quick verification during login/connections
CREATE INDEX IF NOT EXISTS idx_bans_value ON bans(ban_value);
