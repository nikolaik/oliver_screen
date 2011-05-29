from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from oliver_screen.tracks.models import LastFMUser, YouTubeVideo, CurrentTrack

import pylast
from datetime import datetime
from oliver_screen import settings

network = pylast.LastFMNetwork(api_key = settings.LASTFM_API_KEY, api_secret = settings.LASTFM_API_SECRET)

def get_lastfmuser():
    lastfmusers = LastFMUser.objects.filter(active=True)
    if len(lastfmusers) != 1:
        # default
        return network.get_user('kakdns')

    return network.get_user(lastfmusers[0].name)

def get_youtubevideo(artist, title):
    videos = YouTubeVideo.objects.filter(artist=artist, title=title)
    if len(videos) != 1:
        # should only be one
        return ""
    return videos[0]



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
        video = get_youtubevideo(artist.get_name(), track.get_title())
        image = artist.get_images(limit=1)
        if len(image) > 0:
            image = image[0].sizes.original

        now_playing = {
            'artist': artist.get_name(),
            'title': track.get_title(),
            'image': image,
            'video': video
        }
        cache_current(now_playing)
    else:
        # No response from LastFM db?
        now_playing = get_current_from_cache()
        
    return render_to_response("public/now_playing.html", {'now_playing':now_playing}, context_instance=RequestContext(request));

def cache_current(now_playing):
    # Fetch the one CurrentTrack entry in the db and update it with the current track.
    current = CurrentTrack.objects.get(pk=1)
    if not current is None:
        #update
        current.artist = now_playing['artist']
        current.title = now_playing['title']
        current.image = now_playing['image']
        current.retries = 0
        current.save()
    else:
        # First time running? Then creat it.
        current = CurrentTrack(artist=now_playing.artist, title=now_playing.title, image=now_playing.image, retries=0)
        current.save()

def get_current_from_cache():
    current = []
    try:
        current = CurrentTrack.objects.get(pk=1)
    except:
        current = CurrentTrack(artist="", title="", image="", retries=0)
        current.save()

    now_playing = {}

    # try 3 times before clearing the cache
    if current.artist != "" and current.retries < 3:
        now_playing = {
                'artist': current.artist,
                'title': current.title,
                'image': current.image
                }

        current.retries = current.retries + 1
        current.save()
    else:
        current.artist = ""
        current.title = ""
        current.image = ""
        current.save()

    return now_playing

# Mock views
def dummy_get_last_track(request):
    played = {'artist': 'The Album Leaf', 'title': 'Another Day (Revised)'}

    return render_to_response("public/tracks.html", {'played':played});

def dummy_now_playing(request):
    now_playing = { 'artist':'The Album Leaf', 'title': 'Over The Pond', 'image': 'http://userserve-ak.last.fm/serve/_/2857325/The+Album+Leaf+1155442304.jpg'}
            
    return render_to_response("public/now_playing.html", {'now_playing':now_playing});
