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
from django.contrib.auth import views as auth
 
urlpatterns = [
    path('',views.searchUser),
    path('search-video', views.searchVideo),    
    path('video-player', views.videoPlayer),
    path('check-email/', views.checkEmail),
    path('check-username/', views.checkUsername),
    path('admin/', admin.site.urls),
    path('login/', views.Login),
    path('logout/', views.userLogout, name = 'logout'),
    path('register/', user_view.register, name ='register'),
    # path('edit-profile/', views.editProfile, name ='edit-profile'),
    path('view-profile/', views.viewProfile, name = 'view-profile'),
    # path('add-profile/', views.addProfile, name = 'add-profile'),    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
