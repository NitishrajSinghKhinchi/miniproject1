from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['name','email','address']
        labels = {'email': 'Email','name':'Username','address':'Address'}

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model = CustomUser
        fields = ['name','email','address']
        labels = {'email': 'Email','name':'Username','address':'Address'}
