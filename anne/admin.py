from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import CustomUser, SiteDesc, Profile, Cluster, Video

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# admin.site.register(Item, MyModelAdmin)
admin.site.register(SiteDesc)
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Cluster)
admin.site.register(Video)
