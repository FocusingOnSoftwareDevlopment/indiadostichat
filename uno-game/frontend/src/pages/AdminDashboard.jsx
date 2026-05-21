import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  Shield, 
  Activity, 
  History, 
  UserX, 
  LogOut, 
  RefreshCw, 
  Trash2, 
  Unlock, 
  Eye, 
  AlertTriangle, 
  PlusCircle, 
  Gamepad2, 
  ChevronRight,
  Database
} from 'lucide-react';
import soundManager from '../utils/SoundManager';

const AdminDashboard = () => {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('rooms');
  const [token, setToken] = useState(() => localStorage.getItem('dosti_admin_token') || '');
  
  // Data States
  const [activeRooms, setActiveRooms] = useState([]);
  const [bans, setBans] = useState([]);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');

  // Ban Form States
  const [banType, setBanType] = useState('username');
  const [banValue, setBanValue] = useState('');
  const [banReason, setBanReason] = useState('');

  // Confirmations
  const [confirmReset, setConfirmReset] = useState(false);

  // Resolve API URL dynamically
  const apiUrl = import.meta.env.VITE_API_URL || 
    (window.location.hostname === 'localhost' ? 'http://localhost:5000/Duno-room' : window.location.origin + '/Duno-room');

  useEffect(() => {
    if (!token) {
      navigate('/admin/login');
    } else {
      fetchData();
    }
  }, [token, activeTab]);

  const fetchData = async () => {
    setLoading(true);
    setError('');
    try {
      const headers = { 'Authorization': `Bearer ${token}` };
      
      if (activeTab === 'rooms') {
        const res = await fetch(`${apiUrl}/api/admin/active-rooms`, { headers });
        if (!res.ok) handleAuthError(res);
        const data = await res.json();
        setActiveRooms(data);
      } else if (activeTab === 'bans') {
        const res = await fetch(`${apiUrl}/api/admin/bans`, { headers });
        if (!res.ok) handleAuthError(res);
        const data = await res.json();
        setBans(data);
      } else if (activeTab === 'history') {
        const res = await fetch(`${apiUrl}/api/admin/history`, { headers });
        if (!res.ok) handleAuthError(res);
        const data = await res.json();
        setHistory(data);
      }
    } catch (err) {
      setError(err.message || 'Error fetching admin data.');
    } finally {
      setLoading(false);
    }
  };

  const handleAuthError = (res) => {
    if (res.status === 401 || res.status === 403) {
      localStorage.removeItem('dosti_admin_token');
      localStorage.removeItem('dosti_admin_user');
      navigate('/admin/login');
      throw new Error('Session expired. Please log in again.');
    }
    throw new Error('Failed to load data from server.');
  };

  const handleLogout = () => {
    soundManager.play('click');
    localStorage.removeItem('dosti_admin_token');
    localStorage.removeItem('dosti_admin_user');
    navigate('/admin/login');
  };

  // Actions
  const handleForceEnd = async (roomId) => {
    if (!window.confirm(`Are you sure you want to FORCE END game room ${roomId}? This will boot all active players.`)) return;
    setActionLoading(true);
    soundManager.play('click');
    try {
      const res = await fetch(`${apiUrl}/api/admin/force-end/${roomId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        }
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to end room.');
      showSuccess(`Room ${roomId} terminated.`);
      fetchData();
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleKickPlayer = async (roomId, username) => {
    if (!window.confirm(`Are you sure you want to KICK player ${username} from room ${roomId}?`)) return;
    setActionLoading(true);
    soundManager.play('click');
    try {
      const res = await fetch(`${apiUrl}/api/admin/kick`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ roomId, username })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to kick player.');
      showSuccess(`Kicked ${username} successfully.`);
      fetchData();
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleAddBan = async (e) => {
    e.preventDefault();
    if (!banValue.trim()) return;
    setActionLoading(true);
    soundManager.play('click');
    setError('');
    try {
      const res = await fetch(`${apiUrl}/api/admin/ban`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          banType,
          banValue: banValue.trim(),
          reason: banReason.trim() || 'Banned by Admin'
        })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to apply ban.');
      
      showSuccess(`Successfully banned ${banValue}.`);
      setBanValue('');
      setBanReason('');
      fetchData();
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleUnban = async (banValue) => {
    setActionLoading(true);
    soundManager.play('click');
    try {
      const res = await fetch(`${apiUrl}/api/admin/unban`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ banValue })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to remove ban.');
      
      showSuccess(`Successfully unbanned ${banValue}.`);
      fetchData();
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleResetLeaderboard = async () => {
    if (!confirmReset) {
      setConfirmReset(true);
      soundManager.play('warning');
      return;
    }
    setActionLoading(true);
    soundManager.play('click');
    try {
      const res = await fetch(`${apiUrl}/api/admin/reset-leaderboard`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to reset leaderboard.');
      
      showSuccess('Leaderboard reset successfully.');
      setConfirmReset(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const showSuccess = (msg) => {
    setSuccessMsg(msg);
    setTimeout(() => setSuccessMsg(''), 4000);
  };

  const handleTabChange = (tab) => {
    soundManager.play('click');
    setActiveTab(tab);
  };

  return (
    <div className="min-h-screen animated-bg flex flex-col justify-between p-4 sm:p-6 relative text-slate-100">
      <div className="absolute top-[-10%] right-[-5%] w-96 h-96 rounded-full bg-indigo-900/10 blur-[120px] pointer-events-none"></div>

      {/* Header bar */}
      <header className="w-full max-w-6xl mx-auto flex items-center justify-between z-10 border-b border-white/5 pb-4 mb-6">
        <div className="flex items-center gap-3">
          <div className="bg-slate-800 p-2 rounded-xl border border-white/10 flex items-center justify-center">
            <Shield className="w-5 h-5 text-amber-500" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-base font-black tracking-widest text-slate-200">HEISENBERG</span>
              <span className="text-[10px] px-2 py-0.5 rounded-full bg-red-500/20 border border-red-500/30 text-red-400 font-extrabold uppercase">ROOT</span>
            </div>
            <p className="text-slate-400 text-[10px] uppercase tracking-wider">DUNO: DRAGON CARD CLASH SECURE CONTROLLER</p>
          </div>
        </div>
        <button
          onClick={handleLogout}
          className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-red-950/20 hover:bg-red-950/40 border border-red-500/20 hover:border-red-500/40 text-xs font-bold uppercase tracking-wider text-red-200 transition-all hover:scale-105"
        >
          <LogOut className="w-3.5 h-3.5" />
          Disconnect
        </button>
      </header>

      {/* Main dashboard content container */}
      <main className="w-full max-w-6xl mx-auto flex-1 z-10 grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Sidebar Nav */}
        <section className="lg:col-span-1 flex flex-row lg:flex-col gap-2 overflow-x-auto pb-2 lg:pb-0 scrollbar-none">
          <button
            onClick={() => handleTabChange('rooms')}
            className={`flex items-center gap-3 px-4 py-3.5 rounded-2xl border text-xs font-extrabold uppercase tracking-widest transition-all w-full min-w-[140px] ${
              activeTab === 'rooms'
                ? 'bg-white/10 border-white/20 text-white shadow-lg'
                : 'bg-white/5 border-white/5 text-slate-400 hover:bg-white/10 hover:text-slate-200'
            }`}
          >
            <Activity className="w-4 h-4 text-amber-500" />
            Active Arenas
          </button>
          <button
            onClick={() => handleTabChange('bans')}
            className={`flex items-center gap-3 px-4 py-3.5 rounded-2xl border text-xs font-extrabold uppercase tracking-widest transition-all w-full min-w-[140px] ${
              activeTab === 'bans'
                ? 'bg-white/10 border-white/20 text-white shadow-lg'
                : 'bg-white/5 border-white/5 text-slate-400 hover:bg-white/10 hover:text-slate-200'
            }`}
          >
            <UserX className="w-4 h-4 text-red-500" />
            Bans Control
          </button>
          <button
            onClick={() => handleTabChange('history')}
            className={`flex items-center gap-3 px-4 py-3.5 rounded-2xl border text-xs font-extrabold uppercase tracking-widest transition-all w-full min-w-[140px] ${
              activeTab === 'history'
                ? 'bg-white/10 border-white/20 text-white shadow-lg'
                : 'bg-white/5 border-white/5 text-slate-400 hover:bg-white/10 hover:text-slate-200'
            }`}
          >
            <History className="w-4 h-4 text-amber-400" />
            Battle Ledger
          </button>
          <button
            onClick={() => handleTabChange('database')}
            className={`flex items-center gap-3 px-4 py-3.5 rounded-2xl border text-xs font-extrabold uppercase tracking-widest transition-all w-full min-w-[140px] ${
              activeTab === 'database'
                ? 'bg-white/10 border-white/20 text-white shadow-lg'
                : 'bg-white/5 border-white/5 text-slate-400 hover:bg-white/10 hover:text-slate-200'
            }`}
          >
            <Database className="w-4 h-4 text-emerald-400" />
            DB Utilities
          </button>
        </section>

        {/* Content Pane */}
        <section className="lg:col-span-3">
          <div className="glass rounded-3xl p-6 border border-white/10 flex flex-col h-full min-h-[500px]">
            {/* Header info */}
            <div className="flex items-center justify-between border-b border-white/5 pb-4 mb-6">
              <div>
                <h2 className="text-lg font-black text-white uppercase tracking-tight">
                  {activeTab === 'rooms' && 'Active Dragon Arena Matches'}
                  {activeTab === 'bans' && 'Network Ban Registry'}
                  {activeTab === 'history' && 'Completed Match Ledger'}
                  {activeTab === 'database' && 'System Database Operations'}
                </h2>
                <p className="text-slate-400 text-xs mt-0.5">
                  {activeTab === 'rooms' && 'Manage running lobbies and active dragon card clash tables'}
                  {activeTab === 'bans' && 'Blacklist malicious IPs or players permanently'}
                  {activeTab === 'history' && 'Audit logs of completed game outcomes'}
                  {activeTab === 'database' && 'Root database commands and score resets'}
                </p>
              </div>

              {activeTab !== 'database' && (
                <button
                  onClick={fetchData}
                  disabled={loading}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-[10px] font-extrabold uppercase tracking-wider text-slate-300 transition-colors"
                >
                  <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
                  Sync
                </button>
              )}
            </div>

            {/* Notification center */}
            {error && (
              <div className="mb-4 p-3 rounded-xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs font-bold text-center">
                {error}
              </div>
            )}
            {successMsg && (
              <div className="mb-4 p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-200 text-xs font-bold text-center">
                {successMsg}
              </div>
            )}

            {/* Core Tab Renderers */}
            <div className="flex-1">
              {loading ? (
                <div className="h-64 flex flex-col items-center justify-center gap-2">
                  <RefreshCw className="w-8 h-8 animate-spin text-indigo-400" />
                  <span className="text-xs uppercase tracking-widest font-extrabold text-slate-500">Querying Server...</span>
                </div>
              ) : (
                <>
                  {/* LOBBY / ROOMS TAB */}
                  {activeTab === 'rooms' && (
                    <div className="space-y-4">
                      {activeRooms.length === 0 ? (
                        <div className="h-48 rounded-2xl border border-dashed border-white/5 flex flex-col items-center justify-center text-slate-500">
                          <Gamepad2 className="w-8 h-8 mb-2 opacity-40 text-slate-400" />
                          <span className="text-xs font-bold uppercase tracking-widest">No Active Game Rooms Found</span>
                        </div>
                      ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                          {activeRooms.map((room) => (
                            <div key={room.roomId} className="bg-slate-950/40 border border-white/5 rounded-2xl p-4 flex flex-col justify-between">
                              <div>
                                <div className="flex items-center justify-between mb-2">
                                  <span className="text-xs font-black uppercase tracking-wider text-indigo-300">Room: {room.roomId}</span>
                                  <span className={`text-[9px] px-2 py-0.5 rounded-full font-bold uppercase ${
                                    room.status === 'playing' 
                                      ? 'bg-emerald-500/10 border border-emerald-500/20 text-emerald-400' 
                                      : 'bg-amber-500/10 border border-amber-500/20 text-amber-400'
                                  }`}>
                                    {room.status}
                                  </span>
                                </div>

                                <div className="text-[11px] text-slate-400 space-y-1.5 mb-4">
                                  <div className="flex justify-between border-b border-white/5 pb-1">
                                    <span>Players ({room.players.length}/8):</span>
                                    <span className="text-white font-bold">{room.players.map(p => p.username).join(', ')}</span>
                                  </div>
                                  <div className="flex justify-between border-b border-white/5 pb-1">
                                    <span>Privacy:</span>
                                    <span className="text-slate-300">{room.isPrivate ? 'Private Key' : 'Public Lobby'}</span>
                                  </div>
                                  {room.status === 'playing' && (
                                    <>
                                      <div className="flex justify-between border-b border-white/5 pb-1">
                                        <span>Current Turn:</span>
                                        <span className="text-slate-300 font-bold">{room.activePlayerName || 'None'}</span>
                                      </div>
                                      <div className="flex justify-between border-b border-white/5 pb-1">
                                        <span>Timeout Timer:</span>
                                        <span className="text-red-400 font-bold">{room.secondsRemaining}s</span>
                                      </div>
                                    </>
                                  )}
                                </div>
                              </div>

                              {/* Actions inside individual room */}
                              <div className="flex gap-2 mt-2 pt-2 border-t border-white/5">
                                <button
                                  onClick={() => {
                                    soundManager.play('click');
                                    navigate(`/admin/spectate/${room.roomId}`);
                                  }}
                                  className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-[10px] font-bold uppercase tracking-wider text-slate-200 transition-colors"
                                >
                                  <Eye className="w-3 h-3 text-amber-500" />
                                  Spectate
                                </button>
                                <button
                                  onClick={() => handleForceEnd(room.roomId)}
                                  disabled={actionLoading}
                                  className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-xl bg-red-950/20 hover:bg-red-950/40 border border-red-500/10 hover:border-red-500/30 text-[10px] font-bold uppercase tracking-wider text-red-300 transition-colors"
                                >
                                  <Trash2 className="w-3 h-3" />
                                  Kill Match
                                </button>
                              </div>

                              {/* Player quick controls */}
                              {room.players.length > 0 && (
                                <div className="mt-3 bg-black/25 rounded-xl p-2.5 border border-white/5">
                                  <span className="block text-[8px] font-black text-slate-500 uppercase tracking-widest mb-1.5">Quick Player Ejections:</span>
                                  <div className="flex flex-wrap gap-1.5">
                                    {room.players.map(p => (
                                      <button
                                        key={p.username}
                                        onClick={() => handleKickPlayer(room.roomId, p.username)}
                                        className="text-[9px] bg-red-500/10 hover:bg-red-500/20 text-red-300 border border-red-500/25 px-2 py-0.5 rounded-md font-extrabold flex items-center gap-1 transition-all"
                                      >
                                        {p.username}
                                        <span className="text-[7px] text-red-500">✕</span>
                                      </button>
                                    ))}
                                  </div>
                                </div>
                              )}
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}

                  {/* BANS TAB */}
                  {activeTab === 'bans' && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                      {/* Left: Ban addition form */}
                      <div className="md:col-span-1 bg-slate-950/30 rounded-2xl p-4 border border-white/5 h-fit">
                        <h3 className="text-xs font-black text-white uppercase tracking-wider mb-4 flex items-center gap-2">
                          <PlusCircle className="w-4 h-4 text-red-500" />
                          Issue New Ban
                        </h3>
                        <form onSubmit={handleAddBan} className="space-y-4">
                          <div>
                            <label className="block text-[9px] font-black uppercase text-slate-400 mb-1.5">Ban Context</label>
                            <select
                              value={banType}
                              onChange={(e) => setBanType(e.target.value)}
                              className="w-full bg-slate-900 border border-white/10 rounded-xl px-3 py-2 text-xs font-bold text-slate-200 focus:outline-none"
                            >
                              <option value="username">Username Registry Ban</option>
                              <option value="ip">IPv4 Address Ban</option>
                            </select>
                          </div>

                          <div>
                            <label className="block text-[9px] font-black uppercase text-slate-400 mb-1.5">
                              {banType === 'username' ? 'Username Value' : 'IPv4 Address'}
                            </label>
                            <input
                              type="text"
                              value={banValue}
                              onChange={(e) => setBanValue(e.target.value)}
                              placeholder={banType === 'username' ? 'badPlayer123' : '12.34.56.78'}
                              required
                              className="w-full bg-slate-900 border border-white/10 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-600 focus:outline-none focus:border-slate-500"
                            />
                          </div>

                          <div>
                            <label className="block text-[9px] font-black uppercase text-slate-400 mb-1.5">Reason for Action</label>
                            <input
                              type="text"
                              value={banReason}
                              onChange={(e) => setBanReason(e.target.value)}
                              placeholder="Spamming Chat / Glitching"
                              className="w-full bg-slate-900 border border-white/10 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-600 focus:outline-none focus:border-slate-500"
                            />
                          </div>

                          <button
                            type="submit"
                            disabled={actionLoading || !banValue.trim()}
                            className="w-full py-2.5 rounded-xl bg-red-700 hover:bg-red-650 disabled:opacity-50 text-white font-extrabold text-xs uppercase tracking-widest transition-transform hover:scale-[1.02]"
                          >
                            Add Ban Rule
                          </button>
                        </form>
                      </div>

                      {/* Right: Active Bans display */}
                      <div className="md:col-span-2 space-y-3">
                        <h3 className="text-xs font-black text-white uppercase tracking-wider mb-2">Active Blacklists ({bans.length})</h3>
                        {bans.length === 0 ? (
                          <div className="h-48 rounded-2xl border border-dashed border-white/5 flex flex-col items-center justify-center text-slate-500">
                            <span className="text-xs font-bold uppercase tracking-widest">No active bans registered.</span>
                          </div>
                        ) : (
                          <div className="max-h-[350px] overflow-y-auto space-y-2 pr-1">
                            {bans.map((ban) => (
                              <div key={ban.id} className="bg-slate-950/40 border border-white/5 rounded-xl p-3 flex items-center justify-between">
                                <div className="flex items-center gap-3">
                                  <div className={`px-2 py-0.5 rounded text-[8px] font-black uppercase ${
                                    ban.ban_type === 'username' ? 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/20' : 'bg-amber-500/20 text-amber-300 border border-amber-500/20'
                                  }`}>
                                    {ban.ban_type}
                                  </div>
                                  <div>
                                    <div className="text-xs font-bold text-white">{ban.ban_value}</div>
                                    <div className="text-[10px] text-slate-400">Reason: {ban.reason}</div>
                                  </div>
                                </div>
                                <button
                                  onClick={() => handleUnban(ban.ban_value)}
                                  disabled={actionLoading}
                                  className="p-2 rounded-xl bg-emerald-950/20 hover:bg-emerald-950/40 border border-emerald-500/20 text-emerald-400 hover:text-emerald-300 transition-colors flex items-center gap-1 text-[9px] font-extrabold uppercase tracking-wide"
                                >
                                  <Unlock className="w-3 h-3" />
                                  Unban
                                </button>
                              </div>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                  )}

                  {/* HISTORY LEDGER TAB */}
                  {activeTab === 'history' && (
                    <div className="space-y-4">
                      {history.length === 0 ? (
                        <div className="h-48 rounded-2xl border border-dashed border-white/5 flex flex-col items-center justify-center text-slate-500">
                          <span className="text-xs font-bold uppercase tracking-widest">No completed matches recorded yet.</span>
                        </div>
                      ) : (
                        <div className="overflow-x-auto rounded-2xl border border-white/5">
                          <table className="w-full text-left border-collapse bg-slate-950/30">
                            <thead>
                              <tr className="border-b border-white/10 text-[9px] font-black text-slate-400 uppercase tracking-wider bg-black/20">
                                <th className="px-4 py-3">Room ID</th>
                                <th className="px-4 py-3">Winner</th>
                                <th className="px-4 py-3">Score</th>
                                <th className="px-4 py-3">Players Hand List</th>
                                <th className="px-4 py-3 text-right">Date/Time</th>
                              </tr>
                            </thead>
                            <tbody className="divide-y divide-white/5 text-xs">
                              {history.map((row) => (
                                <tr key={row.id} className="hover:bg-white/[0.02] text-slate-300">
                                  <td className="px-4 py-3 font-mono text-[10px] uppercase text-indigo-400">{row.room_id}</td>
                                  <td className="px-4 py-3 font-bold text-white">{row.winner_username}</td>
                                  <td className="px-4 py-3 font-bold text-amber-400">+{row.score_awarded}</td>
                                  <td className="px-4 py-3 text-slate-400 max-w-[200px] truncate">
                                    {Array.isArray(row.players_list) 
                                      ? row.players_list.map(p => `${p.username} (${p.score})`).join(', ') 
                                      : JSON.stringify(row.players_list)}
                                  </td>
                                  <td className="px-4 py-3 text-right text-[10px] text-slate-500">
                                    {new Date(row.created_at).toLocaleString()}
                                  </td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      )}
                    </div>
                  )}

                  {/* DATABASE UTILITIES TAB */}
                  {activeTab === 'database' && (
                    <div className="space-y-6 max-w-xl">
                      <div className="bg-red-500/5 border border-red-500/10 rounded-2xl p-5 flex gap-4">
                        <AlertTriangle className="w-8 h-8 text-red-500 shrink-0 mt-1" />
                        <div>
                          <h3 className="text-sm font-black text-white uppercase tracking-wider mb-1">DANGER ZONE</h3>
                          <p className="text-slate-400 text-xs leading-relaxed mb-4">
                            Executing database purges cannot be reverted. Make sure you back up production schemas before resetting statistics.
                          </p>

                          <div className="space-y-4">
                            <div className="p-4 bg-slate-950/60 rounded-xl border border-white/5">
                              <h4 className="text-xs font-bold text-white uppercase mb-2">Truncate Leaderboard Rankings</h4>
                              <p className="text-slate-400 text-[10px] leading-relaxed mb-3">
                                Resets wins, matches, and scores to zero for all players globally, but retains user accounts and historic match logs.
                              </p>
                              <button
                                onClick={handleResetLeaderboard}
                                disabled={actionLoading}
                                className={`px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider border transition-all ${
                                  confirmReset 
                                    ? 'bg-red-600 border-red-700 text-white animate-pulse'
                                    : 'bg-red-950/20 hover:bg-red-950/40 border-red-500/20 text-red-200'
                                }`}
                              >
                                {confirmReset ? 'CONFIRM LEADERBOARD RESET?' : 'Truncate Leaderboard'}
                              </button>
                              {confirmReset && (
                                <button
                                  onClick={() => setConfirmReset(false)}
                                  className="ml-3 text-[10px] font-extrabold uppercase tracking-widest text-slate-400 underline"
                                >
                                  Cancel
                                </button>
                              )}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                </>
              )}
            </div>
          </div>
        </section>
      </main>

      <footer className="w-full text-center text-slate-600 text-[10px] uppercase tracking-widest z-10 pt-8 max-w-6xl mx-auto">
        Heisenberg Controller &bull; Encrypted Node Session
      </footer>
    </div>
  );
};

export default AdminDashboard;
