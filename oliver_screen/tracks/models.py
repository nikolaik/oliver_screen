from django.db import models

# Create your models here.
#
class LastFMUser(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField()

    def __unicode__(self):
        if self.active:
            return self.name + ": active"
        return self.name + ": NOT active"

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    videoId = models.CharField(max_length=200)
    start = models.IntegerField()
    active = models.BooleanField()

    def __unicode__(self):
        if self.active:
            return self.artist + " - " + self.title + ": active"
        return self.artist +" - " + self.title + " : NOT active"


# TODO: cache current track. avoids overwriting video-iframe if the song is still the same.
