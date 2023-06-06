from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SingupForm, SigninForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {})
    else:
        #si el usuario no está auth redirecionar a signin
        return redirect('signin')

def signup(request):
    #vista para crear cuenta
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET': # si se solicita la vista mostrar formulario signin
            form = SingupForm()
            context = {
                'form': form
            }
            return render(request, 'signup.html', context )
        else:
            form = SingupForm(request.POST) #method POST:
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('index')  #si el form es valido crea usuario y redirecciona a index "/"
            else:
                return render(request, 'signup.html', {"form": form}) #si no es valido vuelve a cargar el form signup


def signin(request):
    #vista para inicio de sesion
    if request.user.is_authenticated:#user autenticado redirecciona a "/"
        return redirect('index')
    else:
        if request.method == 'GET':  #solicita la vista muestra form signin
            context = {
            
                'form': SigninForm
            }
            return render(request, 'signin.html', context)
        else:
            form = SigninForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password) #compruba usuario
            if user is not None:
                #usuario existe
                login(request, user)
                return redirect('index')
            else:
                #usuario NO existe muestra la vista form signin
                context = {
                    'form': form
                }
                messages.error(request, "usuario o contraseña incorrectos")
                return render(request, 'signin.html', context)
            
def signout(request):
    #vista para deslogueo
    logout(request)
    return redirect('signin')