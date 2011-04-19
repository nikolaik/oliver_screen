from django.db import models

# Create your models here.
#
class LastFMSettings(models.Model):
    apikey = models.CharField(max_length=200)
    apisecret = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user
