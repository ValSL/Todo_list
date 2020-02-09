from django.shortcuts import render, redirect, reverse
from .models import Task
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TodoForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list/index.html', context={'tasks': tasks})


class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'content']
    success_url = 'todo/index'
    template_name = 'todo_list/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        return context


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
