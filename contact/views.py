from django.shortcuts import render
from .models import Contact
from .forms import ContacForm
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request, letter = None):
    if request.user.is_authenticated:
        if letter != None: # busca contacto por inicial
            contacts = Contact.objects.filter(name__istartswith=letter, user=request.user)
        else:
            #busca contacto por barra de busqueda. Si no hay valor en form de búsqueda obtiene todos los contactos de user
            contacts = Contact.objects.filter(name__contains=request.GET.get('search', ''), user=request.user)
        context = {

            'contacts': contacts
        }
        return render (request, 'contact/index.html', context)
    return redirect('index') # si user no autenticado rediraccionar a "/"

@login_required
def view(request,id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }

    return render(request, 'contact/detail.html', context)

@login_required
def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
       #renderizar form de edición con datos del contacto
       form = ContacForm(instance=contact)
       context = {
           'form': form,
           'id': id
       }
       
       return render(request, 'contact/edit.html', context)
    
    if request.method == 'POST': # actualiza contacto con datos nuevos
        form = ContacForm(request.POST, instance = contact)
        form.save()
        context = {
           'form': form,
           'id': id
       }
        messages.success(request, 'Contacto actualizado correctamente')
        return render(request, 'contact/edit.html', context)
       
@login_required  
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
            try:
                new_contact = form.save(commit=False)
                new_contact.user = request.user #asignar usuario logueado al nuevo contacto antes del commit
                new_contact.save()
                return redirect("contact")
            except ValueError:
                messages.error(request, "Introduzca los datos correctamente")
                context = {
                    'form': form
                }
                return render(request, 'contact/create.html', context)
        
    
@login_required
def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')