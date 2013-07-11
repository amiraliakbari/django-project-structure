# -*- coding: utf-8 -*-
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()  # Parse database configuration from $DATABASE_URL
}

DEBUG = False
