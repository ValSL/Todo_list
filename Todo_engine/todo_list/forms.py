from django import forms
from .models import Task


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Название')
    content = forms.CharField(label='Содержание', widget=forms.widgets.Textarea())
    priority = forms.ChoiceField(label='Приоритет', widget=forms.widgets.Select(), choices=Task.colors)

    class Meta:
        model = Task
        fields = ['title', 'content', 'priority']
