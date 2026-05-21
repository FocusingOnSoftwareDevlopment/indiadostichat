import React from 'react';
import { RotateCw, Ban, Disc } from 'lucide-react';

const UnoCard = ({ card, onClick, isPlayable = true, size = 'md', className = '' }) => {
  if (!card) return null;

  const { color, value } = card;

  // Background and border styling mapping
  const bgStyles = {
    red: 'bg-unocardred border-red-300 shadow-red-500/20 text-white',
    blue: 'bg-unocardblue border-blue-300 shadow-blue-500/20 text-white',
    green: 'bg-unocardgreen border-green-300 shadow-green-500/20 text-white',
    yellow: 'bg-unocardyellow border-yellow-300 shadow-yellow-500/20 text-slate-900',
    wild: 'bg-slate-900 border-slate-700 shadow-slate-900/30 text-white',
  };

  const borderStyles = {
    red: 'border-red-600',
    blue: 'border-blue-600',
    green: 'border-green-600',
    yellow: 'border-yellow-500',
    wild: 'border-slate-800',
  };

  const getCardIcon = () => {
    switch (value) {
      case 'skip':
        return <Ban className="w-8 h-8 sm:w-10 sm:h-10" />;
      case 'reverse':
        return <RotateCw className="w-8 h-8 sm:w-10 sm:h-10" />;
      case 'draw2':
        return <span className="font-extrabold text-2xl sm:text-3xl">+2</span>;
      case 'wild':
        return (
          <div className="relative w-10 h-10 flex items-center justify-center">
            {/* Quadrant color ring */}
            <div className="absolute inset-0 rounded-full border-4 border-t-red-500 border-r-blue-500 border-b-yellow-500 border-l-green-500 animate-spin-slow"></div>
            <span className="text-[10px] font-black uppercase tracking-tighter">Wild</span>
          </div>
        );
      case 'wild4':
        return (
          <div className="relative w-10 h-10 flex items-center justify-center">
            {/* Quadrant color ring */}
            <div className="absolute inset-0 rounded-full border-4 border-t-red-500 border-r-blue-500 border-b-yellow-500 border-l-green-500 animate-spin-slow"></div>
            <span className="font-black text-xl sm:text-2xl z-10 text-white drop-shadow">+4</span>
          </div>
        );
      default:
        return <span className="font-black text-3xl sm:text-4xl italic tracking-tighter">{value}</span>;
    }
  };

  const sizeClasses = {
    sm: 'w-16 h-24 text-sm rounded-lg border-2',
    md: 'w-24 h-36 sm:w-28 sm:h-40 rounded-xl border-4 shadow-lg',
    lg: 'w-32 h-48 sm:w-36 sm:h-54 rounded-2xl border-4 shadow-xl',
  };

  // Rendering Wild overlay background card inside the card itself
  const renderCardBody = () => {
    if (color === 'wild') {
      return (
        <div className="absolute inset-0 flex items-center justify-center overflow-hidden rounded-lg">
          {/* Diagnostic split background */}
          <div className="absolute w-[200%] h-[200%] rotate-45 grid grid-cols-2 grid-rows-2">
            <div className="bg-red-500 opacity-90"></div>
            <div className="bg-blue-500 opacity-90"></div>
            <div className="bg-green-500 opacity-90"></div>
            <div className="bg-yellow-400 opacity-90"></div>
          </div>
          {/* Inner circle badge */}
          <div className="absolute w-[75%] h-[75%] rounded-full bg-slate-900 border border-slate-700 flex items-center justify-center shadow-inner z-10">
            {getCardIcon()}
          </div>
        </div>
      );
    }

    return (
      <div className="relative w-full h-full flex flex-col justify-between p-2 sm:p-3 overflow-hidden select-none">
        {/* Top-Left Index */}
        <div className="flex justify-start">
          <span className="font-black text-base sm:text-lg italic leading-none">{value === 'draw2' ? '+2' : value === 'skip' ? 'Ø' : value === 'reverse' ? '⇆' : value}</span>
        </div>

        {/* Center Symbol */}
        <div className="flex-1 flex items-center justify-center">
          {/* Oval white badge for numbers/symbols */}
          <div className={`w-[75%] h-[70%] rounded-[50%] rotate-[-25deg] bg-white/10 border border-white/20 flex items-center justify-center shadow-inner`}>
            <div className="rotate-[25deg] flex items-center justify-center text-inherit">
              {getCardIcon()}
            </div>
          </div>
        </div>

        {/* Bottom-Right Index */}
        <div className="flex justify-end rotate-180">
          <span className="font-black text-base sm:text-lg italic leading-none">{value === 'draw2' ? '+2' : value === 'skip' ? 'Ø' : value === 'reverse' ? '⇆' : value}</span>
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
        ${isPlayable && onClick ? 'cursor-pointer hover:-translate-y-6 hover:shadow-2xl hover:scale-105 active:scale-95' : 'cursor-not-allowed'}
        ${!isPlayable ? 'brightness-50 filter saturate-50 border-slate-600' : ''}
        ${className}
      `}
    >
      {renderCardBody()}
      {/* Light glow shimmer effect */}
      <div className="absolute inset-0 rounded-lg pointer-events-none bg-gradient-to-tr from-transparent via-white/10 to-transparent"></div>
    </div>
  );
};

export default UnoCard;
