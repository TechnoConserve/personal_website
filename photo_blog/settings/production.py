from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.averyuslaner.com', '104.236.24.80']

EMAIL_SSL_KEYFILE = '/etc/letsencrypt/live/conservationtechnologysolutions.com/privkey.pem'
EMAIL_SSL_CERTFILE = '/etc/letsencrypt/live/conservationtechnologysolutions.com/fullchain.pem'

try:
    from .local import *
except ImportError:
    pass
