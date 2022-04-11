from django import forms
from .models import Profile, Cluster, Video
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class SearchVideoForm(forms.Form):
    desc = forms.CharField(label=False, max_length=100, widget=forms.TextInput(attrs={'placeholder':'Search videos, cluster'}))

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

class ProfileForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = {'image','about', 'website_name', 'country'} 
          widgets={
            'about':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter About'}),
            'website_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Website'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Country'}),
           }

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
   

class ClusterForm(forms.ModelForm):
    class Meta:
       model = Cluster
       fields = {'cluster_name', 'cluster_desc', 'cluster_hashtags'} 
       widgets={
            'cluster_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'cluster_desc':forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'cluster_hashtags':forms.TextInput(attrs={'class':'form-control','placeholder':'Hashtags'}),
           }

# class AddItemForm(forms.Form):
#     cluster_id = forms.CharField(max_length=10)
#     item_url = forms.CharField(label='Title',max_length=400)
  

class AddVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = {'video_owner_thumbnail', 'video_description', 'video_platform_id','video_url', 'video_title', 'video_thumbnail', 'video_owner'}


class DeleteVideoForm(forms.Form):
    videos = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)