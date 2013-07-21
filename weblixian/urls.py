from django.conf.urls import patterns
#from webui.webui import hello
from webui.views import index, download, check
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', index),
    ('^download/$', download),
    ('^check/$', check),
)

if settings.DEBUG: 
    urlpatterns += patterns('', 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}), 
    ) 