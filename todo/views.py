from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(title__contains=request.GET.get('search', ''), user=request.user)
        context = {
            
            'todos': todos
        }
        return render(request, 'todo/index.html', context)
    else:
        return redirect('index')

@login_required
def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        
        'todo': todo
    }
    return render(request,'todo/detail.html', context)


@login_required
def edit(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == 'GET':
       form = TodoForm(instance=todo)
       context = {

           'form': form,
           'id': id,
           'todo': todo
       }
       
       return render(request, 'todo/edit.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        form.save()
        messages.success(request, "Tarea modificada con exito con exito")
        context = {

            'form': form,
            'id': id
        }
        return render(request,'todo/edit.html', context)


@login_required
def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {

            'form': form
        }
        return render(request, 'todo/create.html', context)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                new_task = form.save(commit=False)
                new_task.user = request.user
                new_task.save()
                return redirect('todo')
            except ValueError:
                context = {
                    'form': form
                }
                messages.error(request, "Introduzca los datos correctamente")
                return render(request, 'todo/create.html', context)
            


@login_required
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')