from django import forms
from .models import Task


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Название')
    content = forms.CharField(label='Содержание', widget=forms.widgets.Textarea())

    class Meta:
        model = Task
        fields = ['title', 'content']
