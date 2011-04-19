from django.conf.urls.defaults import *
urlpatterns = patterns('oliver_screen.tracks.views',
    (r'^last/$', 'get_last_track'),
    (r'^now_playing/$', 'get_now_playing'),
    )

