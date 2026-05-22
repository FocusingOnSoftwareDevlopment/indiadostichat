import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  Shield, 
  ArrowLeft, 
  RefreshCw, 
  Compass, 
  Trash2, 
  UserMinus, 
  Play, 
  List, 
  EyeOff
} from 'lucide-react';
import { useSocket } from '../context/SocketContext';
import UnoCard from '../components/UnoCard';
import soundManager from '../utils/SoundManager';

const AdminSpectate = () => {
  const { roomId } = useParams();
  const navigate = useNavigate();
  const { socket, connected } = useSocket();

  const [spectateState, setSpectateState] = useState(null);
  const [error, setError] = useState('');
  const [joined, setJoined] = useState(false);
  const [actionLoading, setActionLoading] = useState(false);
  const logEndRef = useRef(null);

  const token = localStorage.getItem('dosti_admin_token') || '';
  const apiUrl = import.meta.env.VITE_API_URL || 
    (window.location.hostname === 'localhost' ? 'http://localhost:5000/Duno-room' : 
     (window.location.hostname.includes('indiadostichat.com') ? 'http://103.86.176.185/Duno-room' : window.location.origin + '/Duno-room'));

  useEffect(() => {
    if (!token) {
      navigate('/admin/login');
      return;
    }

    if (!socket || !connected) return;

    // Join room spectating
    socket.emit('admin_spectate_join', { token, roomId }, (res) => {
      if (res.error) {
        setError(res.error);
        soundManager.play('error');
      } else {
        setJoined(true);
        soundManager.play('deal');
      }
    });

    const handleUpdate = (state) => {
      setSpectateState(state);
    };

    socket.on('admin_spectate_update', handleUpdate);

    return () => {
      socket.off('admin_spectate_update', handleUpdate);
      // Clean up spectator state in room
      socket.emit('leave_game');
    };
  }, [socket, connected, roomId, token, navigate]);

  // Autoscroll logs
  useEffect(() => {
    if (logEndRef.current) {
      logEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [spectateState?.logs]);

  const handleBack = () => {
    soundManager.play('click');
    navigate('/admin/dashboard');
  };

  const handleForceEnd = async () => {
    if (!window.confirm('Are you sure you want to FORCE END this game? This will boot everyone.')) return;
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
      navigate('/admin/dashboard');
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleKickPlayer = async (username) => {
    if (!window.confirm(`Kick player ${username}?`)) return;
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
      soundManager.play('click');
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleBanPlayer = async (username) => {
    if (!window.confirm(`Are you sure you want to BAN and KICK ${username}?`)) return;
    setActionLoading(true);
    soundManager.play('click');
    try {
      const res = await fetch(`${apiUrl}/api/admin/ban`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          banType: 'username',
          banValue: username,
          reason: 'Banned in-game by Admin'
        })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to ban player.');
      soundManager.play('warning');
    } catch (err) {
      setError(err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const clanNames = {
    red: 'Fire Clan',
    blue: 'Ice Clan',
    green: 'Forest Clan',
    yellow: 'Thunder Clan',
  };

  const renderColorDot = (color) => {
    const dots = {
      red: 'bg-unored',
      blue: 'bg-unoblue',
      green: 'bg-unogreen',
      yellow: 'bg-unoyellow',
      wild: 'bg-slate-400'
    };
    return <span className={`inline-block w-3 h-3 rounded-full border border-white/20 ${dots[color] || 'bg-slate-400'}`}></span>;
  };

  return (
    <div className="min-h-screen animated-bg flex flex-col justify-between p-4 sm:p-6 relative text-slate-100">
      {/* Background elements */}
      <div className="absolute top-[-10%] right-[-5%] w-96 h-96 rounded-full bg-slate-900/10 blur-[120px] pointer-events-none"></div>

      {/* Header bar */}
      <header className="w-full max-w-6xl mx-auto flex items-center justify-between z-10 border-b border-white/5 pb-4 mb-6">
        <div className="flex items-center gap-3">
          <button
            onClick={handleBack}
            className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-xs font-bold uppercase tracking-wider text-slate-200 transition-colors"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            Terminal
          </button>
          <div className="hidden sm:block">
            <span className="text-xs font-black tracking-widest text-slate-400">INVISIBLE SPECTATOR &bull; ROOM: <span className="text-white uppercase font-mono">{roomId}</span></span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <EyeOff className="w-4 h-4 text-slate-400 animate-pulse" />
          <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-800 border border-white/10 font-bold uppercase text-slate-400">GHOST MODE</span>
          <button
            onClick={handleForceEnd}
            disabled={actionLoading || !spectateState}
            className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-red-950/20 hover:bg-red-950/40 border border-red-500/20 text-xs font-bold uppercase tracking-wider text-red-300 transition-colors"
          >
            <Trash2 className="w-3.5 h-3.5" />
            Kill Room
          </button>
        </div>
      </header>

      {/* Connection warning */}
      {!connected && (
        <div className="w-full max-w-6xl mx-auto mb-4 p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-200 text-xs text-center font-bold">
          Connecting to Socket Gateway...
        </div>
      )}

      {error && (
        <div className="w-full max-w-6xl mx-auto mb-4 p-3 rounded-xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs text-center font-bold">
          {error}
        </div>
      )}

      {/* Main Board view */}
      <main className="w-full max-w-6xl mx-auto flex-1 z-10 grid grid-cols-1 lg:grid-cols-4 gap-6 items-start">
        {/* Left 3 columns: Game state & Players list */}
        <section className="lg:col-span-3 space-y-6">
          {!spectateState ? (
            <div className="glass rounded-3xl p-12 border border-white/10 flex flex-col items-center justify-center text-slate-500 h-[450px]">
              <RefreshCw className="w-8 h-8 animate-spin text-slate-400 mb-3" />
              <span className="text-xs font-black uppercase tracking-widest">Awaiting match sync coordinates...</span>
            </div>
          ) : (
            <>
              {/* Central Deck & Discard layout */}
              <div className="glass rounded-3xl p-6 border border-white/10 flex flex-col sm:flex-row items-center justify-around gap-6 bg-slate-950/20 relative overflow-hidden">
                <div className="absolute top-[-50px] right-[-50px] w-48 h-48 rounded-full bg-slate-900/10 blur-3xl pointer-events-none"></div>

                <div className="flex flex-col items-center justify-center text-center">
                  <span className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-1">Top Discard Card</span>
                  {spectateState.topCard ? (
                    <UnoCard card={spectateState.topCard} isPlayable={false} size="md" />
                  ) : (
                    <div className="w-24 h-36 border-4 border-dashed border-white/10 rounded-xl flex items-center justify-center text-slate-600 text-xs font-black uppercase">
                      Empty
                    </div>
                  )}
                </div>

                {/* Turn Info & Compass */}
                <div className="flex flex-col items-center justify-center text-center py-4 px-6 rounded-2xl bg-black/20 border border-white/5 min-w-[200px]">
                  <Compass className={`w-8 h-8 text-indigo-400 mb-2 ${spectateState.direction === 1 ? 'animate-spin-slow' : 'animate-spin-reverse-slow'}`} />
                  <div className="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">Direction of Play</div>
                  <div className="text-xs font-black text-white mt-1">
                    {spectateState.direction === 1 ? 'Clockwise ↻' : 'Counter-Clockwise ↺'}
                  </div>

                  <div className="mt-4 border-t border-white/5 pt-3 w-full">
                    <div className="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">Active Clan</div>
                    <div className="flex items-center justify-center gap-1.5 mt-1 text-xs font-black text-white capitalize">
                      {renderColorDot(spectateState.currentColor)}
                      {clanNames[spectateState.currentColor] || spectateState.currentColor}
                    </div>
                  </div>

                  <div className="mt-4 border-t border-white/5 pt-3 w-full">
                    <div className="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">Current Play Turn</div>
                    <div className="text-xs font-black text-unoyellow mt-1">
                      {spectateState.players[spectateState.currentTurn]?.username || 'Waiting'}
                    </div>
                    {spectateState.status === 'playing' && (
                      <div className="text-[10px] text-red-400 font-extrabold mt-0.5">
                        Time Remaining: {spectateState.secondsRemaining}s
                      </div>
                    )}
                  </div>
                </div>

                <div className="flex flex-col items-center justify-center text-center">
                  <span className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-1">State Summary</span>
                  <div className="space-y-1">
                    <div className="text-2xl font-black text-white uppercase tracking-tight">{spectateState.status}</div>
                    <p className="text-[10px] text-indigo-300 font-bold uppercase tracking-wider">Players Joined: {spectateState.players.length}/8</p>
                  </div>
                </div>
              </div>

              {/* Revealed Hands of all players */}
              <div className="space-y-4">
                <h3 className="text-xs font-black text-white uppercase tracking-widest border-l-2 border-unoblue pl-2">Revealed Cards Hands</h3>
                {spectateState.players.map((player, idx) => {
                  const isTurn = spectateState.currentTurn === idx && spectateState.status === 'playing';
                  return (
                    <div 
                      key={player.username} 
                      className={`glass rounded-2xl p-4 border transition-all ${
                        isTurn 
                          ? 'border-indigo-500/40 bg-indigo-950/10 shadow-lg' 
                          : 'border-white/5 bg-slate-950/30'
                      }`}
                    >
                      <div className="flex items-center justify-between border-b border-white/5 pb-2 mb-3">
                        <div className="flex items-center gap-2">
                          <span className={`w-2.5 h-2.5 rounded-full ${player.active ? 'bg-emerald-400' : 'bg-red-400'}`}></span>
                          <span className="text-xs font-black text-white">{player.username}</span>
                          {idx === 0 && <span className="text-[8px] font-black uppercase bg-indigo-500/20 text-indigo-300 border border-indigo-500/20 px-1.5 py-0.5 rounded">Host</span>}
                          {isTurn && <span className="text-[8px] font-black uppercase bg-unoyellow/20 text-unoyellow border border-unoyellow/20 px-1.5 py-0.5 rounded animate-pulse">Active Turn</span>}
                        </div>
                        <div className="flex items-center gap-3">
                          <span className="text-[10px] font-bold text-slate-400">Cards: {player.cardsCount}</span>
                          <div className="flex gap-1.5">
                            <button
                              onClick={() => handleKickPlayer(player.username)}
                              disabled={actionLoading}
                              className="text-[9px] bg-red-950/20 hover:bg-red-950/40 border border-red-500/10 hover:border-red-500/30 text-red-300 px-2 py-0.5 rounded font-extrabold flex items-center gap-0.5 transition-colors"
                            >
                              <UserMinus className="w-2.5 h-2.5" />
                              Kick
                            </button>
                            <button
                              onClick={() => handleBanPlayer(player.username)}
                              disabled={actionLoading}
                              className="text-[9px] bg-red-900/30 hover:bg-red-900/50 border border-red-500/25 text-red-200 px-2 py-0.5 rounded font-extrabold flex items-center gap-0.5 transition-colors animate-pulse"
                            >
                              ✕ Ban
                            </button>
                          </div>
                        </div>
                      </div>

                      {/* Display player's cards horizontally */}
                      {player.cards && player.cards.length > 0 ? (
                        <div className="flex flex-wrap gap-2 pr-2">
                          {player.cards.map((card) => (
                            <UnoCard key={card.id} card={card} isPlayable={false} size="sm" className="hover:scale-105 active:scale-100 hover:translate-y-0" />
                          ))}
                        </div>
                      ) : (
                        <div className="text-[10px] font-bold text-slate-500 italic uppercase">No cards in hand (Lobby / Finished)</div>
                      )}
                    </div>
                  );
                })}
              </div>
            </>
          )}
        </section>

        {/* Right 1 column: Game logs ledger */}
        <section className="lg:col-span-1 glass rounded-3xl p-4 border border-white/10 flex flex-col h-[550px] bg-slate-950/20">
          <h3 className="text-xs font-black text-white uppercase tracking-widest border-b border-white/5 pb-2 mb-3 flex items-center gap-1.5">
            <List className="w-3.5 h-3.5 text-indigo-400" />
            Match Logs
          </h3>

          <div className="flex-1 overflow-y-auto space-y-2 pr-1 scrollbar-none text-xs sm:text-sm font-semibold leading-normal">
            {spectateState?.logs && spectateState.logs.length > 0 ? (
              spectateState.logs.map((log, index) => (
                <div key={index} className="p-2.5 rounded-lg bg-slate-900/60 text-slate-200 border-l-3 border-indigo-500/50">
                  {log}
                </div>
              ))
            ) : (
              <div className="h-full flex items-center justify-center text-slate-600 font-sans italic text-center text-xs">
                No logs recorded yet. Match starting.
              </div>
            )}
            <div ref={logEndRef} />
          </div>
        </section>
      </main>

      <footer className="w-full text-center text-slate-600 text-[10px] uppercase tracking-widest z-10 pt-8 max-w-6xl mx-auto">
        Invisible Admin Session &bull; Secured Channel
      </footer>
    </div>
  );
};

export default AdminSpectate;
