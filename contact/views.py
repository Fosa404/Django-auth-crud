from django.shortcuts import render
from .models import Contact
from .forms import ContacForm
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

def index(request, letter = None):
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__contains=request.GET.get('search', ''))
    context = {

        'contacts': contacts
    }
    return render (request, 'contact/index.html', context)


def view(request,id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }

    return render(request, 'contact/detail.html', context)


def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
       
       form = ContacForm(instance=contact)
       context = {
           'form': form,
           'id': id
       }
       
       return render(request, 'contact/edit.html', context)
    
    if request.method == 'POST':
        form = ContacForm(request.POST, instance = contact)
        form.save()
        context = {
           'form': form,
           'id': id
       }
        messages.success(request, 'Contacto actualizado correctamente')
        return render(request, 'contact/edit.html', context)
       
    
def create(request):
    if request.method == 'GET':
        form = ContacForm( )
        context = {
            'form': form
        }
        return render(request, 'contact/create.html', context)
    

    if request.method == 'POST':
        form = ContacForm(request.POST)
        if form.is_valid:
            form.save()
        messages.success(request, "Contacto creado satisfactoriamente")
        return redirect("contact")
    

def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')