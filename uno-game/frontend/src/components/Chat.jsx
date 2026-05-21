import React, { useState, useEffect, useRef } from 'react';
import { Send, MessageSquare } from 'lucide-react';

const Chat = ({ messages, onSendMessage, currentUsername }) => {
  const [inputText, setInputText] = useState('');
  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputText.trim()) {
      onSendMessage(inputText);
      setInputText('');
    }
  };

  return (
    <div className="flex flex-col h-full bg-slate-950/40 backdrop-blur border border-white/10 rounded-2xl overflow-hidden shadow-xl">
      {/* Header */}
      <div className="px-4 py-3 bg-white/5 border-b border-white/10 flex items-center gap-2">
        <MessageSquare className="w-5 h-5 text-unoblue" />
        <span className="font-extrabold text-sm uppercase tracking-wider text-slate-200">Room Chat</span>
      </div>

      {/* Messages list */}
      <div className="flex-1 p-4 overflow-y-auto space-y-3 min-h-[180px] scrollbar-none">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-slate-500 text-center p-4">
            <MessageSquare className="w-8 h-8 opacity-20 mb-2" />
            <p className="text-xs">No messages yet. Send one to start the conversation!</p>
          </div>
        ) : (
          messages.map((msg, idx) => {
            const isMe = msg.username === currentUsername;
            return (
              <div
                key={idx}
                className={`flex flex-col max-w-[85%] ${
                  isMe ? 'ml-auto items-end' : 'mr-auto items-start'
                }`}
              >
                {/* Username */}
                {!isMe && (
                  <span className="text-[10px] font-bold text-slate-400 mb-1 px-1">
                    {msg.username}
                  </span>
                )}
                {/* Text Bubble */}
                <div
                  className={`px-3 py-2 rounded-2xl text-sm break-all shadow ${
                    isMe
                      ? 'bg-gradient-to-br from-blue-600 to-indigo-700 text-white rounded-tr-none'
                      : 'bg-slate-800 text-slate-100 rounded-tl-none border border-slate-700'
                  }`}
                >
                  {msg.text}
                </div>
                {/* Time */}
                <span className="text-[9px] text-slate-500 mt-1 px-1">{msg.time}</span>
              </div>
            );
          })
        )}
        <div ref={chatEndRef} />
      </div>

      {/* Input controls form */}
      <form onSubmit={handleSubmit} className="p-3 bg-white/5 border-t border-white/10 flex gap-2">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Say something..."
          maxLength={100}
          className="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white focus:outline-none focus:border-unoblue transition-colors"
        />
        <button
          type="submit"
          disabled={!inputText.trim()}
          className="bg-unoblue hover:bg-blue-600 disabled:opacity-50 text-white p-2 rounded-xl transition-all flex items-center justify-center"
          aria-label="Send message"
        >
          <Send className="w-4 h-4" />
        </button>
      </form>
    </div>
  );
};

export default Chat;
