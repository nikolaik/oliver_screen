from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # static file serving for development (http://docs.djangoproject.com/en/dev/howto/static-files/)
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/nikk/dev/edb/oliver_screen/oliver_screen/static'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^tracks/', include('oliver_screen.tracks.urls')),
    (r'^$', include('oliver_screen.main.urls')),
)
