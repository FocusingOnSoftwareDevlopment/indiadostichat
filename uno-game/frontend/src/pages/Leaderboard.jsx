import React, { useState, useEffect, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { Award, ArrowLeft, Loader2, Trophy, Medal } from 'lucide-react';
import soundManager from '../utils/SoundManager';

const Leaderboard = () => {
  const navigate = useNavigate();
  const [filter, setFilter] = useState('all-time');
  const [stats, setStats] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

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

  // Resolve API URL dynamically
  const apiUrl = import.meta.env.VITE_API_URL || 
    (window.location.hostname === 'localhost' ? 'http://localhost:5000/Duno-room' : 
     (window.location.hostname.includes('indiadostichat.com') ? 'http://103.86.176.185/Duno-room' : window.location.origin + '/Duno-room'));

  useEffect(() => {
    const fetchLeaderboard = async () => {
      setLoading(true);
      setError('');
      try {
        const response = await fetch(`${apiUrl}/api/leaderboard?filter=${filter}`);
        if (!response.ok) {
          throw new Error('Failed to retrieve leaderboard data.');
        }
        const data = await response.json();
        setStats(data);
      } catch (err) {
        setError(err.message || 'Server connection failed.');
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, [filter, apiUrl]);

  const handleBack = () => {
    soundManager.play('click');
    navigate('/');
  };

  const tabs = [
    { id: 'daily', name: 'Daily' },
    { id: 'weekly', name: 'Weekly' },
    { id: 'monthly', name: 'Monthly' },
    { id: 'all-time', name: 'All-Time' },
  ];

  const getRankBadge = (rank) => {
    if (rank === 1) return <Trophy className="w-5 h-5 text-amber-400 fill-amber-400/10 inline" />;
    if (rank === 2) return <Medal className="w-5 h-5 text-slate-300 fill-slate-300/10 inline" />;
    if (rank === 3) return <Medal className="w-5 h-5 text-amber-600 fill-amber-600/10 inline" />;
    return <span className="text-slate-500 font-extrabold text-sm px-1.5">{rank}</span>;
  };

  const getDragonTitle = (score) => {
    if (score >= 1000) return { name: 'Dragon Master', class: 'bg-purple-950/40 text-purple-300 border-purple-500/30' };
    if (score >= 500) return { name: 'Gold Clan', class: 'bg-amber-950/40 text-amber-300 border-amber-500/30' };
    if (score >= 200) return { name: 'Silver Clan', class: 'bg-slate-800/60 text-slate-300 border-slate-600/30' };
    return { name: 'Fledgling', class: 'bg-stone-900/60 text-stone-400 border-stone-700/30' };
  };

  return (
    <div className="min-h-screen animated-bg flex flex-col justify-between p-4 sm:p-6 relative overflow-hidden">
      {/* Background Decor */}
      <div className="absolute top-[-10%] left-[-5%] w-96 h-96 rounded-full bg-purple-600/10 blur-[120px] pointer-events-none"></div>

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

      {/* Header bar */}
      <header className="w-full max-w-4xl mx-auto flex items-center justify-between z-10 border-b border-white/5 pb-4">
        <button
          onClick={handleBack}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-all hover:scale-105 cursor-pointer"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          Back
        </button>
        <div className="flex items-center gap-2">
          <Award className="w-5 h-5 text-amber-400" />
          <span className="text-sm font-black tracking-widest text-slate-100 uppercase">DUNO <span className="text-amber-400">Arena</span></span>
        </div>
      </header>

      {/* Main Stats list */}
      <main className="w-full max-w-3xl mx-auto my-auto py-6 z-10 flex-1 flex flex-col justify-center">
        <div className="glass p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl space-y-6">
          <div className="text-center">
            <h1 className="text-3xl font-black text-white tracking-tight uppercase">Dragon Arena Hall of Fame</h1>
            <p className="text-slate-400 text-xs mt-1">Epic victories achieved by dragon warriors globally</p>
          </div>

          {/* Navigation Filter Tabs */}
          <div className="flex justify-center border-b border-white/5 pb-1 gap-1">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => {
                  soundManager.play('click');
                  setFilter(tab.id);
                }}
                className={`px-4 py-2.5 rounded-xl text-xs font-extrabold uppercase tracking-wider transition-all cursor-pointer ${
                  filter === tab.id
                    ? 'bg-amber-600 text-white shadow shadow-amber-500/15'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-white/5'
                }`}
              >
                {tab.name}
              </button>
            ))}
          </div>

          {/* Loading details */}
          {loading ? (
            <div className="h-64 flex flex-col items-center justify-center gap-3 text-slate-400">
              <Loader2 className="w-8 h-8 animate-spin text-amber-550" />
              <span className="text-xs font-bold uppercase tracking-wider">Loading rankings...</span>
            </div>
          ) : error ? (
            <div className="p-4 rounded-2xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs font-bold text-center">
              {error}
            </div>
          ) : stats.length === 0 ? (
            <div className="h-64 flex flex-col items-center justify-center text-slate-500 text-center">
              <Award className="w-12 h-12 opacity-20 mb-2" />
              <p className="text-sm">No dragon clash results recorded. Enter the arena to claim your glory!</p>
            </div>
          ) : (
            /* Stats Table list */
            <div className="overflow-x-auto scrollbar-none rounded-2xl border border-white/5 bg-slate-950/20 shadow-inner">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="border-b border-white/5 bg-white/5 text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">
                    <th className="py-3 px-4">Rank</th>
                    <th className="py-3 px-4">Warrior Name</th>
                    <th className="py-3 px-4 text-center">Wins</th>
                    <th className="py-3 px-4 text-center">Played</th>
                    <th className="py-3 px-4 text-center">Winrate</th>
                    <th className="py-3 px-4 text-right">Glory Points</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-white/5">
                  {stats.map((p, idx) => (
                    <tr
                      key={idx}
                      className="hover:bg-white/5 transition-colors text-sm text-slate-300 font-bold"
                    >
                      <td className="py-3 px-4 whitespace-nowrap">{getRankBadge(idx + 1)}</td>
                      <td className="py-3 px-4 whitespace-nowrap text-white font-extrabold">
                        <div className="flex flex-col sm:flex-row sm:items-center gap-1.5">
                          <span>{p.username}</span>
                          {(() => {
                            const title = getDragonTitle(p.score);
                            return (
                              <span className={`px-1.5 py-0.5 rounded text-[8px] font-black border uppercase tracking-wider ${title.class}`}>
                                {title.name}
                              </span>
                            );
                          })()}
                        </div>
                      </td>
                      <td className="py-3 px-4 text-center">{p.wins}</td>
                      <td className="py-3 px-4 text-center">{p.games_played}</td>
                      <td className="py-3 px-4 text-center text-xs">
                        {p.win_percentage}%
                      </td>
                      <td className="py-3 px-4 text-right text-amber-400 font-black text-base">
                        {p.score}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </main>

      {/* Footer bar */}
      <footer className="w-full text-center text-slate-600 text-[10px] uppercase tracking-widest z-10 pt-4">
        DUNO dragon clash card game Leaderboard &bull; Updated real-time
      </footer>
    </div>
  );
};

export default Leaderboard;
