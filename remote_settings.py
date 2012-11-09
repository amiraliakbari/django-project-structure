# -*- coding: utf-8 -*-
import project

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASEPATH = '/www/%s/' % project.NAME
STATIC_ROOT = BASEPATH + '../statics/%s' % project.NAME
SITE_URL = 'http://?/'

TEMPLATE_DIRS = ('/usr/local/lib/python2.7/dist-packages/django/contrib/admin/templates/',)

SERVE_STATIC_FILES = False

SECRET_KEY = '?'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%ssrc/%s.sqlite' % (BASEPATH, project.NAME),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
