# Dosti Cards - Production Deployment Guide

This guide details the steps required to deploy the **Dosti Cards** multiplayer game server to a VPS running Ubuntu/Debian, utilizing Nginx as a reverse proxy, PM2 for process clustering, and optionally PostgreSQL.

---

## 1. Environment Setup

Connect to your VPS server via SSH and execute the following setup commands:

### A. Node.js Installation
Configure NodeSource repositories and install Node.js v20+ (LTS):
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### B. PM2 & Build Tools
Install PM2 globally to daemonize Node.js and build packages:
```bash
sudo npm install -y pm2 -g
sudo apt-get install -y build-essential
```

### C. PostgreSQL Database (Optional)
If you want to use persistent database storage (retains user records, completed match ledgers, ban registries, and scores), install PostgreSQL:
```bash
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
```
*Note: If no database configuration is detected in environment files, the backend defaults to a secure in-memory database mock automatically.*

---

## 2. Server Installation & Build

1. Clone or copy the `uno-game` repository folder to your VPS target directory (e.g., `/var/www/dosti-cards`).
2. Navigate to the backend folder, install production dependencies:
   ```bash
   cd backend
   npm install --omit=dev
   ```
3. Set up the production variables in `.env` file under the `backend/` folder:
   ```env
   PORT=5000
   JWT_SECRET=use-a-strong-random-key-here
   ADMIN_USERNAME=Heisenberg
   ADMIN_PASSWORD_HASH=$2a$10$7Z2D5J6.nO72r5t/p.mKpew5i3o.2L8r19M/Tq2X8jYm.zW/c1t2G # bcrypt hash of 'heisenberg123'
   
   # PostgreSQL configuration (Uncomment to use PostgreSQL instead of In-Memory mock)
   # DATABASE_URL=postgresql://dbuser:dbpass@localhost:5432/dosticards
   ```
4. If using PostgreSQL, create the database and seed the schema:
   ```bash
   # Log in as postgres user
   sudo -u postgres psql
   
   # Create database & user inside interactive shell
   CREATE DATABASE dosticards;
   CREATE USER dbuser WITH PASSWORD 'dbpass';
   GRANT ALL PRIVILEGES ON DATABASE dosticards TO dbuser;
   \q
   
   # Run schema migration script
   psql -U dbuser -d dosticards -f src/db/schema.sql -h localhost -W
   ```
5. Navigate to the frontend folder, install dependencies, and compile the production client bundle:
   ```bash
   cd ../frontend
   npm install
   npm run build
   ```
   *Note: This generates HTML, JS, and CSS assets under `frontend/dist/` which are served statically by the Express backend for single-port convenience.*

---

## 3. Daemon Management with PM2

Start and register the Dosti Cards backend as a background service:
```bash
cd ..
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

Useful PM2 CLI Commands:
- **Monitor status**: `pm2 status`
- **Live console logs**: `pm2 logs dosti-cards-backend`
- **Restart process**: `pm2 restart dosti-cards-backend`
- **Stop process**: `pm2 stop dosti-cards-backend`

---

## 4. Nginx Reverse Proxy with HTTPS & WebSockets

To enable public client traffic, handle SSL termination, and proxy WebSockets without connection drops, use the following configuration blocks.

1. Install Nginx:
   ```bash
   sudo apt-get install -y nginx
   ```
2. Create a new site config `/etc/nginx/sites-available/dosticards`:
   ```nginx
   server {
       listen 80;
       server_name cards.indiadostichat.com; # Replace with your subdomain/domain
   
       # Client static build and API endpoints
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_http_version 1.1;
           
           # Reverse proxy headers
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   
       # Dedicated WebSocket / socket.io upgrade block
       location /socket.io/ {
           proxy_pass http://127.0.0.1:5000/socket.io/;
           proxy_http_version 1.1;
           
           # Upgrade connection for WebSockets
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "Upgrade";
           
           # Disable request buffers for instant synchronization
           proxy_buffering off;
           
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }
   ```
3. Enable the configuration and restart Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/dosticards /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```
4. Obtain a free SSL certificate from Let's Encrypt Certbot:
   ```bash
   sudo apt-get install -y certbot python3-certbot-nginx
   sudo certbot --nginx -d cards.indiadostichat.com
   ```

Now, your multiplayer card game is running in production with secure SSL links and WebSockets routing!
