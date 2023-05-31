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
        return redirect('signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            form = SingupForm()
            context = {
                'form': form
            }
            return render(request, 'signup.html', context )
        else:
            form = SingupForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'signup.html', {"form": form})


def signin(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'GET':
            context = {
            
                'form': SigninForm
            }
            return render(request, 'signin.html', context)
        else:
            form = SigninForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'form': form
                }
                messages.error(request, "usuario o contraseña incorrectos")
                return render(request, 'signin.html', context)
            
def signout(request):
    logout(request)
    return redirect('signin')