import React, { useState, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSocket } from '../context/SocketContext';
import { Play, Shield, Award, Users, PlusCircle } from 'lucide-react';

const Landing = () => {
  const { joinRoom, error, setError } = useSocket();
  const [usernameInput, setUsernameInput] = useState('');
  const [roomInput, setRoomInput] = useState('');
  const [isPrivate, setIsPrivate] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Memoized embers array to prevent re-generating positions on render
  const embers = useMemo(() => {
    return Array.from({ length: 15 }).map((_, i) => ({
      id: i,
      left: `${Math.random() * 100}%`,
      size: `${Math.random() * 6 + 4}px`,
      duration: `${Math.random() * 8 + 6}s`,
      delay: `${Math.random() * 8}s`,
      drift: `${Math.random() * 80 - 40}px`,
    }));
  }, []);

  const handleCreateRoom = async (e) => {
    e.preventDefault();
    if (!usernameInput.trim()) {
      setError('Please enter a username.');
      return;
    }
    // Generate a random room code (6 alphanumeric characters)
    const randomRoomId = Math.random().toString(36).substring(2, 8);
    setLoading(true);
    try {
      await joinRoom(usernameInput, randomRoomId, isPrivate);
      navigate(`/room/${randomRoomId}`);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleJoinRoom = async (e) => {
    e.preventDefault();
    if (!usernameInput.trim()) {
      setError('Please enter a username.');
      return;
    }
    if (!roomInput.trim()) {
      setError('Please enter a room code.');
      return;
    }
    const cleanRoomId = roomInput.trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    setLoading(true);
    try {
      await joinRoom(usernameInput, cleanRoomId);
      navigate(`/room/${cleanRoomId}`);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen animated-bg flex flex-col justify-between relative overflow-hidden px-4 py-8 sm:px-6">
      {/* Background Decor */}
      <div className="absolute top-[-10%] right-[-5%] w-96 h-96 rounded-full bg-red-900/10 blur-[120px] pointer-events-none"></div>
      <div className="absolute bottom-[-10%] left-[-5%] w-96 h-96 rounded-full bg-purple-900/10 blur-[120px] pointer-events-none"></div>

      {/* Floating Embers */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
        {embers.map((ember) => (
          <div
            key={ember.id}
            className="ember"
            style={{
              left: ember.left,
              '--ember-size': ember.size,
              '--ember-duration': ember.duration,
              '--ember-drift': ember.drift,
              animationDelay: ember.delay,
            }}
          />
        ))}
      </div>

      {/* Floating cards visual background */}
      <div className="absolute inset-0 pointer-events-none opacity-[0.06] flex justify-around items-center">
        <div className="w-24 h-36 bg-gradient-to-br from-red-800 to-red-950 rounded-xl border border-red-500/30 rotate-12 transform -translate-y-20 animate-bounce-slow flex items-center justify-center shadow-lg">
          <span className="text-red-300/40 font-black text-base uppercase tracking-widest">Fire</span>
        </div>
        <div className="w-24 h-36 bg-gradient-to-br from-sky-800 to-indigo-950 rounded-xl border border-cyan-500/30 -rotate-12 transform translate-y-12 animate-pulse-slow flex items-center justify-center shadow-lg">
          <span className="text-sky-300/40 font-black text-base uppercase tracking-widest">Ice</span>
        </div>
        <div className="w-24 h-36 bg-gradient-to-br from-emerald-800 to-emerald-950 rounded-xl border border-emerald-500/30 rotate-[45deg] transform translate-x-12 animate-bounce-slow flex items-center justify-center shadow-lg">
          <span className="text-emerald-300/40 font-black text-base uppercase tracking-widest">Forest</span>
        </div>
      </div>

      {/* Header / Logo */}
      <header className="w-full max-w-4xl mx-auto flex items-center justify-between z-10">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-red-700 via-amber-500 to-yellow-500 flex items-center justify-center font-black text-xl text-slate-900 shadow-lg shadow-amber-500/20">
            D
          </div>
          <div className="flex flex-col">
            <span className="text-xl font-black tracking-widest text-slate-100 uppercase">
              DUNO <span className="text-amber-400 font-medium text-xs tracking-normal normal-case block sm:inline sm:ml-2 sm:text-sm">dragon clash card game</span>
            </span>
            <span className="text-[9px] text-slate-500 tracking-wider font-bold uppercase mt-[-2px]">
              IndiaDostiChat Arena
            </span>
          </div>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => navigate('/leaderboard')}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-all hover:scale-105 cursor-pointer"
          >
            <Award className="w-3.5 h-3.5 text-yellow-400" />
            Arena Stats
          </button>
          <button
            onClick={() => navigate('/admin/login')}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-all hover:scale-105 cursor-pointer"
          >
            <Shield className="w-3.5 h-3.5 text-slate-400" />
            Admin
          </button>
        </div>
      </header>

      {/* Main card box */}
      <main className="w-full max-w-md mx-auto my-auto py-8 z-10">
        <div className="glass p-8 rounded-3xl border border-white/10 shadow-2xl relative">
          <div className="absolute top-[-5px] left-[10%] right-[10%] h-[3px] bg-gradient-to-r from-red-650 via-amber-550 to-yellow-500 rounded-full"></div>
          
          <div className="text-center mb-8">
            <h1 className="text-2xl sm:text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-amber-400 to-yellow-500 tracking-wide uppercase leading-tight">
              DUNO dragon clash card game
            </h1>
            <p className="text-slate-400 text-xs mt-1">
              Enter the multiplayer dark fantasy dragon card arena
            </p>
          </div>

          {/* Errors */}
          {error && (
            <div className="mb-6 p-3 rounded-xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs text-center font-bold">
              {error}
            </div>
          )}

          {/* Username registration field */}
          <div className="mb-8">
            <label className="block text-[10px] font-extrabold uppercase tracking-widest text-slate-400 mb-2">
              Dragon Nickname
            </label>
            <input
              type="text"
              value={usernameInput}
              onChange={(e) => setUsernameInput(e.target.value.slice(0, 20))}
              placeholder="e.g. FireBreather"
              required
              className="w-full bg-slate-950/60 border border-white/10 rounded-xl px-4 py-3 text-white placeholder-slate-650 focus:outline-none focus:border-amber-500 transition-colors shadow-inner"
            />
          </div>

          {/* Grid: Create vs Join Action */}
          <div className="grid grid-cols-1 gap-6">
            {/* Create Room box */}
            <form onSubmit={handleCreateRoom} className="space-y-4">
              <div className="flex items-center justify-between border-b border-white/5 pb-2">
                <span className="text-xs font-extrabold uppercase tracking-wider text-slate-300 flex items-center gap-1.5">
                  <PlusCircle className="w-4 h-4 text-emerald-400" />
                  Convene Dragon Arena
                </span>
              </div>
              <div className="flex items-center justify-between px-1">
                <label htmlFor="private-checkbox" className="text-xs text-slate-400 cursor-pointer select-none">
                  Make Room Private (Only invite code)
                </label>
                <input
                  id="private-checkbox"
                  type="checkbox"
                  checked={isPrivate}
                  onChange={(e) => setIsPrivate(e.target.checked)}
                  className="w-4 h-4 rounded border-slate-700 bg-slate-800 text-amber-500 focus:ring-amber-500 focus:ring-offset-slate-900 cursor-pointer"
                />
              </div>
              <button
                type="submit"
                disabled={loading || !usernameInput.trim()}
                className="w-full glow-btn bg-gradient-to-r from-red-700 via-amber-600 to-indigo-850 disabled:opacity-50 text-white font-extrabold py-3 px-4 rounded-xl shadow-lg hover:shadow-amber-500/20 hover:translate-y-[-2px] transition-all flex items-center justify-center gap-2 cursor-pointer"
              >
                <Play className="w-4 h-4 fill-white" />
                CREATE ROOM
              </button>
            </form>

            <div className="relative flex py-2 items-center">
              <div className="flex-grow border-t border-white/5"></div>
              <span className="flex-shrink mx-4 text-[9px] font-black text-slate-500 uppercase tracking-widest">
                Or join existing
              </span>
              <div className="flex-grow border-t border-white/5"></div>
            </div>

            {/* Join Room Box */}
            <form onSubmit={handleJoinRoom} className="space-y-4">
              <div className="flex flex-col sm:flex-row gap-3">
                <input
                  type="text"
                  value={roomInput}
                  onChange={(e) => setRoomInput(e.target.value)}
                  placeholder="Enter Room Code"
                  className="w-full sm:flex-1 bg-slate-950/60 border border-white/10 rounded-xl px-4 py-2.5 text-white placeholder-slate-650 focus:outline-none focus:border-amber-500 transition-colors shadow-inner uppercase text-center tracking-widest text-sm"
                />
                <button
                  type="submit"
                  disabled={loading || !usernameInput.trim() || !roomInput.trim()}
                  className="w-full sm:w-auto px-6 py-2.5 bg-white/5 hover:bg-white/10 disabled:opacity-50 border border-white/10 text-white font-extrabold rounded-xl transition-all hover:scale-105 active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer"
                >
                  <Users className="w-4 h-4" />
                  JOIN
                </button>
              </div>
            </form>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="w-full max-w-4xl mx-auto text-center text-slate-600 text-[10px] uppercase tracking-widest z-10 border-t border-white/5 pt-4">
        &copy; 2026 IndiaDostiChat DUNO dragon clash card game. All rights reserved.
      </footer>
    </div>
  );
};

export default Landing;
