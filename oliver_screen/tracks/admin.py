from oliver_screen.tracks.models import LastFMUser
from django.contrib import admin

class LastFMAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name','active']})
	]

admin.site.register(LastFMUser, LastFMAdmin)
