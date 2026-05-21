module.exports = {
  apps: [
    {
      name: 'dosti-cards-backend',
      script: './src/index.js',
      cwd: './backend',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        NODE_ENV: 'production',
        PORT: 5000,
        JWT_SECRET: 'supersecretchangeinproduction',
        ADMIN_USERNAME: 'Heisenberg',
        ADMIN_PASSWORD_HASH: '$2a$10$7Z2D5J6.nO72r5t/p.mKpew5i3o.2L8r19M/Tq2X8jYm.zW/c1t2G' // heisenberg123
      },
      env_production: {
        NODE_ENV: 'production',
        PORT: 5000
      }
    }
  ]
};
