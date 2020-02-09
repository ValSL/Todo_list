from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView, CreateView
from .forms import Todo


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list/index.html', context={'tasks': tasks})


class Tasks(CreateView):
    model = Task
    fields = ['title', 'content']
    success_url = reverse_lazy('index_url')
    template_name = 'todo_list/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Todo()
        return context
