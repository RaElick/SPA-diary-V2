from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

@login_required
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})


def create(request):
    error=''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Введите корректные данные!'





    form = TaskForm()
    context = {
        'form': form,
        'error':error
    }
    return render(request, 'main/create.html', context)

