from django.urls import path
from .views import index, check, TaskCreate, TaskDetail, TaskUpdate, TaskDelete

urlpatterns = [
    path('', index, name='index_url'),
    path('check/<int:pk>', check, name='check_url'),
    path('create/', TaskCreate.as_view(), name='create_url'),
    path('detail/<int:pk>', TaskDetail.as_view(), name='detail_url'),
    path('detail/<int:pk>/update', TaskUpdate.as_view(), name='update_url'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete_url'),
]
