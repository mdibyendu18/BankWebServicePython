from .base import *

DEBUG = True
INSTALLED_APPS += (
        'debug_toolbar',
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bank_detail',
        'USER': 'btfyle',
        'PASSWORD': 'btfyle',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}