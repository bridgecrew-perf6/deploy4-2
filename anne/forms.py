from django import forms
# from .models import Profile
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
      

# class ProfileForm(forms.ModelForm):
#       class Meta:
#           model = Profile
#           fields = {'first_name', 'about', 'website_name', 'phone_no'} 
#           widgets={
#             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. The Weeknd'}),
#             'about':forms.TextInput(attrs={'class':'form-control','placeholder':'describe about yourself'}),
#             'website_name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. pluudo.com'}),
#             'phone_no':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 1234567890'}),
#             }  

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
