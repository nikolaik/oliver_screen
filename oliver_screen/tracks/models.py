from django.db import models

# Create your models here.
#
class LastFMSettings(models.Model):
    user = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user
