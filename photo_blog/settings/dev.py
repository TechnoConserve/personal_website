from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = 'secret'

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

EMAIL_SSL_KEYFILE = '/home/ave/PycharmProjects/averyuslaner.com/privkey.pem'
EMAIL_SSL_CERTFILE = '/home/ave/PycharmProjects/averyuslaner.com/fullchain.pem'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test'
    }
}

try:
    from .local import *
except ImportError:
    pass
