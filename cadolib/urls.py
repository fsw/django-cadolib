import inspect

from django.conf.urls.defaults import include, patterns, url
from django.shortcuts import redirect
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^extrafields/(?P<model>[A-Za-z0-9\-\.]*)/(?P<provider_id>\d+)$', 'cadolib.views.extrafields', name='cadolib_extrafields'),                      
)



"""
def Urls():
    
    def getPatterns(self):
        print "ASDFADSF"
        return pattrns() 
"""

