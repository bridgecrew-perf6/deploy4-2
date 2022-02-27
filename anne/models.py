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


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     id = models.AutoField(primary_key=True)
#     about = models.CharField(max_length=300)
#     phone_no = models.IntegerField()
#     first_name = models.CharField(max_length = 50)
#     website_name = models.CharField(max_length = 200)    