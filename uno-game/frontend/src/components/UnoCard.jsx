import React from 'react';
import { RotateCw, Snowflake, Flame, Leaf, Zap } from 'lucide-react';

// Custom card sub-components for special assets
const FreezeIcon = ({ className = "w-8 h-8" }) => (
  <div className="relative flex items-center justify-center">
    <Snowflake className={`${className} text-cyan-200 animate-pulse`} />
    <span className="absolute text-[7px] font-black text-cyan-900 bg-cyan-200/90 rounded px-0.5 select-none bottom-[-8px] tracking-tighter">FREEZE</span>
  </div>
);

const TurnIcon = ({ className = "w-8 h-8" }) => (
  <div className="relative flex items-center justify-center">
    <RotateCw className={`${className} text-indigo-200 animate-spin-slow`} />
    <span className="absolute text-[7px] font-black text-indigo-900 bg-indigo-200/90 rounded px-0.5 select-none bottom-[-8px] tracking-tighter">TURN</span>
  </div>
);

const BiteIcon = ({ className = "w-8 h-8" }) => (
  <div className="relative flex flex-col items-center justify-center">
    <span className="text-xl sm:text-2xl font-black italic tracking-tighter text-red-100 leading-none">+2</span>
    <span className="text-[7px] font-black text-red-950 bg-red-200/90 rounded px-0.5 select-none mt-1 tracking-tighter">BITE</span>
  </div>
);

const ElderDragonIcon = ({ className = "w-9 h-9" }) => (
  <div className="relative flex flex-col items-center justify-center">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={`${className} text-amber-300 animate-pulse`}>
      <path d="M12 2L2 22h20L12 2z" />
      <circle cx="12" cy="13" r="3" fill="currentColor" className="text-amber-500" />
      <path d="M12 10v6" stroke="#000" strokeWidth="1.5" />
    </svg>
    <span className="absolute text-[7px] font-black text-amber-950 bg-amber-300 rounded px-0.5 select-none bottom-[-11px] tracking-tighter">ELDER</span>
  </div>
);

const ChaosDragonIcon = ({ className = "w-9 h-9" }) => (
  <div className="relative flex flex-col items-center justify-center">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={`${className} text-purple-400 animate-pulse`}>
      <path d="M4.5 16.5c-1.5 1.26-2.5 3.19-2.5 5.5h20c0-2.31-1-4.24-2.5-5.5M12 2C6.48 2 2 6.48 2 12c0 1.5.35 2.9 1 4.17l9-8.17 9 8.17c.65-1.27 1-2.67 1-4.17 0-5.52-4.48-10-10-10z" />
      <circle cx="12" cy="12" r="2" fill="currentColor" className="text-red-500 animate-ping" />
    </svg>
    <span className="absolute text-[7px] font-black text-purple-100 bg-purple-900 border border-purple-500 rounded px-0.5 select-none bottom-[-11px] tracking-tighter">CHAOS +4</span>
  </div>
);

const UnoCard = ({ card, onClick, isPlayable = true, size = 'md', className = '' }) => {
  if (!card) return null;

  const { color, value } = card;

  // Clan background styling using vibrant, high-contrast gradients and custom glows
  const bgStyles = {
    red: 'bg-gradient-to-br from-orange-500 via-red-600 to-red-800 border-orange-400/90 shadow-[0_0_15px_rgba(239,68,68,0.5)] text-red-50',
    blue: 'bg-gradient-to-br from-cyan-400 via-sky-500 to-blue-755 border-cyan-350/90 shadow-[0_0_15px_rgba(56,189,248,0.5)] text-sky-50',
    green: 'bg-gradient-to-br from-lime-450 via-emerald-500 to-green-700 border-lime-350/90 shadow-[0_0_15px_rgba(34,197,94,0.5)] text-emerald-50',
    yellow: 'bg-gradient-to-br from-yellow-300 via-amber-400 to-yellow-500 border-yellow-200/90 shadow-[0_0_15px_rgba(234,179,8,0.5)] text-yellow-50',
    wild: 'bg-gradient-to-br from-slate-800 via-amber-900 to-slate-950 border-amber-500/90 shadow-[0_0_15px_rgba(245,158,11,0.5)] text-amber-50',
  };

  const getCardIcon = () => {
    switch (value) {
      case 'skip':
        return <FreezeIcon className="w-8 h-8 sm:w-10 sm:h-10" />;
      case 'reverse':
        return <TurnIcon className="w-8 h-8 sm:w-10 sm:h-10" />;
      case 'draw2':
        return <BiteIcon className="w-8 h-8 sm:w-10 sm:h-10" />;
      case 'wild':
        return <ElderDragonIcon className="w-9 h-9 sm:w-10 sm:h-10" />;
      case 'wild4':
        return <ChaosDragonIcon className="w-9 h-9 sm:w-10 sm:h-10" />;
      default:
        return (
          <div className="relative flex items-center justify-center">
            <span className="font-black text-3xl sm:text-4xl italic tracking-tighter text-slate-100 drop-shadow-md select-none">{value}</span>
          </div>
        );
    }
  };

  const getCornerLabel = () => {
    switch (value) {
      case 'skip':
        return <Snowflake className="w-3 h-3 text-cyan-300" />;
      case 'reverse':
        return <RotateCw className="w-3 h-3 text-indigo-300" />;
      case 'draw2':
        return <span className="font-black text-xs text-red-200">+2</span>;
      case 'wild':
        return <span className="font-black text-[9px] text-amber-300">W</span>;
      case 'wild4':
        return <span className="font-black text-[9px] text-purple-300">+4</span>;
      default:
        return <span className="font-black text-xs sm:text-sm">{value}</span>;
    }
  };

  const getClanEmblem = () => {
    switch (color) {
      case 'red':
        return <Flame className="w-3 h-3 text-red-400" />;
      case 'blue':
        return <Snowflake className="w-3 h-3 text-cyan-400" />;
      case 'green':
        return <Leaf className="w-3 h-3 text-emerald-400" />;
      case 'yellow':
        return <Zap className="w-3 h-3 text-yellow-400" />;
      default:
        return null;
    }
  };

  const sizeClasses = {
    sm: 'w-16 h-24 text-xs rounded-lg border shadow-sm',
    md: 'w-24 h-36 sm:w-28 sm:h-40 rounded-xl border-2 shadow-lg',
    lg: 'w-32 h-48 sm:w-36 sm:h-54 rounded-2xl border-4 shadow-xl',
  };

  const renderCardBody = () => {
    if (color === 'wild') {
      return (
        <div className="absolute inset-0 flex items-center justify-center overflow-hidden rounded-lg sm:rounded-xl">
          {/* Swirling chaos color quadrants */}
          <div className="absolute w-[200%] h-[200%] rotate-45 grid grid-cols-2 grid-rows-2 animate-spin-slow opacity-50">
            <div className="bg-red-900"></div>
            <div className="bg-blue-900"></div>
            <div className="bg-emerald-900"></div>
            <div className="bg-yellow-800"></div>
          </div>
          {/* Outer magical border */}
          <div className="absolute w-[80%] h-[80%] rounded-full border border-dashed border-amber-500/30 animate-spin-reverse-slow"></div>
          {/* Center dark lens */}
          <div className="absolute w-[70%] h-[70%] rounded-full bg-slate-950/90 border border-amber-500/50 flex items-center justify-center shadow-inner z-10">
            {getCardIcon()}
          </div>
        </div>
      );
    }

    return (
      <div className="relative w-full h-full flex flex-col justify-between p-1.5 sm:p-2.5 overflow-hidden select-none">
        {/* Top Corner Details */}
        <div className="flex justify-between items-center">
          {getCornerLabel()}
          {getClanEmblem()}
        </div>

        {/* Center Emblem/Number */}
        <div className="flex-1 flex items-center justify-center relative">
          {/* Magical Runic Ring */}
          <div className="absolute w-[82%] h-[82%] rounded-full border border-dashed border-white/10 animate-spin-slow"></div>
          
          <div className={`w-[72%] h-[72%] rounded-full bg-slate-950/30 border border-white/5 flex items-center justify-center shadow-inner`}>
            <div className="flex items-center justify-center text-inherit">
              {getCardIcon()}
            </div>
          </div>
        </div>

        {/* Bottom Corner Details (Inverted) */}
        <div className="flex justify-between items-center rotate-180">
          {getCornerLabel()}
          {getClanEmblem()}
        </div>
      </div>
    );
  };

  return (
    <div
      onClick={isPlayable && onClick ? onClick : undefined}
      className={`
        relative 
        ${sizeClasses[size]} 
        ${bgStyles[color] || bgStyles.wild} 
        transition-all duration-300
        ${isPlayable && onClick ? 'cursor-pointer hover:-translate-y-5 hover:shadow-2xl hover:scale-105 active:scale-95' : 'cursor-not-allowed'}
        ${!isPlayable ? 'brightness-[95%] saturate-[100%] border-slate-700/40 shadow-sm' : ''}
        ${className}
      `}
    >
      {renderCardBody()}
      {/* Light shimmer overlay */}
      <div className="absolute inset-0 rounded-lg sm:rounded-xl pointer-events-none bg-gradient-to-tr from-transparent via-white/5 to-transparent"></div>
    </div>
  );
};

export default UnoCard;
