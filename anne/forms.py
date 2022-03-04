from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class SearchVideoForm(forms.Form):
    desc = forms.CharField(label='Title',max_length=100)
    

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
      

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
   