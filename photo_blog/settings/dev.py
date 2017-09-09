from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

EMAIL_SSL_KEYFILE = '/home/ave/PycharmProjects/averyuslaner.com/privkey.pem'
EMAIL_SSL_CERTFILE = '/home/ave/PycharmProjects/averyuslaner.com/fullchain.pem'

try:
    from .local import *
except ImportError:
    pass
