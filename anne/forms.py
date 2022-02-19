from django import forms

class SearchVideoForm(forms.Form):
    desc = forms.CharField(label = "", max_length=200, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search video, cluster'}))

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
      