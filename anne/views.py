import json
from django.http import JsonResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SearchVideoForm #, ProfileForm
from anne import models

from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, RegisterForm
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
    users = models.CustomUser.objects.all()
    emails = []
    usernames = []
    for i in users:
        print(i.email)
        emails.append(i.email)
        usernames.append(i.username)
    form = SearchVideoForm()
    authform = LoginForm()
    registerform = RegisterForm()
    obj = models.Item.objects.all()
    print(obj)
    site_d = models.SiteDesc.objects.all()
    #return render(request,'anne/index.html', {'authform':authform, 'registerform':registerform,'obj':obj, 'site_des':set(site_d), 'form': form})
    return render(request,'anne/index.html', {'authform':authform, 'registerform':registerform,'usernames':usernames,'emails':emails, 'obj':obj, 'site_des':set(site_d), 'form': form})


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
  

# def Login(request):
#     if request.method == 'POST':
        
#         # AuthenticationForm_can_also_be_used__
        
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username)
#         print(password)
#         user = authenticate(request, username = username, password = password)
#         print(user)
#         if user:
#             if 'session_username' not in request.session:
#                 request.session['session_username'] = username
#             return render(request, 'anne/profile.html')   
#         else:
#             form = LoginForm()
#             messages = "Either username or password is incorrect....TRY AGAIN !!!"
#             res = render(request,'anne/login.html',{'form':form,'messages':messages})
#             return res    
#     form = LoginForm()
#     users = models.CustomUser.objects.all()
#     emails = []
#     usernames = []
#     for i in users:
#         print(i.email)
#         emails.append(i.email)
#         emails.append(i.username)
#     return render(request, 'anne/login.html', {'form':form, 'emails':emails, 'usernames':usernames})




# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             ##################################################################
#             messages = 'Your account has been created ! You are now able to log in'
#             username = request.POST['username']
#             form_ = ProfileForm()
#             form_.data['user'] = username
#             return render(request, 'anne/profile.html', {'msg':messages, 'form':form_, 'username':username})
#     else:
#         form = UserRegisterForm()
#     return render(request, 'anne/register.html', {'form': form, 'title':'reqister here'})
  
# ################ login forms ###################################################
# def Login(request):
#     if request.method == 'POST':
  
#         # AuthenticationForm_can_also_be_used__
  
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username)
#         print(password)
#         user = authenticate(request, username = username, password = password)
#         print(user)
#         if user:
#             login(request, user)
#             try:
#                 profile = models.Profile.objects.get(user=user)
#             except:
#                 profile = False
#                 form = ProfileForm
#                 return render(request, 'anne/profile.html',{'profile':profile, 'form':form, 'username':username})
#             request.session['sess_id'] = profile.id
#             if 'sess_id' in request.session:
#                 sess_id = request.session['sess_id']
#             fields = {'id':profile.id,'about':profile.about,'first_name':profile.first_name,'website_name':profile.website_name, 'phone_no':profile.phone_no}
#             form = ProfileForm(initial=fields)
#             return render(request, 'anne/profile.html',{'profile':profile, 'form':form})   
#         else:
#             form = AuthenticationForm()
#             messages = "Either username or password is incorrect....TRY AGAIN !!!"
#             res = render(request,'anne/index.html',{'authform':form,'messages':messages})
#             return res    
#     form = AuthenticationForm()
#     return render(request, 'anne/login.html', {'form':form, 'title':'log in'})


# def addProfile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST or None)
#         print(form)
#         if form.is_valid():
#             profile = models.Profile()
#             username = request.GET['username']
#             user = models.User.objects.get(username=username)
#             profile.user = user
#             profile.first_name = form.data['first_name']
#             profile.about = form.data['about']
#             profile.website_name = form.data['website_name']
#             profile.phone_no = form.data['phone_no']
#             profile.save()
#             request.session['sess_id'] = profile.id
#             return render(request,'anne/profile.html',{'profile':profile, 'form':form})

# @login_required(login_url='http://localhost:8000/login/')
# def editProfile(request):
#     if request.method == 'POST':
#         print("aman")
#         if 'sess_id' in request.session:
#             sess_id = request.session['sess_id']
#             profile = models.Profile.objects.get(id = sess_id)
#             form = ProfileForm(request.POST or None, instance=profile)
#             form.save()
#             return render(request,'anne/profile.html',{'profile':profile, 'form':form})

def viewProfile(request):
            print("aman")
            # sess_id = request.session['sess_id']
            # profile = models.Profile.objects.get(id = sess_id)
            # form = ProfileForm(request.POST or None, instance=profile)

            return render(request,'anne/profile.html')
                      