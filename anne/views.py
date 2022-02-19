from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SearchVideoForm
from anne import models

from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://kudos02.pythonanywhere.com/login/')
def searchUser(request):
    authform = AuthenticationForm()
    regform = UserRegisterForm()
    form = SearchVideoForm()
    obj = models.Item.objects.all()
    print(obj)
    site_d = models.SiteDesc.objects.all()
    return render(request,'anne/index.html', {'obj':obj, 'site_des':set(site_d), 'form': form, 'regform' : regform, 'authform' : authform})


def videoPlayer(request):
    obj = models.Item.objects.all()
    video_id = request.GET['video_id']
    video = models.Item.objects.get(id=video_id)
    return render(request, 'anne/video_player.html', {'obj':obj, 'my_video':video})

def searchVideo(request):
    if request.method=='POST':
        form = SearchVideoForm(request.POST)
        desc = form.data['desc']
        items = models.Item.objects.filter(desc=desc)
        res = render(request,'anne/search_video.html',{'form':form,'items':items})
        return res


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            ##################################################################
            messages = 'Your account has been created ! You are now able to log in'
            return render(request, 'anne/profile.html', {'msg':messages})
    else:
        form = UserRegisterForm()
    return render(request, 'anne/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return render(request, 'anne/profile.html',)
        else:
            messages = 'Your account has been created ! You are now to logged in'
            return render(request, 'anne/profile.html', {'msg':messages})
    form = AuthenticationForm()
    return render(request, 'anne/login.html', {'form':form, 'title':'log in'})        
