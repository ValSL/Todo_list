from django.db import models


class Task(models.Model):
    colors = (('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green'))
    title = models.CharField(max_length=100)
    check = models.BooleanField(default=False)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices=colors, default='red')
