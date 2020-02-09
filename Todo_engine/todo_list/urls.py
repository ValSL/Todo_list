from django.contrib import admin
from django.urls import path
from .views import index, Tasks

urlpatterns = [
    path('', index, name='index_url'),
    path('create/', Tasks.as_view(), name='create_url'),
]
