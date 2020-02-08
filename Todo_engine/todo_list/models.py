from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    check = models.BooleanField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    position = models.AutoField(unique=True)
