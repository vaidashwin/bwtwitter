# Use me for dev environments
import os

dirname = os.path.dirname(__file__)
exec(open(os.path.join(dirname, 'settings.py')).read())

DEBUG = True
TEMPLATE_DEBUG = True
WSGI_APPLICATION = None
STATIC_URL = '/static/'
STATIC_ROOT = './bwti/static'

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'yourdatabasename.db'),
    }
}
