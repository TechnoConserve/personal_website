from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.averyuslaner.com', '178.128.177.110', '138.68.54.97']

EMAIL_SSL_KEYFILE = '/etc/letsencrypt/live/averyuslaner.com/privkey.pem'
EMAIL_SSL_CERTFILE = '/etc/letsencrypt/live/averyuslaner.com/fullchain.pem'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
}