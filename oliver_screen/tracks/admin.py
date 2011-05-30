from oliver_screen.tracks.models import LastFMUser, YouTubeVideo
from django.contrib import admin

class LastFMAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name','active']})
	]

class VideoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['artist', 'title', 'videoId', 'start', 'active']})
	]

admin.site.register(LastFMUser, LastFMAdmin)
admin.site.register(YouTubeVideo, VideoAdmin)
