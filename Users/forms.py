from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Name', required=False)
    last_name = forms.CharField(label='Lastname', required=False) 
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1', 'password2']
        help_texts = {k:"" for k in fields}



class AvatarForm(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['avatar']


class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Messages
        fields = ['receiver','msg',]
        widgets = {'msg': forms.Textarea(attrs={'cols': 80})}  # widget para agrandar el TextField a 80 columnas