# ON-CARE Medicine Ordering System - Production Deployment Guide

## Overview
This guide provides step-by-step instructions for deploying the ON-CARE Medicine Ordering System to production environment.

## Prerequisites

### System Requirements
- **Operating System**: Ubuntu 20.04 LTS or CentOS 8+
- **Python**: 3.8 or higher
- **Database**: MySQL 8.0 or MariaDB 10.4+
- **Web Server**: Nginx 1.18+
- **Application Server**: Gunicorn or uWSGI
- **Cache**: Redis 6.0+
- **Memory**: Minimum 4GB RAM
- **Storage**: Minimum 50GB SSD

### Software Dependencies
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3.8 python3.8-pip python3.8-venv -y

# Install MySQL
sudo apt install mysql-server mysql-client -y

# Install Nginx
sudo apt install nginx -y

# Install Redis
sudo apt install redis-server -y

# Install system dependencies
sudo apt install build-essential libmysqlclient-dev pkg-config -y
```

## Step 1: Database Setup

### 1.1 Create MySQL Database and User
```sql
-- Connect to MySQL as root
sudo mysql -u root -p

-- Create database
CREATE DATABASE oncare_production_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user
CREATE USER 'oncare_user'@'localhost' IDENTIFIED BY 'your_secure_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON oncare_production_db.* TO 'oncare_user'@'localhost';
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
```

### 1.2 Test Database Connection
```bash
mysql -u oncare_user -p oncare_production_db
```

## Step 2: Application Deployment

### 2.1 Create Application Directory
```bash
sudo mkdir -p /opt/oncare
sudo chown $USER:$USER /opt/oncare
cd /opt/oncare
```

### 2.2 Clone and Setup Application
```bash
# Clone the repository (adjust URL as needed)
git clone <repository-url> medicine_ordering_system
cd medicine_ordering_system

# Create virtual environment
python3.8 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.3 Environment Configuration
```bash
# Create environment file
cat > .env << EOF
# Database Configuration
DB_NAME=oncare_production_db
DB_USER=oncare_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=3306

# Django Configuration
DJANGO_SECRET_KEY=your_super_secure_secret_key_here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# Redis Configuration
REDIS_URL=redis://localhost:6379/1
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
EOF
```

### 2.4 Database Migration
```bash
# Run migrations
python manage.py migrate --settings=medicine_ordering_system.production_settings

# Create superuser
python manage.py createsuperuser --settings=medicine_ordering_system.production_settings

# Collect static files
python manage.py collectstatic --settings=medicine_ordering_system.production_settings --noinput
```

## Step 3: Web Server Configuration

### 3.1 Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/oncare
```

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL Configuration (use Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    
    # Static files
    location /static/ {
        alias /opt/oncare/medicine_ordering_system/staticfiles/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # Media files
    location /media/ {
        alias /opt/oncare/medicine_ordering_system/media/;
        expires 1y;
        add_header Cache-Control "public";
    }
    
    # Application
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
```

### 3.2 Enable Site and Test Configuration
```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/oncare /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# Reload Nginx
sudo systemctl reload nginx
```

## Step 4: Application Server Configuration

### 4.1 Install and Configure Gunicorn
```bash
# Install Gunicorn
pip install gunicorn

# Create Gunicorn configuration
cat > gunicorn_config.py << EOF
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
preload_app = True
user = "www-data"
group = "www-data"
daemon = False
pidfile = "/opt/oncare/gunicorn.pid"
accesslog = "/opt/oncare/logs/gunicorn_access.log"
errorlog = "/opt/oncare/logs/gunicorn_error.log"
loglevel = "info"
EOF
```

### 4.2 Create Systemd Service
```bash
sudo nano /etc/systemd/system/oncare.service
```

```ini
[Unit]
Description=ON-CARE Medicine Ordering System
After=network.target mysql.service redis.service

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/opt/oncare/medicine_ordering_system
Environment="DJANGO_SETTINGS_MODULE=medicine_ordering_system.production_settings"
ExecStart=/opt/oncare/medicine_ordering_system/venv/bin/gunicorn --config gunicorn_config.py medicine_ordering_system.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 4.3 Enable and Start Services
```bash
# Enable services
sudo systemctl enable oncare.service
sudo systemctl enable nginx.service
sudo systemctl enable mysql.service
sudo systemctl enable redis.service

# Start services
sudo systemctl start oncare.service
sudo systemctl start nginx.service
sudo systemctl start mysql.service
sudo systemctl start redis.service

# Check status
sudo systemctl status oncare.service
```

## Step 5: SSL Certificate Setup

### 5.1 Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 5.2 Obtain SSL Certificate
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 5.3 Setup Auto-renewal
```bash
sudo crontab -e
# Add this line:
0 12 * * * /usr/bin/certbot renew --quiet
```

## Step 6: Monitoring and Logging

### 6.1 Setup Log Rotation
```bash
sudo nano /etc/logrotate.d/oncare
```

```
/opt/oncare/logs/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 www-data www-data
    postrotate
        systemctl reload oncare
    endscript
}
```

### 6.2 Install Monitoring Tools
```bash
# Install htop for system monitoring
sudo apt install htop -y

# Install fail2ban for security
sudo apt install fail2ban -y
```

### 6.3 Configure Fail2ban
```bash
sudo nano /etc/fail2ban/jail.local
```

```ini
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5

[nginx-http-auth]
enabled = true

[nginx-limit-req]
enabled = true
```

## Step 7: Backup Configuration

### 7.1 Database Backup Script
```bash
cat > /opt/oncare/backup_db.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/opt/oncare/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="oncare_production_db"
DB_USER="oncare_user"

mkdir -p $BACKUP_DIR

# Database backup
mysqldump -u $DB_USER -p$DB_PASSWORD $DB_NAME | gzip > $BACKUP_DIR/db_backup_$DATE.sql.gz

# Keep only last 30 days of backups
find $BACKUP_DIR -name "db_backup_*.sql.gz" -mtime +30 -delete

echo "Database backup completed: db_backup_$DATE.sql.gz"
EOF

chmod +x /opt/oncare/backup_db.sh
```

### 7.2 Setup Automated Backups
```bash
# Add to crontab
sudo crontab -e
# Add this line for daily backups at 2 AM:
0 2 * * * /opt/oncare/backup_db.sh
```

## Step 8: Performance Optimization

### 8.1 MySQL Optimization
```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

```ini
[mysqld]
innodb_buffer_pool_size = 1G
innodb_log_file_size = 256M
innodb_flush_log_at_trx_commit = 2
query_cache_size = 128M
query_cache_type = 1
max_connections = 200
```

### 8.2 Redis Optimization
```bash
sudo nano /etc/redis/redis.conf
```

```ini
maxmemory 256mb
maxmemory-policy allkeys-lru
save 900 1
save 300 10
save 60 10000
```

## Step 9: Security Hardening

### 9.1 Firewall Configuration
```bash
# Install UFW
sudo apt install ufw -y

# Configure firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### 9.2 SSH Security
```bash
sudo nano /etc/ssh/sshd_config
```

```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Port 2222
```

## Step 10: Health Checks and Maintenance

### 10.1 Health Check Script
```bash
cat > /opt/oncare/health_check.sh << 'EOF'
#!/bin/bash

# Check if services are running
services=("nginx" "mysql" "redis" "oncare")

for service in "${services[@]}"; do
    if ! systemctl is-active --quiet $service; then
        echo "ERROR: $service is not running"
        systemctl restart $service
    else
        echo "OK: $service is running"
    fi
done

# Check database connection
if ! mysql -u oncare_user -p$DB_PASSWORD -e "SELECT 1;" oncare_production_db > /dev/null 2>&1; then
    echo "ERROR: Database connection failed"
else
    echo "OK: Database connection successful"
fi

# Check application response
if ! curl -f http://localhost:8000/ > /dev/null 2>&1; then
    echo "ERROR: Application not responding"
else
    echo "OK: Application is responding"
fi
EOF

chmod +x /opt/oncare/health_check.sh
```

### 10.2 Setup Monitoring Alerts
```bash
# Add health check to crontab
sudo crontab -e
# Add this line for every 5 minutes:
*/5 * * * * /opt/oncare/health_check.sh >> /opt/oncare/logs/health_check.log
```

## Post-Deployment Checklist

- [ ] Database migrations completed successfully
- [ ] Static files collected and served correctly
- [ ] SSL certificate installed and working
- [ ] All services running and healthy
- [ ] Firewall configured and enabled
- [ ] Backups configured and tested
- [ ] Monitoring and logging setup
- [ ] Performance optimization applied
- [ ] Security hardening completed
- [ ] Health checks passing

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Check MySQL service status
   - Verify database credentials
   - Check firewall rules

2. **Static Files Not Loading**
   - Verify STATIC_ROOT configuration
   - Check Nginx static file configuration
   - Ensure proper file permissions

3. **SSL Certificate Issues**
   - Verify domain DNS configuration
   - Check Certbot logs
   - Ensure port 80 is accessible

4. **Application Not Starting**
   - Check Gunicorn logs
   - Verify Python dependencies
   - Check file permissions

### Log Locations
- Application logs: `/opt/oncare/logs/`
- Nginx logs: `/var/log/nginx/`
- MySQL logs: `/var/log/mysql/`
- System logs: `/var/log/syslog`

## Support and Maintenance

For ongoing maintenance:
1. Regular security updates
2. Database optimization
3. Log monitoring and cleanup
4. Performance monitoring
5. Backup verification

---

**Note**: This deployment guide is designed for a production environment. Always test in a staging environment first and ensure you have proper backups before deploying to production.