#!/usr/bin/env python
import imp
import sys
import os
from django.core.management import execute_manager, setup_environ, ManagementUtility

try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write(
        "Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings
sys.path.append('%ssrc' % settings.BASEPATH)
sys.path.append('%slib' % settings.BASEPATH)

if __name__ == "__main__":
    setup_environ(settings)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    utility = ManagementUtility()
    utility.execute()
