const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const db = require('./db');
const adminRouter = require('./routes/admin');
const leaderboardRouter = require('./routes/leaderboard');
const handleSocketConnections = require('./game/sockets');

const app = express();
const server = http.createServer(app);

const PORT = process.env.PORT || 5000;
const CLIENT_URL = process.env.CLIENT_URL || 'http://localhost:5173';

// 1. Security & CORS configuration
const corsOptions = {
  origin: [CLIENT_URL, 'http://localhost:3000', 'https://www.indiadostichat.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
};

app.use(cors(corsOptions));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rate-limiting middleware (anti-spam / denial-of-service prevention)
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Too many requests. Please try again after 15 minutes.' }
});

// Apply rate limits to all auth and API endpoints
app.use('/api/', apiLimiter);

// Bind custom variables to express context
app.set('db', db);

// 2. HTTP Routing API endpoints
app.use('/api/admin', adminRouter);
app.use('/api/leaderboard', leaderboardRouter);

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({
    status: 'healthy',
    time: new Date(),
    dbMode: db.isMockMode() ? 'In-Memory (Mock)' : 'PostgreSQL (Active)'
  });
});

// Serve frontend build files in production (VPS setup)
const path = require('path');
const frontendBuildPath = path.join(__dirname, '..', '..', 'frontend', 'dist');
app.use(express.static(frontendBuildPath));

// Catch-all route to serve frontend index.html for SPA client-side routing
app.get('*', (req, res, next) => {
  if (req.path.startsWith('/api')) {
    return next();
  }
  res.sendFile(path.join(frontendBuildPath, 'index.html'), (err) => {
    if (err) {
      res.status(200).send('Dosti Cards API Server is Running. Frontend not yet compiled.');
    }
  });
});

// 3. Socket.IO Setup
const io = new Server(server, {
  cors: corsOptions,
  pingTimeout: 30000,
  pingInterval: 15000,
  transports: ['websocket', 'polling']
});

// Attach socket server globally to request object
app.set('io', io);

// Initialize real-time multiplayer controller handlers
handleSocketConnections(io);

// 4. Start Server
server.listen(PORT, () => {
  console.log(`=================================================`);
  console.log(`🚀 Dosti Cards Backend listening on port ${PORT}`);
  console.log(`🔌 WebSockets enabled and configured`);
  console.log(`📦 Database Mode: ${db.isMockMode() ? 'IN-MEMORY MOCK' : 'POSTGRESQL'}`);
  console.log(`=================================================`);
});
