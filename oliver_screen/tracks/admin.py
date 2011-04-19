from oliver_screen.tracks.models import LastFMSettings
from django.contrib import admin

class LastFMAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['user']})
	]

admin.site.register(LastFMSettings, LastFMAdmin)
