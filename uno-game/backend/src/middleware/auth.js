const jwt = require('jsonwebtoken');
require('dotenv').config();

const JWT_SECRET = process.env.JWT_SECRET || 'supersecretchangeinproduction';
const ADMIN_USERNAME = process.env.ADMIN_USERNAME || 'Heisenberg';

// Verify Admin token
function authenticateAdmin(req, res, next) {
  const authHeader = req.headers['authorization'];
  if (!authHeader) {
    return res.status(401).json({ error: 'Access denied. No token provided.' });
  }

  const token = authHeader.split(' ')[1]; // Format: Bearer <token>
  if (!token) {
    return res.status(401).json({ error: 'Access denied. Invalid header format.' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    if (decoded.username !== ADMIN_USERNAME) {
      return res.status(403).json({ error: 'Access denied. Unauthorized user.' });
    }
    req.admin = decoded;
    next();
  } catch (ex) {
    res.status(400).json({ error: 'Invalid token.' });
  }
}

module.exports = {
  authenticateAdmin
};
