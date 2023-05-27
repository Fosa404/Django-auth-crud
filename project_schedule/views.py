from django.http import HttpResponse
from django.shortcuts import render
from .forms import SingupForm

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
            print(request.POST)
            return HttpResponse("usuario creado")
        
        return HttpResponse(form.errors.keys)


