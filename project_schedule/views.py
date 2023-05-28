from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SingupForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html', {})


def signup(request):

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


