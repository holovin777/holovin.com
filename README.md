# [holovin.com](https://www.holovin.com)

### About
Open source e-commerce python web application

Templates repository are located [here](https://github.com/holovin777/templates)

Static files are located [here](https://github.com/holovin777/static_in_dev)
### Quick installation
```bash
git clone https://github.com/holovin777/holovin.com.git
cd holovin.com
git clone https://github.com/holovin777/templates.git
git clone https://github.com/holovin777/static_in_dev.git
vim templates/oscar/partials/footer.html
```
```html
{% load staticfiles %}
{% load i18n %}
<footer class="footer container-fluid">
    {% block footer %}
        {% comment %}
            Could be used for displaying links to privacy policy, terms of service, etc.
            We have a CSS class defined:
                <ul class="footer_links inline">
                    ...
                </ul>
         {% endcomment %}
        <div class="text-center">
        <br>
          <a class="" href="https://www.github.com/holovin777/holovin.com/">
		  <img src="https://image.flaticon.com/icons/svg/1051/1051275.svg" height="40" class="d-inline-block align-top" alt="">&nbsp;&nbsp;
          </a>
	  {% comment %}
	  <a class="" href="https://www.instagram.com/holovin777/">
            <img src="https://image.flaticon.com/icons/svg/174/174855.svg" height="40" class="d-inline-block align-top" alt="">&nbsp;&nbsp;
          </a>
	  <a class="" href="https://www.youtube.com/channel/UCJGCyQHY92xsUgBuivu5-Hw/featured?view_as=subscriber">
            <img src="https://image.flaticon.com/icons/svg/174/174883.svg" height="40" class="d-inline-block align-top" alt="">&nbsp;&nbsp;
          </a>
	  {% endcomment %}
	  <br><br>
<div class="text-center text-secondary">
    <small>
        Copyright © 2020
        <a class="" href="/home">
            <img src="{% static 'logowhite.svg' %}" height="27" class="d-inline-block align-top" alt="">
             {{ shop_name }} <small class="text-secondary"> {{ shop_tagline }}</small>
        </a>
    </small>
</div>
	</div>
    {% endblock %}
</footer>
```
```bash
python3 -m venv venv
source venv/bin/activate
vim holovin/settings_local.py
```
---
```python
SECRET_KEY = 'entersecretkey!tkekekrlud=jo8+97oo+&90i@a@4c$w1=g+iz#wup!m$_voqrepf2%s'

ALLOWED_HOSTS = ['*']

OSCAR_SHOP_NAME = 'holovin'

OSCAR_SHOP_TAGLINE = 'com'

LANGUAGE_CODE = 'en-us'

OSCAR_DEFAULT_CURRENCY = '$'

OSCAR_HOMEPAGE = '/home/'

#OSCAR_USE_LESS = True
```
---
```bash
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
### Deploy with Postgres, Nginx, and Gunicorn on Debian 9 (aws)
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
git clone https://github.com/holovin777/templates.git
git clone https://github.com/holovin777/static_in_dev.git
vim templates/oscar/partials/footer.html
```
```html
{% load staticfiles %}
{% load i18n %}
<footer class="footer container-fluid">
    {% block footer %}
        {% comment %}
            Could be used for displaying links to privacy policy, terms of service, etc.
            We have a CSS class defined:
                <ul class="footer_links inline">
                    ...
                </ul>
         {% endcomment %}
        <div class="text-center">
        <br>
          <a class="" href="https://www.github.com/holovin777/holovin.com/">
		  <img src="https://image.flaticon.com/icons/svg/1051/1051275.svg" height="40" class="d-inline-block align-top" alt="">&nbsp;&nbsp;
          </a>
	  {% comment %}
	  <a class="" href="https://www.instagram.com/holovin777/">
            <img src="https://image.flaticon.com/icons/svg/174/174855.svg" height="40" class="d-inline-block align-top" alt="">&nbsp;&nbsp;
          </a>
	  <a class="" href="https://www.youtube.com/channel/UCJGCyQHY92xsUgBuivu5-Hw/featured?view_as=subscriber">
            <img src="https://image.flaticon.com/icons/svg/174/174883.svg" height="40" class="d-inline-block align-top" alt="">&nbsp;&nbsp;
          </a>
	  {% endcomment %}
	  <br><br>
<div class="text-center text-secondary">
    <small>
        Copyright © 2020
        <a class="" href="/home">
            <img src="{% static 'logowhite.svg' %}" height="27" class="d-inline-block align-top" alt="">
             {{ shop_name }} <small class="text-secondary"> {{ shop_tagline }}</small>
        </a>
    </small>
</div>
	</div>
    {% endblock %}
</footer>
```
```bash
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
vim holovin/settings_local.py
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

OSCAR_HOMEPAGE = '/home/'

#OSCAR_USE_LESS = True

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
#AWS

AWS_ACCESS_KEY_ID = '78G78870DFHFDGHFD'
AWS_SECRET_ACCESS_KEY = 'fd90g78fd90g7890fd70g90dfxg8'
AWS_STORAGE_BUCKET_NAME = 'bucketname'
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
            }
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'holovin.storage_backends.PublicMediaStorage'
```
---
```bash
vim holovin/storage_backends.py
```
---
```python
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
```
---
'CORS configuration'
---
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
   <AllowedOrigin>*</AllowedOrigin>
   <AllowedMethod>GET</AllowedMethod>
   <AllowedMethod>HEAD</AllowedMethod>
   <MaxAgeSeconds>3000</MaxAgeSeconds>
   <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
---
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```
'Open :8000 port'
```bash
python manage.py runserver 0:8000
gunicorn --bind 0.0.0.0:8000 holovin.wsgi
deactivate
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
WorkingDirectory=/home/admin/holovin.com/
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
        root /home/admin/holovin.com;
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

### Secure Nginx with Let's Encrypt on Debian 9

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

#### Initial data

The default checkout process requires a shipping address with a country. Oscar uses a model for countries with flags that indicate which are valid shipping countries and so the country database table must be populated before a customer can check out.
The easiest way to achieve this is to use country data from the pycountry package. Oscar ships with a management command to parse that data:
```bash
pip install pycountry
python manage.py oscar_populate_countries
```
By default, this command will mark all countries as a shipping country. Call it with the --no-shipping option to prevent that. You then need to manually mark at least one country as a shipping country.

#### Commands server

```bash
sudo ssh -i Downloads/Key.pem admin@0.0.0.0
sudo scp -i /home/admin/Downloads/Key.pem /home/admin/Pictures/logo.svg admin@0.0.0.0:/home/admin/holovin.com/holovin/static_in_dev/logo.svg
sudo systemctl restart gunicorn
sudo systemctl reload nginx
```

##### License [GNU](https://choosealicense.com/licenses/gpl-3.0/)

