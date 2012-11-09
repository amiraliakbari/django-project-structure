# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('sma.people.views',
    url(r'^(?:dashboard)$', 'dashboard', name='people/dashboard'),
)
