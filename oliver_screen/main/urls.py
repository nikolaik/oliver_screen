from django.conf.urls.defaults import *
urlpatterns = patterns('oliver_screen.main.views',
    (r'^tracks', 'tracks'),
    (r'^$', 'index'),
    )

