import django_heroku

from .production import *

ALLOWED_HOSTS = ['*.herokuapp.com']

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.getenv('MEMCACHIER_SERVERS').split(','),
        'OPTIONS': {
                'username': os.getenv('MEMCACHIER_USERNAME'),
                'password': os.getenv('MEMCACHIER_PASSWORD')
            }
    }
}

django_heroku.settings(locals())
