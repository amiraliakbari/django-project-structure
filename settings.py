# -*- coding: utf-8 -*-
# local & server settings switcher
try:
    from local_settings import *
except ImportError:
    from remote_settings import *


# DEBUG SETTINGS
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASEPATH + "logs/logs.txt",
            'maxBytes': 5*1024*1024, # 5M
            'backupCount': 2,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}


# django specific
MANAGERS = ADMINS = ()
SITE_ID = 1


# i18n
LANGUAGE_CODE = 'fa-IR'
TIME_ZONE = 'Iran'
USE_I18N = True
USE_L10N = True


# paths & urls
MEDIA_ROOT = BASEPATH + 'media/'
MEDIA_URL = SITE_URL + 'media/'
UPLOAD_URL = BASEPATH + 'media/uploads/'
STATIC_URL = SITE_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_DIRS = (BASEPATH + 'static/',)
TEMPLATE_DIRS = (BASEPATH + 'templates/',) + TEMPLATE_DIRS


# django loaders
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',)


# project specific settings
#noinspection PyUnresolvedReferences
from project_settings import *
