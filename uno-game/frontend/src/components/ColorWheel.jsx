import React from 'react';

const ColorWheel = ({ onSelect, isOpen }) => {
  if (!isOpen) return null;

  const clans = [
    { id: 'red', name: 'Fire Clan', bg: 'bg-gradient-to-br from-red-700 to-red-900 border-red-500 hover:from-red-600 hover:to-red-800 text-red-100', border: 'border-red-400/50' },
    { id: 'blue', name: 'Ice Clan', bg: 'bg-gradient-to-br from-sky-600 to-blue-800 border-sky-500 hover:from-sky-500 hover:to-blue-750 text-sky-100', border: 'border-sky-400/50' },
    { id: 'green', name: 'Forest Clan', bg: 'bg-gradient-to-br from-emerald-700 to-green-900 border-emerald-500 hover:from-emerald-600 hover:to-green-800 text-emerald-100', border: 'border-emerald-400/50' },
    { id: 'yellow', name: 'Thunder Clan', bg: 'bg-gradient-to-br from-purple-800 via-purple-900 to-yellow-600 border-yellow-400 hover:from-purple-700 hover:to-yellow-500 text-yellow-100', border: 'border-yellow-350/50' }
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/85 backdrop-blur-md transition-opacity duration-300 animate-fadeIn">
      <div className="glass p-8 rounded-3xl max-w-sm w-full mx-4 text-center border border-white/10 shadow-2xl scale-up">
        <h3 className="text-2xl font-black mb-1 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 via-emerald-400 to-blue-500 tracking-wide">
          SUMMON DRAGON CLAN
        </h3>
        <p className="text-slate-355 text-sm mb-6">Choose the next dragon clan to rule the arena</p>
        
        {/* Clans Grid */}
        <div className="relative w-64 h-64 mx-auto grid grid-cols-2 gap-3 transform hover:rotate-6 transition-transform duration-500">
          {clans.map((clan) => (
            <button
              key={clan.id}
              onClick={() => onSelect(clan.id)}
              className={`
                w-full h-full rounded-2xl ${clan.bg} border ${clan.border}
                shadow-lg hover:shadow-2xl transition-all duration-300 
                flex items-center justify-center font-black text-xs uppercase tracking-wider
                transform hover:scale-105 active:scale-95 cursor-pointer p-2
              `}
              aria-label={`Select ${clan.name}`}
            >
              <span className="drop-shadow-lg text-center leading-tight">{clan.name}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ColorWheel;
