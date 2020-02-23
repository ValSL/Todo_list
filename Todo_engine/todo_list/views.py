from django.shortcuts import render, redirect, reverse
from .models import Task
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TodoForm


def index(request):
    tasks = Task.objects.order_by('position')
    return render(request, 'todo_list/index.html', context={'tasks': tasks})
 

def ordered_index(request, color):
    ordered_tasks = Task.objects.filter(priority=color)
    other_tasks = Task.objects.exclude(priority=color)
    return render(request, 'todo_list/ordered_index.html', context={'tasks': other_tasks, 'ordered_tasks': ordered_tasks})


def check(request, pk):
    current_task = Task.objects.get(id=pk)
    current_task.check = not current_task.check
    current_task.save()
    return redirect(reverse('index_url'))


def change_priority(request, pk):
    if request.method == 'POST':
        current_task = Task.objects.get(id=pk)
        form = TodoForm(request.POST, instance=current_task)
        current_task.priority = form['priority'].data
        current_task.save()
        return redirect(reverse('detail_url', kwargs={'pk': current_task.pk}))


class TaskCreate(CreateView):
    model = Task
    success_url = '/'
    template_name = 'todo_list/create.html'
    form_class = TodoForm


class TaskDetail(DetailView):
    template_name = 'todo_list/detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        return context


class TaskUpdate(UpdateView):
    template_name = 'todo_list/update.html'
    model = Task
    success_url = '/'
    form_class = TodoForm


class TaskDelete(DeleteView):
    template_name = 'todo_list/delete.html'
    model = Task
    success_url = '/'
