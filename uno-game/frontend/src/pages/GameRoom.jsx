import React, { useState, useEffect, useMemo } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useSocket } from '../context/SocketContext';
import UnoCard from '../components/UnoCard';
import ColorWheel from '../components/ColorWheel';
import Chat from '../components/Chat';
import { Copy, Play, LogOut, Check, Shield, Users, MessageCircle, Volume2, VolumeX, RefreshCw, Link } from 'lucide-react';
import soundManager from '../utils/SoundManager';

const CornerDragons = () => {
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-0 select-none">
      {/* Top Left - Fire Dragon (Red Glow) */}
      <div className="absolute -top-4 -left-4 w-36 h-36 md:w-52 md:h-52 text-red-500/20 md:text-red-500/10 transform -rotate-12 transition-all duration-700 animate-pulse">
        <svg
          viewBox="0 0 100 100"
          fill="currentColor"
          className="w-full h-full"
          style={{ filter: 'drop-shadow(0 0 25px rgba(239, 68, 68, 0.6))' }}
        >
          <path d="M90,85 C85,80 75,70 65,65 C55,60 45,62 38,55 C35,52 38,48 42,48 C30,42 20,30 25,18 C28,15 32,18 30,22 C35,16 42,10 48,12 C44,18 43,24 45,28 C50,22 56,18 65,20 C58,25 55,30 54,35 C62,32 70,32 78,38 C70,40 62,42 58,48 C65,48 72,52 75,58 C68,58 60,56 55,62 C62,68 70,72 80,75 C70,75 60,72 52,78 C58,82 65,85 75,88 C60,88 50,82 45,75 C40,82 32,88 20,90 C35,88 42,80 44,72 C35,75 28,75 20,70 C30,70 38,65 40,58 C32,58 25,55 18,48 C28,48 34,52 38,45 C28,40 22,35 15,25 C25,30 32,35 34,42 C36,32 34,22 28,15 C38,20 44,28 42,38 C46,28 52,22 60,18 C54,24 52,32 50,38 C56,32 64,28 72,28 C64,32 58,38 56,44 C62,38 70,36 78,38 C70,42 62,45 58,52 C64,52 70,55 74,60 C66,60 58,58 54,64 C60,70 66,74 74,78 C64,78 55,75 48,82 C54,85 60,88 68,90 C53,90 42,85 36,78 Z" />
          <circle cx="28" cy="22" r="1.5" className="fill-red-200 animate-pulse" />
        </svg>
      </div>

      {/* Top Right - Ice Dragon (Blue Glow) */}
      <div className="absolute -top-4 -right-4 w-36 h-36 md:w-52 md:h-52 text-cyan-400/20 md:text-cyan-400/10 transform scale-x-[-1] -rotate-12 transition-all duration-700 animate-pulse">
        <svg
          viewBox="0 0 100 100"
          fill="currentColor"
          className="w-full h-full"
          style={{ filter: 'drop-shadow(0 0 25px rgba(34, 211, 238, 0.6))' }}
        >
          <path d="M90,85 C85,80 75,70 65,65 C55,60 45,62 38,55 C35,52 38,48 42,48 C30,42 20,30 25,18 C28,15 32,18 30,22 C35,16 42,10 48,12 C44,18 43,24 45,28 C50,22 56,18 65,20 C58,25 55,30 54,35 C62,32 70,32 78,38 C70,40 62,42 58,48 C65,48 72,52 75,58 C68,58 60,56 55,62 C62,68 70,72 80,75 C70,75 60,72 52,78 C58,82 65,85 75,88 C60,88 50,82 45,75 C40,82 32,88 20,90 C35,88 42,80 44,72 C35,75 28,75 20,70 C30,70 38,65 40,58 C32,58 25,55 18,48 C28,48 34,52 38,45 C28,40 22,35 15,25 C25,30 32,35 34,42 C36,32 34,22 28,15 C38,20 44,28 42,38 C46,28 52,22 60,18 C54,24 52,32 50,38 C56,32 64,28 72,28 C64,32 58,38 56,44 C62,38 70,36 78,38 C70,42 62,45 58,52 C64,52 70,55 74,60 C66,60 58,58 54,64 C60,70 66,74 74,78 C64,78 55,75 48,82 C54,85 60,88 68,90 C53,90 42,85 36,78 Z" />
          <circle cx="28" cy="22" r="1.5" className="fill-cyan-100 animate-pulse" />
        </svg>
      </div>

      {/* Bottom Left - Forest Dragon (Green Glow) */}
      <div className="absolute -bottom-4 -left-4 w-36 h-36 md:w-52 md:h-52 text-emerald-500/20 md:text-emerald-500/10 transform scale-y-[-1] -rotate-12 transition-all duration-700 animate-pulse">
        <svg
          viewBox="0 0 100 100"
          fill="currentColor"
          className="w-full h-full"
          style={{ filter: 'drop-shadow(0 0 25px rgba(16, 185, 129, 0.6))' }}
        >
          <path d="M90,85 C85,80 75,70 65,65 C55,60 45,62 38,55 C35,52 38,48 42,48 C30,42 20,30 25,18 C28,15 32,18 30,22 C35,16 42,10 48,12 C44,18 43,24 45,28 C50,22 56,18 65,20 C58,25 55,30 54,35 C62,32 70,32 78,38 C70,40 62,42 58,48 C65,48 72,52 75,58 C68,58 60,56 55,62 C62,68 70,72 80,75 C70,75 60,72 52,78 C58,82 65,85 75,88 C60,88 50,82 45,75 C40,82 32,88 20,90 C35,88 42,80 44,72 C35,75 28,75 20,70 C30,70 38,65 40,58 C32,58 25,55 18,48 C28,48 34,52 38,45 C28,40 22,35 15,25 C25,30 32,35 34,42 C36,32 34,22 28,15 C38,20 44,28 42,38 C46,28 52,22 60,18 C54,24 52,32 50,38 C56,32 64,28 72,28 C64,32 58,38 56,44 C62,38 70,36 78,38 C70,42 62,45 58,52 C64,52 70,55 74,60 C66,60 58,58 54,64 C60,70 66,74 74,78 C64,78 55,75 48,82 C54,85 60,88 68,90 C53,90 42,85 36,78 Z" />
          <circle cx="28" cy="22" r="1.5" className="fill-emerald-200 animate-pulse" />
        </svg>
      </div>

      {/* Bottom Right - Thunder Dragon (Yellow Glow) */}
      <div className="absolute -bottom-4 -right-4 w-36 h-36 md:w-52 md:h-52 text-amber-400/20 md:text-amber-400/10 transform scale-x-[-1] scale-y-[-1] -rotate-12 transition-all duration-700 animate-pulse">
        <svg
          viewBox="0 0 100 100"
          fill="currentColor"
          className="w-full h-full"
          style={{ filter: 'drop-shadow(0 0 25px rgba(245, 158, 11, 0.6))' }}
        >
          <path d="M90,85 C85,80 75,70 65,65 C55,60 45,62 38,55 C35,52 38,48 42,48 C30,42 20,30 25,18 C28,15 32,18 30,22 C35,16 42,10 48,12 C44,18 43,24 45,28 C50,22 56,18 65,20 C58,25 55,30 54,35 C62,32 70,32 78,38 C70,40 62,42 58,48 C65,48 72,52 75,58 C68,58 60,56 55,62 C62,68 70,72 80,75 C70,75 60,72 52,78 C58,82 65,85 75,88 C60,88 50,82 45,75 C40,82 32,88 20,90 C35,88 42,80 44,72 C35,75 28,75 20,70 C30,70 38,65 40,58 C32,58 25,55 18,48 C28,48 34,52 38,45 C28,40 22,35 15,25 C25,30 32,35 34,42 C36,32 34,22 28,15 C38,20 44,28 42,38 C46,28 52,22 60,18 C54,24 52,32 50,38 C56,32 64,28 72,28 C64,32 58,38 56,44 C62,38 70,36 78,38 C70,42 62,45 58,52 C64,52 70,55 74,60 C66,60 58,58 54,64 C60,70 66,74 74,78 C64,78 55,75 48,82 C54,85 60,88 68,90 C53,90 42,85 36,78 Z" />
          <circle cx="28" cy="22" r="1.5" className="fill-amber-200 animate-pulse" />
        </svg>
      </div>
    </div>
  );
};

const GameRoom = () => {
  const { roomId } = useParams();
  const navigate = useNavigate();

  // Memoized embers array to prevent re-generating positions on render
  const embers = useMemo(() => {
    return Array.from({ length: 20 }).map((_, i) => ({
      id: i,
      left: `${Math.random() * 100}%`,
      size: `${Math.random() * 6 + 4}px`,
      duration: `${Math.random() * 8 + 6}s`,
      delay: `${Math.random() * 8}s`,
      drift: `${Math.random() * 80 - 40}px`,
    }));
  }, []);
  const {
    connected,
    username,
    gameState,
    lobbyPlayers,
    error,
    setError,
    chatMessages,
    toggleReady,
    startGame,
    playCard,
    drawCard,
    playDrawnCard,
    callUno,
    sendChat,
    leaveGame,
  } = useSocket();

  const [copySuccess, setCopySuccess] = useState(false);
  const [copyLinkSuccess, setCopyLinkSuccess] = useState(false);
  const [showChat, setShowChat] = useState(false);
  const [muted, setMuted] = useState(soundManager.isMuted());
  
  // Wild card state
  const [wildCardId, setWildCardId] = useState(null);
  const [showColorWheel, setShowColorWheel] = useState(false);
  
  // Drawn card state
  const [drawnPlayableCard, setDrawnPlayableCard] = useState(null);
  const [showDrawnDecision, setShowDrawnDecision] = useState(false);
  const [drawnWildColorSelect, setDrawnWildColorSelect] = useState(false);

  // Auto exit if username is cleared (session expired/direct url entry)
  useEffect(() => {
    if (!username) {
      navigate('/');
    }
  }, [username, navigate]);

  const handleCopyCode = () => {
    navigator.clipboard.writeText(roomId);
    setCopySuccess(true);
    soundManager.play('click');
    setTimeout(() => setCopySuccess(false), 2000);
  };

  const handleCopyLink = () => {
    const joinLink = `${window.location.origin}/Duno-room/room/${roomId}`;
    navigator.clipboard.writeText(joinLink);
    setCopyLinkSuccess(true);
    soundManager.play('click');
    setTimeout(() => setCopyLinkSuccess(false), 2000);
  };

  const handleToggleMute = () => {
    const isMuted = soundManager.toggleMute();
    setMuted(isMuted);
  };

  const handleLeave = () => {
    soundManager.play('click');
    leaveGame();
    navigate('/');
  };

  const handleCardClick = (card) => {
    soundManager.play('click');
    if (card.color === 'wild') {
      setWildCardId(card.id);
      setShowColorWheel(true);
    } else {
      playCard(card.id).catch((err) => {
        setError(err.message);
        setTimeout(() => setError(''), 4000);
      });
    }
  };

  const handleSelectColor = (color) => {
    soundManager.play('click');
    setShowColorWheel(false);
    
    if (drawnWildColorSelect) {
      // Resolve playing a drawn wild card
      playDrawnCard(true, color)
        .then(() => {
          setDrawnPlayableCard(null);
          setShowDrawnDecision(false);
          setDrawnWildColorSelect(false);
        })
        .catch((err) => {
          setError(err.message);
          setTimeout(() => setError(''), 4000);
        });
    } else if (wildCardId) {
      // Resolve playing a card from hand
      playCard(wildCardId, color)
        .then(() => setWildCardId(null))
        .catch((err) => {
          setError(err.message);
          setTimeout(() => setError(''), 4000);
        });
    }
  };

  const handleDrawCard = () => {
    if (gameState?.activePlayerName !== username || gameState?.wildAwaitingColor) return;
    
    drawCard()
      .then((playableCard) => {
        if (playableCard) {
          // Player drew a playable card, let them choose to play or keep it
          setDrawnPlayableCard(playableCard);
          setShowDrawnDecision(true);
        }
      })
      .catch((err) => {
        setError(err.message);
        setTimeout(() => setError(''), 4000);
      });
  };

  const handleDrawnDecision = (shouldPlay) => {
    soundManager.play('click');
    if (shouldPlay) {
      if (drawnPlayableCard.color === 'wild') {
        setDrawnWildColorSelect(true);
        setShowColorWheel(true);
      } else {
        playDrawnCard(true)
          .then(() => {
            setDrawnPlayableCard(null);
            setShowDrawnDecision(false);
          })
          .catch((err) => {
            setError(err.message);
            setTimeout(() => setError(''), 4000);
          });
      }
    } else {
      playDrawnCard(false).then(() => {
        setDrawnPlayableCard(null);
        setShowDrawnDecision(false);
      });
    }
  };

  const handleCallUno = () => {
    soundManager.play('click');
    callUno()
      .then(() => {
        soundManager.play('roar');
      })
      .catch((err) => {
        setError(err.message);
        setTimeout(() => setError(''), 4000);
      });
  };

  // Seating configuration helper (circular arrangement)
  const getOrderedPlayers = () => {
    if (!gameState || !gameState.players) return [];
    const players = gameState.players;
    const myIndex = players.findIndex(p => p.username === username);
    if (myIndex === -1) return players;

    const ordered = [];
    for (let i = 0; i < players.length; i++) {
      ordered.push(players[(myIndex + i) % players.length]);
    }
    return ordered;
  };

  const orderedPlayers = getOrderedPlayers();
  const clientPlayer = gameState?.players.find(p => p.username === username);
  const activePlayerIndex = gameState?.currentTurn;
  const isMyTurn = gameState?.activePlayerName === username;

  // Lobby view representation
  if (!gameState || gameState.status === 'waiting') {
    const currentLobby = gameState ? gameState.players : lobbyPlayers;
    const isHost = currentLobby.find(p => p.username === username)?.isHost;
    const allReady = currentLobby.every(p => p.isReady);

    return (
      <div className="min-h-screen animated-bg flex flex-col justify-between p-4 sm:p-6 relative overflow-hidden">
        {/* Glowing Corner Dragons */}
        <CornerDragons />

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

        {/* Header toolbar */}
        <div className="w-full max-w-5xl mx-auto flex items-center justify-between z-10 border-b border-white/5 pb-4">
          <div className="flex items-center gap-2">
            <div className="flex flex-col">
              <span className="text-sm font-black tracking-widest text-slate-100 uppercase">
                DUNO <span className="text-amber-400 font-medium text-[10px] tracking-normal normal-case ml-1.5 hidden sm:inline">dragon clash card game</span>
              </span>
              <span className="text-[8px] text-slate-500 tracking-wider font-bold uppercase mt-[-2px]">
                IndiaDostiChat Arena
              </span>
            </div>
            <span className="px-2 py-0.5 text-[9px] font-bold rounded bg-amber-500/20 border border-amber-500/40 text-amber-300 uppercase tracking-widest">Arena Lobby</span>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handleToggleMute}
              className="p-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-slate-300 transition-all cursor-pointer"
              aria-label="Toggle mute"
            >
              {muted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
            </button>
            <button
              onClick={handleLeave}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-red-500/10 hover:bg-red-500/20 border border-red-500/20 text-xs font-bold uppercase tracking-wider text-red-300 transition-all hover:scale-105 cursor-pointer"
            >
              <LogOut className="w-3.5 h-3.5" />
              Retreat
            </button>
          </div>
        </div>

        {/* Central main lobby card */}
        <main className="w-full max-w-4xl mx-auto my-auto grid grid-cols-1 md:grid-cols-3 gap-6 py-6 z-10">
          <div className="md:col-span-2 glass p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl space-y-6">
            {error && (
              <div className="p-3 rounded-xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs font-bold text-center animate-pulse">
                {error}
              </div>
            )}
            
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-slate-950/40 p-4 rounded-2xl border border-white/5">
              <div>
                <span className="text-[10px] font-black uppercase text-slate-400 tracking-wider">Arena Code</span>
                <h2 className="text-2xl font-black text-white tracking-widest uppercase mt-0.5">{roomId}</h2>
              </div>
              <div className="flex flex-wrap gap-2">
                <button
                  type="button"
                  onClick={handleCopyCode}
                  className="flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 font-extrabold text-xs uppercase tracking-wider text-white transition-all transform active:scale-95 shadow-lg shadow-amber-500/15 cursor-pointer"
                >
                  {copySuccess ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
                  {copySuccess ? 'Copied Code!' : 'Copy Code'}
                </button>
                <button
                  type="button"
                  onClick={handleCopyLink}
                  className="flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-sky-600 hover:bg-sky-500 font-extrabold text-xs uppercase tracking-wider text-white transition-all transform active:scale-95 shadow-lg shadow-sky-500/15 cursor-pointer"
                >
                  {copyLinkSuccess ? <Check className="w-4 h-4" /> : <Link className="w-4 h-4" />}
                  {copyLinkSuccess ? 'Copied Link!' : 'Copy Link'}
                </button>
              </div>
            </div>

            {/* Players slots */}
            <div className="space-y-3">
              <h3 className="text-xs font-extrabold uppercase tracking-widest text-slate-400 flex items-center gap-1.5">
                <Users className="w-4 h-4 text-amber-400" />
                Dragon Warriors ({currentLobby.length} / 8)
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {currentLobby.map((player, idx) => (
                  <div
                    key={idx}
                    className={`flex items-center justify-between p-3.5 rounded-2xl transition-all border ${
                      player.active 
                        ? player.username === username
                          ? 'bg-amber-900/10 border-amber-500/30 text-white'
                          : 'bg-slate-900/40 border-white/5 text-slate-200'
                        : 'bg-slate-900/10 border-white/5 opacity-50 text-slate-400'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <span className="font-extrabold text-sm">{player.username}</span>
                      {player.isHost && (
                        <Shield className="w-3.5 h-3.5 text-amber-400 fill-amber-400/20" title="Arena Host" />
                      )}
                    </div>
                    {player.isReady ? (
                      <span className="px-2 py-0.5 rounded-lg bg-green-500/10 border border-green-500/20 text-[10px] font-extrabold text-emerald-400 uppercase tracking-wider">
                        Ready
                      </span>
                    ) : (
                      <span className="px-2 py-0.5 rounded-lg bg-yellow-500/10 border border-yellow-500/20 text-[10px] font-extrabold text-amber-400 uppercase tracking-wider">
                        Waiting
                      </span>
                    )}
                  </div>
                ))}
              </div>
            </div>

            {/* Ready Actions */}
            <div className="border-t border-white/5 pt-6 flex gap-3">
              <button
                onClick={toggleReady}
                className={`flex-1 font-extrabold py-3.5 px-4 rounded-xl transition-all uppercase tracking-wider text-sm shadow cursor-pointer ${
                  currentLobby.find(p => p.username === username)?.isReady && !isHost
                    ? 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-white/10'
                    : 'bg-emerald-600 hover:bg-emerald-500 text-white'
                }`}
              >
                {currentLobby.find(p => p.username === username)?.isReady && !isHost
                  ? 'Not Ready'
                  : 'Ready to Clash'}
              </button>
              
              {isHost && (
                <button
                  onClick={startGame}
                  disabled={!allReady || currentLobby.length < 2}
                  className="flex-1 glow-btn bg-gradient-to-r from-red-700 via-amber-600 to-yellow-500 disabled:opacity-50 text-white font-extrabold py-3.5 px-4 rounded-xl transition-all uppercase tracking-wider text-sm shadow flex items-center justify-center gap-2 cursor-pointer"
                >
                  <Play className="w-4 h-4 fill-white" />
                  Begin Clash
                </button>
              )}
            </div>
            {!allReady && isHost && (
              <p className="text-[10px] text-center text-slate-500 uppercase tracking-wider">
                Waiting for all warriors to ready up...
              </p>
            )}
            {currentLobby.length < 2 && isHost && (
              <p className="text-[10px] text-center text-amber-400 uppercase tracking-wider">
                Need at least 2 warriors to start the clash.
              </p>
            )}
          </div>

          {/* Lobby chat box */}
          <div className="h-[380px] md:h-auto">
            <Chat messages={chatMessages} onSendMessage={sendChat} currentUsername={username} />
          </div>
        </main>

        <footer className="w-full text-center text-slate-600 text-[10px] uppercase tracking-widest z-10">
          DUNO dragon clash card game &bull; Play responsibly
        </footer>
      </div>
    );
  }

  // ACTIVE BOARD GAME PLAY SCREEN
  const currentColorStyles = {
    red: 'shadow-red-950/30 bg-gradient-to-r from-red-800 to-red-650 text-white',
    blue: 'shadow-blue-950/30 bg-gradient-to-r from-sky-850 to-indigo-900 text-white',
    green: 'shadow-green-950/30 bg-gradient-to-r from-emerald-800 to-emerald-650 text-white',
    yellow: 'shadow-purple-950/30 bg-gradient-to-r from-indigo-950 via-purple-900 to-yellow-600 text-yellow-100',
  };

  const clanNames = {
    red: 'Fire Clan',
    blue: 'Ice Clan',
    green: 'Forest Clan',
    yellow: 'Thunder Clan',
  };

  return (
    <div className="min-h-screen animated-bg text-slate-100 flex flex-col justify-between relative overflow-hidden h-screen select-none">
      {/* Glowing Corner Dragons */}
      <CornerDragons />

      {/* Background Subtle overlays */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(30,27,75,0.4),rgba(2,6,23,0.9))] pointer-events-none"></div>

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

      {/* Main Board Container */}
      <div className="relative flex-1 flex flex-col items-center justify-center p-2 sm:p-4">
        {/* Top Header bar inside game */}
        <div className="absolute top-2 left-2 right-2 flex justify-between items-center z-30">
          <div className="flex items-center gap-2">
            <button
              onClick={handleLeave}
              className="p-1.5 sm:p-2 bg-slate-900/60 hover:bg-red-950/20 border border-white/10 hover:border-red-500/20 text-slate-400 hover:text-red-400 rounded-xl transition-all flex items-center justify-center cursor-pointer"
              title="Retreat from Arena"
            >
              <LogOut className="w-4 h-4" />
            </button>
            <div className="bg-slate-900/80 border border-white/5 px-2.5 py-1 rounded-xl text-[10px] sm:text-xs font-extrabold uppercase text-slate-300">
              Arena: <span className="text-amber-400 tracking-wider">{roomId}</span>
            </div>
          </div>
          
          <div className="flex items-center gap-2">
            <button
              onClick={handleToggleMute}
              className="p-1.5 sm:p-2 rounded-xl bg-slate-900/60 hover:bg-slate-800 border border-white/10 text-slate-300 transition-all cursor-pointer"
            >
              {muted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
            </button>
            <button
              onClick={() => setShowChat(!showChat)}
              className={`p-1.5 sm:p-2 rounded-xl border transition-all flex items-center justify-center relative cursor-pointer ${
                showChat
                  ? 'bg-amber-600 text-white border-amber-600'
                  : 'bg-slate-900/60 border-white/10 text-slate-300'
              }`}
            >
              <MessageCircle className="w-4 h-4" />
              {/* Notification count */}
              {chatMessages.length > 0 && !showChat && (
                <span className="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse"></span>
              )}
            </button>
          </div>
        </div>

        {/* Dynamic circular table seating (Supports up to 8 players) */}
        <div className="relative w-full max-w-lg aspect-square sm:max-w-xl md:max-w-2xl flex items-center justify-center scale-95 sm:scale-100">
          {/* Seating Rings / visual table overlay */}
          <div className="absolute w-[60%] aspect-square rounded-full border border-white/5 bg-[radial-gradient(circle_at_center,rgba(31,41,55,0.1),rgba(15,23,42,0.4))] shadow-[0_0_50px_rgba(0,0,0,0.8)] flex items-center justify-center">
            {/* Center Table Contents */}
            <div className="relative flex flex-col items-center justify-center text-center p-4">
              {/* Current Match Color Outer Glow */}
              <div className={`absolute inset-0 rounded-full blur-2xl opacity-25 ${
                gameState.currentColor === 'red' ? 'bg-red-500' :
                gameState.currentColor === 'blue' ? 'bg-blue-500' :
                gameState.currentColor === 'green' ? 'bg-green-500' : 'bg-purple-600'
              }`}></div>
              
              {/* Discard & Draw piles row */}
              <div className="flex gap-4 items-center z-10">
                {/* DRAW DECK PILE (Spellbook style) */}
                <div
                  onClick={handleDrawCard}
                  className={`
                    w-16 h-24 sm:w-20 sm:h-28 rounded-lg bg-slate-900 border-2 border-amber-600/50 
                    shadow-xl flex items-center justify-center cursor-pointer select-none
                    transform hover:scale-105 active:scale-95 transition-all
                    ${!isMyTurn || gameState.wildAwaitingColor ? 'opacity-70 pointer-events-none brightness-50' : 'hover:border-amber-500'}
                  `}
                  title="Convene Spell (Draw Card)"
                >
                  <div className="w-[85%] h-[85%] rounded bg-gradient-to-br from-slate-950 via-stone-900 to-amber-950 border border-amber-500/20 flex flex-col items-center justify-center rotate-[-12deg] shadow-inner select-none relative overflow-hidden">
                    <div className="absolute w-12 h-12 rounded-full border border-amber-500/10 animate-pulse"></div>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="w-8 h-8 text-amber-500 drop-shadow-md">
                      <path d="M12 2L2 22h20L12 2z" />
                      <circle cx="12" cy="13" r="2.5" fill="currentColor" className="text-amber-600" />
                    </svg>
                    <span className="text-[6.5px] font-black text-amber-400 tracking-wider uppercase mt-1">DUNO</span>
                  </div>
                </div>

                {/* DISCARD PILE (TOP PLAYED CARD) */}
                <div className="relative shadow-2xl select-none">
                  {gameState.topCard ? (
                    <UnoCard key={gameState.topCard.id} card={gameState.topCard} isPlayable={false} size="sm" className="sm:w-20 sm:h-28 animate-deal" />
                  ) : (
                    <div className="w-16 h-24 sm:w-20 sm:h-28 rounded-lg border border-dashed border-white/10 bg-slate-900"></div>
                  )}
                  {/* Current Active clan banner */}
                  <div className={`absolute bottom-[-10px] left-[5%] right-[5%] py-0.5 rounded-full text-[8px] font-black uppercase text-center tracking-widest border border-white/10 ${currentColorStyles[gameState.currentColor]}`}>
                    {clanNames[gameState.currentColor] || gameState.currentColor}
                  </div>
                </div>
              </div>

              {/* Turn indicator and play timer details */}
              <div className="mt-6 flex flex-col items-center justify-center z-10">
                <span className="text-[9px] font-bold uppercase tracking-widest text-slate-400">Current Turn</span>
                <span className={`text-xs sm:text-sm font-black tracking-tight mt-0.5 uppercase ${isMyTurn ? 'text-amber-400' : 'text-slate-200'}`}>
                  {isMyTurn ? 'Your Turn!' : gameState.activePlayerName}
                </span>
                
                {/* Visual Circular Timer */}
                <div className={`mt-2 px-3 py-1 rounded-full text-[10px] font-black tracking-widest border flex items-center gap-1.5 ${
                  gameState.secondsRemaining <= 5 
                    ? 'bg-red-500/20 border-red-500 text-red-450 animate-pulse'
                    : isMyTurn
                      ? 'bg-amber-500/10 border-amber-500 text-amber-400'
                      : 'bg-slate-900 border-white/10 text-slate-400'
                }`}>
                  <RefreshCw className={`w-3.5 h-3.5 ${gameState.direction === 1 ? 'animate-spin-slow' : 'animate-reverse'}`} />
                  {gameState.secondsRemaining}s
                </div>
              </div>
            </div>
          </div>

          {/* Place opponent nodes in clockwise positions */}
          {orderedPlayers.map((player, idx) => {
            const isSelf = player.username === username;
            
            // Generate circular coordinates
            const total = orderedPlayers.length;
            const angle = (idx / total) * 2 * Math.PI + Math.PI / 2; // Start from bottom
            const radius = 40; // Percentage radius
            const left = 50 + radius * Math.cos(angle);
            const top = 50 + radius * Math.sin(angle);

            // Turn detection
            const activePlayer = gameState.players[activePlayerIndex];
            const isPlayerTurn = activePlayer && activePlayer.username === player.username;

            return (
              <div
                key={idx}
                className="absolute transform -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-20 transition-all duration-500"
                style={{ left: `${left}%`, top: `${top}%` }}
              >
                {/* Seating User profile bubble */}
                <div
                  className={`
                    w-12 h-12 sm:w-14 sm:h-14 rounded-full flex flex-col items-center justify-center border-2 shadow-lg transition-all
                    ${
                      isPlayerTurn
                        ? 'bg-slate-900 border-amber-400 shadow-amber-400/20 scale-110'
                        : 'bg-slate-900/90 border-white/10'
                    }
                    ${!player.active ? 'opacity-40 filter grayscale' : ''}
                  `}
                >
                  {/* Avatar Character initials */}
                  <span className="font-extrabold text-xs text-slate-300">
                    {player.username.substring(0, 2).toUpperCase()}
                  </span>
                  
                  {/* Card count tag badge */}
                  <div className="absolute -bottom-1 right-[-4px] bg-indigo-600 border border-white/20 px-1.5 py-0.5 rounded-md text-[8px] font-black text-white leading-none shadow">
                    {player.cardsCount}
                  </div>
                </div>

                {/* Nickname and status */}
                <div className="mt-1.5 flex flex-col items-center text-center">
                  <span className={`text-[10px] font-black tracking-tight max-w-[80px] truncate ${
                    isSelf ? 'text-cyan-400 font-black' : isPlayerTurn ? 'text-amber-400 font-bold' : 'text-slate-300'
                  }`}>
                    {isSelf ? 'YOU' : player.username}
                  </span>
                  {!player.active && (
                    <span className="text-[7px] font-extrabold text-red-400 uppercase tracking-widest leading-none">
                      Fled
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Floating drawn card choice modal overlay */}
      {showDrawnDecision && drawnPlayableCard && (
        <div className="fixed inset-0 z-40 flex items-center justify-center bg-slate-950/80 backdrop-blur-md">
          <div className="glass p-6 sm:p-8 rounded-3xl max-w-sm w-full mx-4 text-center border border-white/10 shadow-2xl animate-scaleUp">
            <h3 className="text-xl font-black mb-1 uppercase tracking-wider text-slate-200">PLAY OR KEEP?</h3>
            <p className="text-xs text-slate-400 mb-6">You drew a playable spell card!</p>
            
            <div className="flex justify-center mb-6">
              <UnoCard card={drawnPlayableCard} isPlayable={false} size="md" />
            </div>

            <div className="flex gap-4">
              <button
                onClick={() => handleDrawnDecision(true)}
                className="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold py-3 px-4 rounded-xl transition-all uppercase tracking-wider text-xs shadow cursor-pointer"
              >
                Cast Spell
              </button>
              <button
                onClick={() => handleDrawnDecision(false)}
                className="flex-1 bg-slate-800 hover:bg-slate-700 text-slate-300 border border-white/10 font-extrabold py-3 px-4 rounded-xl transition-all uppercase tracking-wider text-xs shadow cursor-pointer"
              >
                Keep Card
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Color Select Modal Overlay */}
      <ColorWheel isOpen={showColorWheel} onSelect={handleSelectColor} />

      {/* Game Completed Win Screen Modal */}
      {gameState?.status === 'ended' && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/90 backdrop-blur-lg">
          <div className="glass p-8 rounded-3xl max-w-md w-full mx-4 text-center border border-white/10 shadow-2xl animate-scaleUp space-y-6">
            <div>
              <span className="text-[10px] font-black uppercase text-amber-400 tracking-widest">Victory Board</span>
              <h2 className="text-3xl font-black text-white tracking-tight uppercase mt-1">ROUND ENDED</h2>
            </div>

            {/* List game final player scores */}
            <div className="bg-slate-900/60 rounded-2xl border border-white/5 divide-y divide-white/5 overflow-hidden">
              {gameState.players.map((p, idx) => (
                <div key={idx} className="flex justify-between items-center p-3.5 text-sm">
                  <span className="font-extrabold text-slate-200">{p.username}</span>
                  <div className="flex items-center gap-3">
                    <span className="text-xs text-slate-500 uppercase font-bold tracking-widest">{p.cardsCount} cards</span>
                    <span className={`font-black text-xs uppercase tracking-wider ${p.cardsCount === 0 ? 'text-emerald-400' : 'text-slate-405'}`}>
                      {p.cardsCount === 0 ? 'VICTORIOUS' : 'DEFEATED'}
                    </span>
                  </div>
                </div>
              ))}
            </div>

            <div className="border-t border-white/5 pt-6">
              <button
                onClick={handleLeave}
                className="w-full glow-btn bg-gradient-to-r from-red-700 via-amber-600 to-indigo-850 text-white font-extrabold py-3 px-4 rounded-xl transition-all uppercase tracking-wider text-xs shadow-lg shadow-amber-500/20 cursor-pointer"
              >
                Return to Lobby
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Bottom User UI Controls Panel */}
      <div className="relative bg-slate-900/80 backdrop-blur-md border-t border-white/5 p-3 sm:p-5 flex flex-col gap-3 z-30 shadow-[0_-10px_30px_rgba(0,0,0,0.5)]">
        {/* Error Notification banner */}
        {error && (
          <div className="absolute top-[-36px] left-[5%] right-[5%] mx-auto max-w-sm p-1.5 rounded-lg bg-red-500/20 border border-red-500/40 text-red-200 text-[10px] font-extrabold text-center uppercase tracking-widest animate-pulse">
            {error}
          </div>
        )}

        {/* Hand headers row: controls for UNO alert buzzer */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-1">
            <span className="text-[10px] font-black uppercase text-slate-400 tracking-wider">Your Hand</span>
            <span className="px-1.5 py-0.5 text-[8px] font-bold rounded bg-slate-800 text-slate-300">
              {clientPlayer?.cards.length || 0}
            </span>
          </div>

          {/* ROAR BUZZER BUTTON */}
          <button
            onClick={handleCallUno}
            disabled={!clientPlayer || clientPlayer.cards.length > 2}
            className={`
              px-6 py-2 rounded-full font-black text-xs uppercase tracking-widest transition-all duration-300 cursor-pointer
              ${
                clientPlayer && clientPlayer.cards.length <= 2
                  ? 'bg-gradient-to-r from-red-700 via-amber-600 to-yellow-500 text-white border-2 border-amber-400 animate-pulse hover:shadow-amber-500/35 hover:scale-105 active:scale-95'
                  : 'bg-slate-800 border border-white/5 text-slate-505 cursor-not-allowed'
              }
            `}
          >
            🔥 ROAR! 🔥
          </button>
        </div>

        {/* Scrollable Player hand cards row */}
        <div className="w-full overflow-x-auto scrollbar-none py-4">
          <div className="flex gap-2 sm:gap-3 px-2 min-w-max justify-center items-end h-44 sm:h-48">
            {clientPlayer?.cards.map((card, index) => {
              const playable = isMyTurn && !gameState.wildAwaitingColor && (
                gameState.topCard === null || 
                card.color === 'wild' || 
                card.color === gameState.currentColor || 
                card.value === gameState.topCard.value
              );

              return (
                <div 
                  key={card.id} 
                  className="first:ml-0 transform transition-all duration-300 animate-deal"
                  style={{ animationDelay: `${index * 80}ms` }}
                >
                  <UnoCard
                     card={card}
                     onClick={() => handleCardClick(card)}
                     isPlayable={playable}
                     size="md"
                  />
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Floating Side Drawer Chat Overlay (For mobile/split views) */}
      {showChat && (
        <div className="fixed inset-y-0 right-0 w-80 max-w-full z-40 p-4 pt-16 bg-slate-950/80 backdrop-blur-md shadow-2xl animate-slideLeft">
          <Chat messages={chatMessages} onSendMessage={sendChat} currentUsername={username} />
        </div>
      )}
    </div>
  );
};

export default GameRoom;
