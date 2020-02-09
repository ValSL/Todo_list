from django import forms
from django.forms import widgets
from .models import Task


class Todo(forms.ModelForm):
    title = forms.CharField(label='Название')
    content = forms.CharField(label='Содержание', widget=forms.widgets.Textarea())

    class Meta:
        model = Task
        fields = ['title', 'content']


