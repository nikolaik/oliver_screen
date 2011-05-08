from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from oliver_screen.tracks.models import LastFMUser

import pylast
from datetime import datetime
from oliver_screen import settings

network = pylast.LastFMNetwork(api_key = settings.LASTFM_API_KEY, api_secret = settings.LASTFM_API_SECRET)

def get_lastfmuser():
    lastfmusers = LastFMUser.objects.filter(active='yes')
    if len(lastfmusers) != 1:
        # default
        return network.get_user('kakdns')

    return network.get_user(lastfmusers[0].name)

# My views
def get_last_track(request):
    user = get_lastfmuser()
    playedtracks = user.get_recent_tracks(limit=2)
    playback_date  = datetime.strptime(playedtracks[0].playback_date, "%d %b %Y, %H:%M")
    played = {'artist': playedtracks[0].track.get_artist().get_name(),
            'title': playedtracks[0].track.get_title(),
            'playback_date': playback_date,
            # provide utcnow since lastfm servers are UTC
            'utcnow': datetime.utcnow()
            }
    return render_to_response("public/tracks.html", {'played':played});

def get_now_playing(request):
    user = get_lastfmuser()
    track = user.get_now_playing()
    now_playing = []
    if not track is None:
        artist = track.get_artist()
        image = artist.get_images(limit=1)
        if len(image) > 0:
            image = image[0].sizes.original
        now_playing = { 'artist': artist.get_name(), 'title': track.get_title(), 'image': image}
    return render_to_response("public/now_playing.html", {'now_playing':now_playing}, context_instance=RequestContext(request));

# Mock views
def dummy_get_last_track(request):
    played = {'artist': 'The Album Leaf', 'title': 'Another Day (Revised)'}

    return render_to_response("public/tracks.html", {'played':played});

def dummy_now_playing(request):
    now_playing = { 'artist':'The Album Leaf', 'title': 'Over The Pond', 'image': 'http://userserve-ak.last.fm/serve/_/2857325/The+Album+Leaf+1155442304.jpg'}
            
    return render_to_response("public/now_playing.html", {'now_playing':now_playing});
