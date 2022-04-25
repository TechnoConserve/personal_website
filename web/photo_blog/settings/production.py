from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.averyuslaner.com', '178.128.177.110']

EMAIL_SSL_KEYFILE = '/etc/letsencrypt/live/averyuslaner.com/privkey.pem'
EMAIL_SSL_CERTFILE = '/etc/letsencrypt/live/averyuslaner.com/fullchain.pem'

try:
    from .local import *
except ImportError:
    pass

LOGGING['handlers']['console']['level'] = 'ERROR'