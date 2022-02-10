# Test-Task
API for a mobile application in which a customer's field worker visits a store.


# 🛠 Tech stack
Python 3.9.10 , Django Rest, Postgres

## Local developer installing and running
    The first thing to do is to clone the repository
    Create a virtual environment to install dependencies in and activate it:
    Create local_settings.py in project and add 

    
    Genereta new secret key 

    $ python -c 'from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key()) add output in SECRET_KEY

    SECRET_KEY = ^
    ALLOWED_HOSTS = [] 
    DEBUG = True 
    
    Add in local_settings 
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    $ sudo apt-get update
    $ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx ntp virtualenv
    $ sudo adduser ubuntu
    $ sudo -u postgres psql

Create database
---------------
    CREATE DATABASE Testdb;
    CREATE USER Test_user WITH PASSWORD 'Test_password';
    ALTER ROLE Test_user SET client_encoding TO 'utf8';
    ALTER ROLE Test_user SET default_transaction_isolation TO 'read committed';
    GRANT ALL PRIVILEGES ON DATABASE Test_db TO Test_user;
    
    After add .env file and add info db (see > .env.example)

## Installation

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Pages

Administration - http://127.0.0.1:8000/admin/  
Api endpoint - (http://127.0.0.1:8000/api/v1/visit/  
Search by phone - (http://127.0.0.1:8000/api/v1/visit/?search=777777  