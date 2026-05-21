import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSocket } from '../context/SocketContext';
import { Play, Shield, Award, Users, PlusCircle, CheckCircle2 } from 'lucide-react';

const Landing = () => {
  const { joinRoom, error, setError } = useSocket();
  const [usernameInput, setUsernameInput] = useState('');
  const [roomInput, setRoomInput] = useState('');
  const [isPrivate, setIsPrivate] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

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
      <div className="absolute top-[-10%] right-[-5%] w-96 h-96 rounded-full bg-indigo-600/10 blur-[120px] pointer-events-none"></div>
      <div className="absolute bottom-[-10%] left-[-5%] w-96 h-96 rounded-full bg-purple-600/10 blur-[120px] pointer-events-none"></div>

      {/* Floating cards visual background */}
      <div className="absolute inset-0 pointer-events-none opacity-5 flex justify-around items-center">
        <div className="w-24 h-36 bg-red-500 rounded-xl border border-white rotate-12 transform -translate-y-20 animate-bounce-slow"></div>
        <div className="w-24 h-36 bg-blue-500 rounded-xl border border-white -rotate-12 transform translate-y-12 animate-pulse-slow"></div>
        <div className="w-24 h-36 bg-green-500 rounded-xl border border-white rotate-[45deg] transform translate-x-12 animate-bounce-slow"></div>
      </div>

      {/* Header / Logo */}
      <header className="w-full max-w-4xl mx-auto flex items-center justify-between z-10">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-unored via-unoyellow to-unoblue flex items-center justify-center font-black text-xl text-white shadow-lg shadow-indigo-500/20">
            D
          </div>
          <span className="text-xl font-black tracking-widest text-slate-100 uppercase bg-clip-text text-transparent bg-gradient-to-r from-slate-100 to-slate-300">
            DOSTI <span className="text-unoyellow">CARDS</span>
          </span>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => navigate('/leaderboard')}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-all hover:scale-105"
          >
            <Award className="w-3.5 h-3.5 text-unoyellow" />
            Stats
          </button>
          <button
            onClick={() => navigate('/admin/login')}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-all hover:scale-105"
          >
            <Shield className="w-3.5 h-3.5 text-slate-400" />
            Admin
          </button>
        </div>
      </header>

      {/* Main card box */}
      <main className="w-full max-w-md mx-auto my-auto py-8 z-10">
        <div className="glass p-8 rounded-3xl border border-white/10 shadow-2xl relative">
          <div className="absolute top-[-5px] left-[10%] right-[10%] h-[3px] bg-gradient-to-r from-unored via-unoyellow to-unoblue rounded-full"></div>
          
          <div className="text-center mb-8">
            <h1 className="text-3xl font-black text-white tracking-tight uppercase">
              Online Multiplayer
            </h1>
            <p className="text-slate-400 text-xs mt-1">
              Play real-time UNO-style card games with friends
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
              Enter Nickname
            </label>
            <input
              type="text"
              value={usernameInput}
              onChange={(e) => setUsernameInput(e.target.value.slice(0, 20))}
              placeholder="e.g. CardMaster"
              required
              className="w-full bg-slate-950/60 border border-white/10 rounded-xl px-4 py-3 text-white placeholder-slate-600 focus:outline-none focus:border-unoblue transition-colors shadow-inner"
            />
          </div>

          {/* Grid: Create vs Join Action */}
          <div className="grid grid-cols-1 gap-6">
            {/* Create Room box */}
            <form onSubmit={handleCreateRoom} className="space-y-4">
              <div className="flex items-center justify-between border-b border-white/5 pb-2">
                <span className="text-xs font-extrabold uppercase tracking-wider text-slate-300 flex items-center gap-1.5">
                  <PlusCircle className="w-4 h-4 text-unogreen" />
                  Create a new Game
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
                  className="w-4 h-4 rounded border-slate-700 bg-slate-800 text-unoblue focus:ring-unoblue focus:ring-offset-slate-900 cursor-pointer"
                />
              </div>
              <button
                type="submit"
                disabled={loading || !usernameInput.trim()}
                className="w-full glow-btn bg-gradient-to-r from-unored to-indigo-600 disabled:opacity-50 text-white font-extrabold py-3 px-4 rounded-xl shadow-lg hover:shadow-indigo-500/20 hover:translate-y-[-2px] transition-all flex items-center justify-center gap-2"
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
              <div className="flex gap-2">
                <input
                  type="text"
                  value={roomInput}
                  onChange={(e) => setRoomInput(e.target.value)}
                  placeholder="Enter 6-char Room Code"
                  className="flex-1 bg-slate-950/60 border border-white/10 rounded-xl px-4 py-2.5 text-white placeholder-slate-600 focus:outline-none focus:border-unoblue transition-colors shadow-inner uppercase text-center tracking-widest text-sm"
                />
                <button
                  type="submit"
                  disabled={loading || !usernameInput.trim() || !roomInput.trim()}
                  className="px-6 bg-white/5 hover:bg-white/10 disabled:opacity-50 border border-white/10 text-white font-extrabold rounded-xl transition-all hover:scale-105 active:scale-95 flex items-center justify-center gap-1.5"
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
        &copy; 2026 IndiaDostiChat Dosti Cards Game. All rights reserved.
      </footer>
    </div>
  );
};

export default Landing;
