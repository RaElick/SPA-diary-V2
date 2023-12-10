from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import UpdateView, DeleteView
from .forms import RegistrationForm


@login_required
def index(request):
    tasks = Task.objects.filter(author=request.user)
    return render(request, 'main/index.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})


@login_required
def create(request):
    error=''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.author = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')
        else:
            error='Введите корректные данные!'

    form = TaskForm()

    return render(request, 'main/create.html', locals())



class NoteUpdateView(UpdateView):
    model = Task
    template_name = 'main/create.html'
    fields = ['title', 'task']



class NoteDeleteView(DeleteView):
    model = Task
    template_name = 'main/delete.html'
    success_url = '/'

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Замените 'home' на конкретный маршрут вашего сайта
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

