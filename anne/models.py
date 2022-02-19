from django.db import models

# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    desc = models.CharField(max_length=200, default='SOME STRING')
    added = models.DateTimeField(auto_now_add=True, null = True)

    class Meta:
        ordering = ['-added']

    def __str__(self):
        return str(self.desc)


class SiteDesc(models.Model):
    site_desc = models.CharField(max_length=200, default='SOME STRING')