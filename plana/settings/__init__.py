import os

APP_ENV = os.getenv('APP_ENV', 'production')

if APP_ENV in ('develop', 'heroku', 'production'):
    exec('from .{0} import *'.format(APP_ENV))
