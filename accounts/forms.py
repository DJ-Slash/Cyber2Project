from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Requis. Veuillez renseigner votre email d\'entreprise.')
    #username = forms.CharField(max_length=200, label='Nom d\'entreprise', help_text='Requis. Ce nom constitue votre ID pour les traitements futurs.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')