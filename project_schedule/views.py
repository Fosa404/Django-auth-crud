from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html', {})


def signup(request):
    context = {
        
        'form':UserCreationForm
        
        }
    return render(request, 'signup.html', context )

