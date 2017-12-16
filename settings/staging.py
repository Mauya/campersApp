# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://git.heroku.com/campersapp.git'
PAYPAL_RECEIVER_EMAIL = 'smkadungure@live.co.uk'

SITE_URL = 'https://git.heroku.com/campersapp.git'
ALLOWED_HOSTS.append('campersapp.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
