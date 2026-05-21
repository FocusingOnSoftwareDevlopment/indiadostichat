class SoundManager {
  constructor() {
    this.ctx = null;
    this.muted = false;
  }

  init() {
    if (!this.ctx) {
      this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggleMute() {
    this.muted = !this.muted;
    // Attempt init on user interaction to bypass browser audio policies
    this.init();
    return this.muted;
  }

  isMuted() {
    return this.muted;
  }

  play(type) {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    try {
      switch (type) {
        case 'click':
          this.playClick();
          break;
        case 'play':
          this.playCardPlay();
          break;
        case 'draw':
          this.playCardDraw();
          break;
        case 'wild':
          this.playWildCard();
          break;
        case 'win':
          this.playWin();
          break;
        case 'error':
          this.playError();
          break;
        case 'deal':
          this.playDeal();
          break;
        case 'warning':
        case 'roar':
          this.playRoar();
          break;
        default:
          break;
      }
    } catch (e) {
      console.warn("Web Audio API error:", e);
    }
  }

  playClick() {
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.type = 'sine';
    osc.frequency.setValueAtTime(600, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(100, this.ctx.currentTime + 0.1);

    gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.1);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.1);
  }

  playCardPlay() {
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(300, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(500, this.ctx.currentTime + 0.15);

    gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.15);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.15);
  }

  playCardDraw() {
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.type = 'sine';
    osc.frequency.setValueAtTime(200, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(400, this.ctx.currentTime + 0.25);

    gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.25);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.25);
  }

  playWildCard() {
    const time = this.ctx.currentTime;
    const osc1 = this.ctx.createOscillator();
    const osc2 = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(this.ctx.destination);

    osc1.type = 'triangle';
    osc2.type = 'sawtooth';

    osc1.frequency.setValueAtTime(440, time);
    osc1.frequency.linearRampToValueAtTime(880, time + 0.4);

    osc2.frequency.setValueAtTime(220, time);
    osc2.frequency.linearRampToValueAtTime(660, time + 0.4);

    gain.gain.setValueAtTime(0.1, time);
    gain.gain.exponentialRampToValueAtTime(0.01, time + 0.4);

    osc1.start();
    osc2.start();
    osc1.stop(time + 0.4);
    osc2.stop(time + 0.4);
  }

  playDeal() {
    const time = this.ctx.currentTime;
    for (let i = 0; i < 4; i++) {
      const startTime = time + i * 0.08;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.type = 'sine';
      osc.frequency.setValueAtTime(523.25, startTime); // C5
      gain.gain.setValueAtTime(0.1, startTime);
      gain.gain.exponentialRampToValueAtTime(0.01, startTime + 0.06);

      osc.start(startTime);
      osc.stop(startTime + 0.06);
    }
  }

  playRoar() {
    const time = this.ctx.currentTime;
    
    // Create multiple low frequency sawtooth/triangle oscillators for a thick, detuned growl
    const osc1 = this.ctx.createOscillator();
    const osc2 = this.ctx.createOscillator();
    const noise = this.ctx.createOscillator();
    
    // Low pass filter to remove high harshness and keep it rumbling/heavy
    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(150, time);
    filter.frequency.exponentialRampToValueAtTime(60, time + 0.8);
    
    const gain = this.ctx.createGain();
    
    osc1.connect(filter);
    osc2.connect(filter);
    noise.connect(filter);
    filter.connect(gain);
    gain.connect(this.ctx.destination);
    
    osc1.type = 'sawtooth';
    osc1.frequency.setValueAtTime(95, time); // Detuned low freq
    osc1.frequency.linearRampToValueAtTime(45, time + 0.8);
    
    osc2.type = 'sawtooth';
    osc2.frequency.setValueAtTime(92, time); // Slighly detuned
    osc2.frequency.linearRampToValueAtTime(42, time + 0.8);
    
    noise.type = 'triangle';
    noise.frequency.setValueAtTime(130, time); // Throat buzz
    noise.frequency.linearRampToValueAtTime(30, time + 0.8);
    
    // Volume envelope: rapid swell, then rumble down
    gain.gain.setValueAtTime(0.01, time);
    gain.gain.linearRampToValueAtTime(0.35, time + 0.1);
    gain.gain.exponentialRampToValueAtTime(0.001, time + 0.85);
    
    osc1.start(time);
    osc2.start(time);
    noise.start(time);
    
    osc1.stop(time + 0.9);
    osc2.stop(time + 0.9);
    noise.stop(time + 0.9);
  }

  playError() {
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(100, this.ctx.currentTime);

    gain.gain.setValueAtTime(0.25, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.4);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.4);
  }

  playWin() {
    const time = this.ctx.currentTime;
    const chords = [
      [196.00, 246.94, 293.66], // G Major
      [261.63, 329.63, 392.00], // C Major
      [293.66, 369.99, 440.00], // D Major
      [392.00, 493.88, 587.33]  // G Major Octave
    ];
    
    chords.forEach((chord, chordIdx) => {
      const startTime = time + chordIdx * 0.25;
      const duration = 0.5;
      
      chord.forEach((freq) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(freq, startTime);
        
        gain.gain.setValueAtTime(0.01, startTime);
        gain.gain.linearRampToValueAtTime(0.08, startTime + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, startTime + duration);
        
        osc.start(startTime);
        osc.stop(startTime + duration);
      });
    });
  }
}

export default new SoundManager();
