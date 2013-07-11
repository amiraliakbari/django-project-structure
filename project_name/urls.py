# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.static import serve


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^app/', include('project_name.app.urls')),
)

direct_statics = [
    ('robots.txt', 'robots.txt'),
    ('favicon.ico', 'images/favicon.ico'),
]


#################
#  Auto Config  #
#################
try:
    if settings.SERVE_STATIC_FILES:
        urlpatterns += patterns(
            '',
            url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
            url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, )
        )
except AttributeError:
    pass

urlpatterns += patterns(
    '',
    *[url(r'^%s$' % ds[0], serve, {'document_root': settings.STATIC_ROOT, 'path': ds[1]}) for ds in direct_statics]
)
