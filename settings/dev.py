# -*- coding: utf-8 -*-
from .base import *
import debug_toolbar

DEBUG = True

INSTALLED_APPS += 'debug_toolbar'

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# django-paypal environments
PAYPAL_RECEIVER_EMAIL = 'smkadungure@live.co.uk'
PAYPAL_TEST = True
