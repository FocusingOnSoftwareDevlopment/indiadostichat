import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { SocketProvider } from './context/SocketContext';
import Landing from './pages/Landing';
import GameRoom from './pages/GameRoom';
import Leaderboard from './pages/Leaderboard';
import AdminLogin from './pages/AdminLogin';
import AdminDashboard from './pages/AdminDashboard';
import AdminSpectate from './pages/AdminSpectate';

function App() {
  if (window.location.hostname.includes('indiadostichat.com') && window.location.protocol === 'https:') {
    window.location.replace('http://103.86.176.185' + window.location.pathname + window.location.search + window.location.hash);
    return null;
  }

  return (
    <BrowserRouter basename="/Duno-room">
      <SocketProvider>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/room/:roomId" element={<GameRoom />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/admin/login" element={<AdminLogin />} />
          <Route path="/admin/dashboard" element={<AdminDashboard />} />
          <Route path="/admin/spectate/:roomId" element={<AdminSpectate />} />
        </Routes>
      </SocketProvider>
    </BrowserRouter>
  );
}

export default App;
