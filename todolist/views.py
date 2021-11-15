from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def base(request):
    task = Task.objects.all()
    if request.method == "POST":
        name = request.POST["task_name"]
        task = Task.objects.create(
            name=name
        )
        task.save()
        return redirect('/table')
    return render(request, "table.html", {'tasks': task})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/table')

def edit(request, id):
    task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    if request.method == 'POST':
        a = request.POST
        task.name = a["task_name"]
        task.save()
        return redirect('/table')
    return render(request, "table_edit.html", {'task': task, 'tasks': tasks})


