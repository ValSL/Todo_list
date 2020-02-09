from django.shortcuts import render, redirect, reverse
from .models import Task
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TodoForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list/index.html', context={'tasks': tasks})


def check(request, pk):
    current_task = Task.objects.get(id=pk)
    current_task.check = not current_task.check
    current_task.save()
    return redirect(reverse('index_url'))


class TaskCreate(CreateView):
    model = Task
    success_url = '/todo'
    template_name = 'todo_list/create.html'
    form_class = TodoForm


class TaskDetail(DetailView):
    template_name = 'todo_list/detail.html'
    model = Task


class TaskUpdate(UpdateView):
    template_name = 'todo_list/update.html'
    model = Task
    success_url = '/todo'
    form_class = TodoForm


class TaskDelete(DeleteView):
    template_name = 'todo_list/delete.html'
    model = Task
    success_url = '/todo'
