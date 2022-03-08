from django import forms
from .models import Profile, Cluster
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class SearchVideoForm(forms.Form):
    desc = forms.CharField(label='Title',max_length=100)
    

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

class ProfileForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = {'about', 'website_name', 'country'} 
           

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


class AddItemForm(forms.Form):
    cluster_id = forms.CharField(max_length=10)
    item_url = forms.CharField(label='Title',max_length=400)
  