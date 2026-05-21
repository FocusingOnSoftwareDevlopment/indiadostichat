// Card Definitions and Rules Engine for Dosti Cards (UNO-style)

const COLORS = ['red', 'yellow', 'green', 'blue'];
const VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'draw2'];
const WILD_VALUES = ['wild', 'wild4'];

// Score mapping for calculating winning round scores
const CARD_SCORES = {
  '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  'skip': 20,
  'reverse': 20,
  'draw2': 20,
  'wild': 50,
  'wild4': 50
};

// Generate a brand new, shuffled deck (108 cards standard)
function createDeck() {
  const deck = [];
  let cardId = 0;

  // Add colored cards
  for (const color of COLORS) {
    // One '0' card per color
    deck.push({ id: `card_${cardId++}`, color, value: '0', score: CARD_SCORES['0'] });

    // Two of each 1-9, skip, reverse, draw2 per color
    for (const val of VALUES.filter(v => v !== '0')) {
      deck.push({ id: `card_${cardId++}`, color, value: val, score: CARD_SCORES[val] });
      deck.push({ id: `card_${cardId++}`, color, value: val, score: CARD_SCORES[val] });
    }
  }

  // Four of each Wild card
  for (let i = 0; i < 4; i++) {
    deck.push({ id: `card_${cardId++}`, color: 'wild', value: 'wild', score: CARD_SCORES['wild'] });
    deck.push({ id: `card_${cardId++}`, color: 'wild', value: 'wild4', score: CARD_SCORES['wild4'] });
  }

  return shuffle(deck);
}

// Fisher-Yates Shuffle
function shuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Check if a card is playable given the top card, current selected color, and active card drawings
function isPlayable(card, topCard, currentColor, drawPending) {
  // If there are pending draw cards (from Draw Two or Wild Draw Four), the player cannot play normal cards
  // Note: Standard rules state card draw stack isn't stackable unless specific house rules are enabled.
  // We will use standard rules (playing skips/turns/draws resolved immediately, no stacking of draws to avoid over-complicating).
  
  // Wild cards are always playable
  if (card.color === 'wild') {
    return true;
  }

  // Matching color
  if (card.color === currentColor) {
    return true;
  }

  // Matching value (e.g. Red Skip can be played on Blue Skip)
  if (card.value === topCard.value) {
    return true;
  }

  return false;
}

// Calculate the score of a player's hand
function calculateHandScore(cards) {
  return cards.reduce((sum, card) => sum + (card.score || 0), 0);
}

module.exports = {
  COLORS,
  VALUES,
  WILD_VALUES,
  createDeck,
  shuffle,
  isPlayable,
  calculateHandScore
};
