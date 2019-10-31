# [holovin.com](https://www.holovin.com)

## About
E-commerce web application
## Quick installation
```bash
git clone https://github.com/holovin777/holovin.com.git
cd holovin.com/holovin
git clone https://github.com/holovin777/templates.git
git clone https://github.com/holovin777/static_in_dev.git
cd ..
virtualenv venv
source venv/bin/activate
vim holovin/holovin/settings_local.py
```
---
```python
SECRET_KEY = 'entersecretkey!tkekekrlud=jo8+97oo+&90i@a@4c$w1=g+iz#wup!m$_voqrepf2%s'

ALLOWED_HOSTS = ['*']

OSCAR_SHOP_NAME = 'holovin.com'

OSCAR_SHOP_TAGLINE = 'store'

LANGUAGE_CODE = 'en-us'

OSCAR_DEFAULT_CURRENCY = '$'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

```
---
```bash
pip install -r requirements.txt
python holovin/manage.py migrate
python holovin/manage.py createsuperuser
python holovin/manage.py runserver
```
## Deploy with Postgres, Nginx, and Gunicorn on Debian 9 (aws)
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
cd holovin.com/holovin
git clone https://github.com/holovin777/templates.git
git clone https://github.com/holovin777/static_in_dev.git
cd ..
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

OSCAR_SHOP_TAGLINE = 'store'

LANGUAGE_CODE = 'en-us'

OSCAR_DEFAULT_CURRENCY = '$'

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '/media/'

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

#AWS

AWS_ACCESS_KEY_ID = '78G78870DFHFDGHFD'
AWS_SECRET_ACCESS_KEY = 'fd90g78fd90g7890fd70g90dfxg8'
AWS_STORAGE_BUCKET_NAME = 'bucketname'
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
            }
STATIC_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATIC_LOCATION)
STATICFILES_STORAGE = 'holovin.storage_backends.StaticStorage'
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'holovin.storage_backends.PublicMediaStorage'

```
---
```bash
vim holovin/holovin/storage_backends.py
```
---
```python
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
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
        proxy_set_header Host 'holovinbucket.s3.amazonaws.com';
        proxy_set_header Authorization '';
        proxy_hide_header x-amz-id-2;
        proxy_hide_header x-amz-request-id;
        proxy_hide_header Set-Cookie;
        proxy_ignore_headers "Set-Cookie";
        proxy_intercept_errors on;
        proxy_pass https://holovinbucket.s3.amazonaws.com/; # Edit your Amazon S3 Bucket name
        expires 1y;
        log_not_found off;
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

