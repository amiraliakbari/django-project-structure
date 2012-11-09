# -*- coding: utf-8 -*-
from django.conf                           import settings
from django.contrib                        import admin
from django.conf.urls.defaults             import patterns, include, url


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^people/', include('sma.people.urls')),
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, )
    )

urlpatterns += patterns('',
    url(r'^favicon.ico$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'path': 'images/favicon.ico'}),
    url(r'^robots.txt$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'path': 'robots.txt'}),
)
