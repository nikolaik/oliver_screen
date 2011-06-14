from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from os.path import dirname, join

def map_path(target_name):
	'''Enables path names to be decided at runtime.'''
	return join(dirname(__file__), target_name).replace('\\', '/')

urlpatterns = patterns('',
    # static file serving for development (http://docs.djangoproject.com/en/dev/howto/static-files/)
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': map_path('static')}),
    (r'^admin/', include(admin.site.urls)),
    (r'^tracks/', include('oliver_screen.tracks.urls')),
    (r'^$', include('oliver_screen.main.urls')),
)
