import React from 'react';

const ColorWheel = ({ onSelect, isOpen }) => {
  if (!isOpen) return null;

  const colors = [
    { id: 'red', name: 'Red', bg: 'bg-red-500 hover:bg-red-400 active:bg-red-600', border: 'border-red-600' },
    { id: 'yellow', name: 'Yellow', bg: 'bg-yellow-400 hover:bg-yellow-300 active:bg-yellow-500', border: 'border-yellow-500' },
    { id: 'green', name: 'Green', bg: 'bg-green-500 hover:bg-green-400 active:bg-green-600', border: 'border-green-600' },
    { id: 'blue', name: 'Blue', bg: 'bg-blue-500 hover:bg-blue-400 active:bg-blue-600', border: 'border-blue-600' }
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-md transition-opacity duration-300 animate-fadeIn">
      <div className="glass p-8 rounded-3xl max-w-sm w-full mx-4 text-center border border-white/10 shadow-2xl scale-up">
        <h3 className="text-2xl font-black mb-1 text-transparent bg-clip-text bg-gradient-to-r from-unored via-unoyellow to-unoblue tracking-wide">
          CHOOSE COLOR
        </h3>
        <p className="text-slate-300 text-sm mb-6">Select the next play color for the table</p>
        
        {/* Color Wheel Grid/Circle */}
        <div className="relative w-64 h-64 mx-auto grid grid-cols-2 gap-3 transform hover:rotate-12 transition-transform duration-500">
          {colors.map((color, index) => (
            <button
              key={color.id}
              onClick={() => onSelect(color.id)}
              className={`
                w-full h-full rounded-2xl ${color.bg} border-2 ${color.border}
                shadow-lg hover:shadow-2xl transition-all duration-300 
                flex items-center justify-center font-black text-white text-lg uppercase tracking-wider
                transform hover:scale-105 active:scale-95
              `}
              aria-label={`Select ${color.name}`}
            >
              <span className="drop-shadow-md">{color.name}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ColorWheel;
