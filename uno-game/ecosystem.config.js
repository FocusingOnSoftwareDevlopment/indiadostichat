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
        ADMIN_PASSWORD_HASH: '$2a$10$zuPdbN2NiyuvH/II8aclNeA9nn6KxTkJxoVGx5JkcWJeuQHuK4pjK' // heisenberg123
      },
      env_production: {
        NODE_ENV: 'production',
        PORT: 5000
      }
    }
  ]
};
