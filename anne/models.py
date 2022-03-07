from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

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


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=300)
    about = models.CharField(max_length=300)
    website_name = models.CharField(max_length = 200)   

    def __str__(self):
        return str(self.user) 

class Cluster(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    cluster_name = models.CharField(max_length=200)
    cluster_desc = models.CharField(max_length=200)
    cluster_hashtags = models.CharField(max_length=100)

    def __str__(self):
        return self.cluster_name    

class ClusterVideos(models.Model):
    cluster = models.ForeignKey(Cluster,on_delete=models.CASCADE)
    cluster_video = EmbedVideoField()

    def __str__(self):
        return self.cluster_video   