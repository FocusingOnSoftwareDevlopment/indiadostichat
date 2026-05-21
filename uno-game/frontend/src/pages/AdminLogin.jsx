import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Shield, ArrowLeft, Loader2 } from 'lucide-react';
import soundManager from '../utils/SoundManager';

const AdminLogin = () => {
  const navigate = useNavigate();
  const [password, setPassword] = useState('');
  const [username] = useState('Heisenberg');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Resolve API URL dynamically
  const apiUrl = import.meta.env.VITE_API_URL || 
    (window.location.hostname === 'localhost' ? 'http://localhost:5000' : window.location.origin);

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    soundManager.play('click');

    try {
      const response = await fetch(`${apiUrl}/api/admin/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || 'Login failed.');
      }

      localStorage.setItem('dosti_admin_token', data.token);
      localStorage.setItem('dosti_admin_user', data.username);
      navigate('/admin/dashboard');
    } catch (err) {
      setError(err.message || 'Server error.');
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    soundManager.play('click');
    navigate('/');
  };

  return (
    <div className="min-h-screen animated-bg flex flex-col justify-between p-4 sm:p-6 relative overflow-hidden">
      {/* Background Decor */}
      <div className="absolute top-[-10%] right-[-5%] w-96 h-96 rounded-full bg-slate-800/10 blur-[120px] pointer-events-none"></div>

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
          <Shield className="w-4 h-4 text-slate-400" />
          <span className="text-sm font-black tracking-widest text-slate-300">DOSTI <span className="text-unoyellow">CARDS</span></span>
        </div>
      </header>

      {/* Main card box */}
      <main className="w-full max-w-md mx-auto my-auto py-8 z-10">
        <div className="glass p-8 rounded-3xl border border-white/10 shadow-2xl relative">
          <div className="absolute top-[-5px] left-[10%] right-[10%] h-[3px] bg-slate-600 rounded-full"></div>
          
          <div className="text-center mb-8">
            <h1 className="text-2xl font-black text-white tracking-tight uppercase">Admin Terminal</h1>
            <p className="text-slate-400 text-xs mt-1">Authorized Heisenberg personnel only</p>
          </div>

          {error && (
            <div className="mb-6 p-3 rounded-xl bg-red-500/10 border border-red-500/20 text-red-200 text-xs text-center font-bold">
              {error}
            </div>
          )}

          <form onSubmit={handleLogin} className="space-y-6">
            <div>
              <label className="block text-[10px] font-extrabold uppercase tracking-widest text-slate-400 mb-2">
                Admin Username
              </label>
              <input
                type="text"
                value={username}
                disabled
                className="w-full bg-slate-950/60 border border-white/5 rounded-xl px-4 py-3 text-slate-400 cursor-not-allowed select-none font-bold"
              />
            </div>

            <div>
              <label className="block text-[10px] font-extrabold uppercase tracking-widest text-slate-400 mb-2">
                Secret Password Key
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••••••"
                required
                className="w-full bg-slate-950/60 border border-white/10 rounded-xl px-4 py-3 text-white placeholder-slate-600 focus:outline-none focus:border-slate-500 transition-colors shadow-inner"
              />
            </div>

            <button
              type="submit"
              disabled={loading || !password.trim()}
              className="w-full glow-btn bg-slate-800 hover:bg-slate-700 disabled:opacity-50 text-white font-extrabold py-3.5 px-4 rounded-xl shadow-lg border border-white/10 hover:translate-y-[-2px] transition-all flex items-center justify-center gap-2"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin text-unoblue" />
                  AUTHENTICATING...
                </>
              ) : (
                'ENTER TERMINAL'
              )}
            </button>
          </form>
        </div>
      </main>

      <footer className="w-full text-center text-slate-600 text-[10px] uppercase tracking-widest z-10 pt-4">
        Security Level: Alpha &bull; Encrypted Session
      </footer>
    </div>
  );
};

export default AdminLogin;
