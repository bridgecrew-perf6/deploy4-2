import json
from django.http import JsonResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SearchVideoForm #, ProfileForm
from anne import models

from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, RegisterForm, ProfileForm, ClusterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def checkUsername(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')

        u_bool = True
        users = models.CustomUser.objects.all()
        emails = []
        usernames = []
        
        for i in users:
            if username == i.username :
                u_bool = False

        if u_bool:
            print(form) 
            form.save()       
            request.session['session_username'] = username
            return JsonResponse({"status":"username not registered"})   

        else:
            return JsonResponse({"status":"username registered"})        

def Login(request):
    if request.method == 'POST':
        print("inside login function")
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        try:
            user = authenticate(request, username = email, password = password)
        except:
            return JsonResponse({'status':'Invalid credentials'})
        if user is not None:
            print("inside login function user exists")
            login(request, user)
            request.session['session_username'] = user.username
            return JsonResponse({'status':'User Login Success'})
        else:
            print("inside login function user not exists")
            return JsonResponse({'status':'Invaid Credentials'})                   

def checkEmail(request):
    if request.method == 'POST':
        email_entered = request.POST.get('email_entered')
        print("inside check_email")
        print(email_entered)
        print(email_entered)
        e_bool = True
        users = models.CustomUser.objects.all()
        emails = []
        usernames = []
        for i in users:
            if email_entered == i.email :
                e_bool = False
        if e_bool:        
            return JsonResponse({"status":"email not registered"})    
        else:
            return JsonResponse({"status":"email registered"})        

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://kudos02.pythonanywhere.com/')

def searchUser(request):
    form = SearchVideoForm()
    authform = LoginForm()
    registerform = RegisterForm()
    obj = models.Item.objects.all()
    print(obj)
    site_d = models.SiteDesc.objects.all()
    #return render(request,'anne/index.html', {'authform':authform, 'registerform':registerform,'obj':obj, 'site_des':set(site_d), 'form': form})
    return render(request,'anne/index.html', {'authform':authform, 'registerform':registerform, 'obj':obj, 'form': form})


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
        print("yes entering to register function")
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            print("form not valid")
            form.save()
            ##################################################################
            username = request.POST['username']
            request.session['session_username'] = username
            return render(request, 'anne/profile.html', {'username':username})
    else:
        print("not entering to register function")
        form = RegisterForm()
        return render(request, 'anne/register.html', {'form': form, 'title':'register here'})


def addProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        print(form)
        if form.is_valid():
            profile = models.Profile()
            username = request.session['session_username']
            user = models.CustomUser.objects.get(username=username)
            profile.user = user
            profile.about = form.data['about']
            profile.website_name = form.data['website_name']
            profile.save()
            request.session['sess_id'] = profile.id
            return render(request,'anne/profile.html',{'profile':profile, 'profile_form':form, 'cluster_form':ClusterForm})

# @login_required(login_url='http://kudos02.pythonanywhere.com/login/')
def editProfile(request):
    if request.method == 'POST':
        print("aman")
        if 'sess_id' in request.session:
            sess_id = request.session['sess_id']
            profile = models.Profile.objects.get(id = sess_id)
            form = ProfileForm(request.POST or None, instance=profile)
            form.save()
            return render(request,'anne/profile.html',{'profile':profile, 'profile_form':form, 'cluster_form':ClusterForm})

def viewProfile(request):
        print("aman")
        clusters = models.Cluster.objects.all()
        if 'sess_id' in request.session: 
            sess_id = request.session['sess_id']
            profile = models.Profile.objects.get(id = sess_id)
            profile_form = ProfileForm(request.POST or None, instance=profile)
            clusters = models.Cluster.objects.all()
        else:
            profile_form = ProfileForm()
        return render(request,'anne/profile.html', {'profile_form':profile_form, 'cluster_form':ClusterForm, 'clusters':clusters})

def addCluster(request):
    if request.method == 'POST':
        form = ClusterForm(request.POST or None)
        print("inside addCluster")
        print("inside form is valid")
        cluster = models.Cluster()
        cluster.cluster_name = form.data['cluster_name']
        profile = models.Profile.objects.get(id=request.session['sess_id']) 
        cluster.profile = profile
        cluster.save()
        clusters = models.Cluster.objects.all()
        return render(request,'anne/profile.html',{'profile':profile, 'profile_form':form, 'cluster_form':ClusterForm, 'clusters':clusters})

def cluster(request):
    cluster_id = request.GET['cluster_id']
    cluster = models.Cluster.objects.get(id = cluster_id)
    
    cluster_form = ClusterForm(request.POST or None, instance=cluster)
    return render(request, 'anne/cluster.html', {'cluster_form':cluster_form, 'cluster':cluster})