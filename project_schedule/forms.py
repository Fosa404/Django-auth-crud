from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re

class SingupForm(UserCreationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput ,label="Nombre de usuario", help_text="max 10 caracteres")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña", help_text="min 8 caracteres")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user.count():
            raise ValidationError("El nombre de usuario ya existe")
        return username
        
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("las contraseñas no coinciden")
        
        elif re.search(r'[A-Z]', password1) is None: #comprueba mayúsculas
            raise ValidationError("La contraseña debe contener al menos 1 mayus")
        
        elif re.search(r'[0-9]', password1) is None: #comprueba números 
            raise ValidationError("La contraseña debe contener al menos 1 número")
        
        return password2
    

class SigninForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
        
