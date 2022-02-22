from django import forms
from .models import Profile

class SearchVideoForm(forms.Form):
    desc = forms.CharField(label='Title',max_length=100)
    

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
      

class ProfileForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = {'first_name', 'about', 'website_name', 'phone_no'}    