# [holovin.com](https://www.holovin.com)

## About
E-commerce web application

## Quick installation
```bash
git clone https://github.com/holovin777/holovin.com.git
cd holovin.com
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python holovin/manage.py migrate
python holovin/manage.py createsuperuser
python holovin/manage.py runserver
```

## Deploy with Postgres, Nginx, and Gunicorn on Debian 9
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo reboot
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo -u postgres psql
```
```sql
CREATE DATABASE holovindb;
CREATE USER holovin WITH PASSWORD 'password';
ALTER ROLE holovin SET client_encoding TO 'utf8';
ALTER ROLE holovin SET default_transaction_isolation TO 'read committed';
ALTER ROLE holovin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE holovindb TO holovin;
\q
```
```bash
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
sudo apt update
sudo apt install git
git config --global user.name "YourName"
git config --global user.email "your@mail.org"
git clone https://github.com/holovin777/holovin.com.git
cd holovin.com
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
vim holovin/holovin/settings_local.py
```
---
```python
DEBUG = False

SECRET_KEY = 'enteryoursecretkeylikekrlud=jo8+97oo+&90i@a@4c$w1=g+iz#wup!m$_voqrepf2%s'

ALLOWED_HOSTS = ['www.yourdomainname.org', 'yourdomainname.org']

OSCAR_SHOP_NAME = 'YourShopName'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'holovindb',
        'USER': 'holovin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
---
```bash
python holovin/manage.py migrate
python holovin/manage.py collectstatic
python holovin/manage.py createsuperuser
```
'Open :8000 port'
```bash
python holovin/manage.py runserver 0:8000
cd holovin
gunicorn --bind 0.0.0.0:8000 holovin.wsgi
deactivate
cd ..
sudo vim /etc/systemd/system/gunicorn.socket
```
---
```python
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
---
```bash
sudo vim /etc/systemd/system/gunicorn.service
```
---
```python
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=admin
Group=www-data
WorkingDirectory=/home/admin/holovin.com/holovin
ExecStart=/home/admin/holovin.com/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          holovin.wsgi:application

[Install]
WantedBy=multi-user.target
```
---
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
curl --unix-socket /run/gunicorn.sock localhost
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo vim /etc/nginx/sites-available/holovin.com
```
---
```python
server {
    listen 80;
    server_name www.yordomainname.org yourdomainname.org;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/admin/holovin.com/holovin;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
---
```bash
sudo ln -s /etc/nginx/sites-available/holovin.com /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```
'Close :8000 port'
```bash
exit
```

## Secure Nginx with Let's Encrypt on Debian 9

```bash
sudo vim /etc/apt/sources.list
```
---
```python
...
deb http://deb.debian.org/debian stretch-backports main contrib non-free
deb-src http://deb.debian.org/debian stretch-backports main contrib non-free
```
---
```bash
sudo apt update
sudo apt install python-certbot-nginx -t stretch-backports
sudo vim /etc/nginx/sites-available/holovin.com
```
---
```python
...
server_name yourdomainnaim.org www.yourdomainnaim.org;
...
```
---
```bash
sudo nginx -t
sudo systemctl reload nginx
```
'Open :443 port'
```bash
sudo certbot --nginx -d yourdomainnaim.org -d www.yourdomainnaim.org
```

### Initial data

The default checkout process requires a shipping address with a country. Oscar uses a model for countries with flags that indicate which are valid shipping countries and so the country database table must be populated before a customer can check out.
The easiest way to achieve this is to use country data from the pycountry package. Oscar ships with a management command to parse that data:
```bash
pip install pycountry
python holovin/manage.py oscar_populate_countries
```
By default, this command will mark all countries as a shipping country. Call it with the --no-shipping option to prevent that. You then need to manually mark at least one country as a shipping country.

### Commands server

```bash
sudo ssh -i Downloads/Key.pem admin@0.0.0.0
sudo scp -i /home/admin/Downloads/Key.pem /home/admin/Pictures/logo.svg admin@0.0.0.0:/home/admin/holovin.com/holovin/static_in_dev/logo.svg
sudo systemctl restart gunicorn
sudo systemctl reload nginx
```

#### License [GNU](https://choosealicense.com/licenses/gpl-3.0/)

