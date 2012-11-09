# -*- coding: utf-8 -*-
import project

ROOT_URLCONF = '%s.urls' % project.NAME
LOGIN_URL = '/admin/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'debug_toolbar',
    'dj_utils',

    'sma.people')
