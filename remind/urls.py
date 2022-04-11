"""remind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from anne import views
from django.conf import settings
from django.conf.urls.static import static
from anne import views as user_view
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('',views.searchUser),
    path('search-video', views.searchVideo),    
    path('video-player', views.videoPlayer),
    path('check-email/', views.checkEmail),
    path('check-username/', views.checkUsername),
    path('admin/', admin.site.urls),
    path('delete-user/', views.deleteUser),
    path('login/', views.Login),
    path('delete-cluster', views.deleteCluster),
    path('logout/', views.userLogout, name = 'logout'),
    path('register/', user_view.register, name ='register'),
    path('edit-profile/', views.editProfile, name ='edit-profile'),
    path('view-public-profile/', views.viewPublicProfile, name = 'view-public-profile'),
    path('view-profile/', views.viewProfile, name = 'view-profile'),
    path('view-profile-arrange-clusters/', views.viewProfileArrangeClusters, name = 'view-profile-arrange-cluster'),
    path('add-profile/', views.addProfile, name = 'add-profile'), 
    path('add-cluster/', views.addCluster, name = 'add-cluster'),   
    path('cluster/', views.cluster, name = 'cluster'),  
    path('delete_videos/', views.deleteVideos, name = 'delete_videos'),  
    path('share_video/', views.shareVideo, name = 'share_video'),  
    # path('add-item/', views.addItem, name = 'add-item'), 
    path('add-video/', views.addVideo, name = 'add-video'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="anne/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="anne/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="anne/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="anne/password_reset_done.html"), 
        name="password_reset_complete"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
