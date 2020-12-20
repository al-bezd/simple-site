from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!=6hkdyfvpsko+yirl9d4bddvizdwhwv-w27-nv%tpz8-d+876'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
if not DEBUG:
    ACCOUNT_USERNAME_BLACKLIST = ["admin", "god"]

try:
    from .local import *
except ImportError:
    pass
