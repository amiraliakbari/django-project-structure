# -*- coding: utf-8 -*-
import os

BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

SERVE_STATIC_FILES = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_PATH, 'local_db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
