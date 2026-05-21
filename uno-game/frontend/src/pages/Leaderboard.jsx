import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Award, ArrowLeft, Loader2, Trophy, Medal } from 'lucide-react';
import soundManager from '../utils/SoundManager';

const Leaderboard = () => {
  const navigate = useNavigate();
  const [filter, setFilter] = useState('all-time');
  const [stats, setStats] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Resolve API URL dynamically
  const apiUrl = import.meta.env.VITE_API_URL || 
    (window.location.hostname === 'localhost' ? 'http://localhost:5000' : window.location.origin);

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
    if (rank === 1) return <Trophy className="w-5 h-5 text-unoyellow fill-unoyellow/10 inline" />;
    if (rank === 2) return <Medal className="w-5 h-5 text-slate-300 fill-slate-300/10 inline" />;
    if (rank === 3) return <Medal className="w-5 h-5 text-amber-600 fill-amber-600/10 inline" />;
    return <span className="text-slate-500 font-extrabold text-sm px-1.5">{rank}</span>;
  };

  return (
    <div className="min-h-screen animated-bg flex flex-col justify-between p-4 sm:p-6 relative overflow-hidden">
      {/* Background Decor */}
      <div className="absolute top-[-10%] left-[-5%] w-96 h-96 rounded-full bg-purple-600/10 blur-[120px] pointer-events-none"></div>

      {/* Header bar */}
      <header className="w-full max-w-4xl mx-auto flex items-center justify-between z-10 border-b border-white/5 pb-4">
        <button
          onClick={handleBack}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-all hover:scale-105"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          Back
        </button>
        <div className="flex items-center gap-2">
          <Award className="w-5 h-5 text-unoyellow" />
          <span className="text-sm font-black tracking-widest text-slate-300">DOSTI <span className="text-unoyellow">CARDS</span></span>
        </div>
      </header>

      {/* Main Stats list */}
      <main className="w-full max-w-3xl mx-auto my-auto py-6 z-10 flex-1 flex flex-col justify-center">
        <div className="glass p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl space-y-6">
          <div className="text-center">
            <h1 className="text-3xl font-black text-white tracking-tight uppercase">Leaderboard</h1>
            <p className="text-slate-400 text-xs mt-1">High-scores achieved by players globally</p>
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
                className={`px-4 py-2.5 rounded-xl text-xs font-extrabold uppercase tracking-wider transition-all ${
                  filter === tab.id
                    ? 'bg-unoblue text-white shadow shadow-blue-500/15'
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
              <Loader2 className="w-8 h-8 animate-spin text-unoblue" />
              <span className="text-xs font-bold uppercase tracking-wider">Loading rankings...</span>
            </div>
          ) : error ? (
            <div className="p-4 rounded-2xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs font-bold text-center">
              {error}
            </div>
          ) : stats.length === 0 ? (
            <div className="h-64 flex flex-col items-center justify-center text-slate-500 text-center">
              <Award className="w-12 h-12 opacity-20 mb-2" />
              <p className="text-sm">No scores registered yet. Play a game to record stats!</p>
            </div>
          ) : (
            /* Stats Table list */
            <div className="overflow-x-auto scrollbar-none rounded-2xl border border-white/5 bg-slate-950/20 shadow-inner">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="border-b border-white/5 bg-white/5 text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">
                    <th className="py-3 px-4">Rank</th>
                    <th className="py-3 px-4">Username</th>
                    <th className="py-3 px-4 text-center">Wins</th>
                    <th className="py-3 px-4 text-center">Played</th>
                    <th className="py-3 px-4 text-center">Winrate</th>
                    <th className="py-3 px-4 text-right">Points</th>
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
                        {p.username}
                      </td>
                      <td className="py-3 px-4 text-center">{p.wins}</td>
                      <td className="py-3 px-4 text-center">{p.games_played}</td>
                      <td className="py-3 px-4 text-center text-xs">
                        {p.win_percentage}%
                      </td>
                      <td className="py-3 px-4 text-right text-unoyellow font-black text-base">
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
        Dosti Cards Leaderboard &bull; Updated real-time
      </footer>
    </div>
  );
};

export default Leaderboard;
