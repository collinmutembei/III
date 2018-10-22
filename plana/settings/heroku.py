import django_heroku

from .production import *

ALLOWED_HOSTS = ['*.herokuapp.com']

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
                'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
                'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
            }
    }
}

django_heroku.settings(locals())
