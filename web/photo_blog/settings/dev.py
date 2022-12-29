import socket

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = 'secret'

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'} }

EMAIL_SSL_KEYFILE = '/home/ave/PycharmProjects/averyuslaner.com/privkey.pem'
EMAIL_SSL_CERTFILE = '/home/ave/PycharmProjects/averyuslaner.com/fullchain.pem'

INSTALLED_APPS += [
    'debug_toolbar'
]

try:
    from .local import *
except ImportError:
    pass
