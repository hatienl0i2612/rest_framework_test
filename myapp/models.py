from django.db import models


# Create your models here.
class key(models.Model):
    time = models.DateTimeField(auto_now=True)
    site = models.CharField(max_length=255, blank=False)
    key = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=False)
    user_created = models.CharField(max_length=255, blank=False)

    def __unicode__(self):
        return self.key
