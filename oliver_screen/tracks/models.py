from django.db import models

# Create your models here.
#
class LastFMUser(models.Model):
    name = models.CharField(max_length=200)
    ACTIVE_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    active = models.CharField(choices=ACTIVE_CHOICES, max_length=3)

    def __unicode__(self):
        if self.active == "yes":
            return self.name + ": active"
        return self.name + ": NOT active"
