from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class SingupForm(UserCreationForm):
    username = forms.CharField(max_length=10, label="Nombre de usuario", widget=forms.TextInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    def clean_username(self):
        username = self.cleaned_data['username']