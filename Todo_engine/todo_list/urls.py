from django.urls import path
from .views import index, ordered_index, check, change_priority, TaskCreate, TaskDetail, TaskUpdate, TaskDelete

urlpatterns = [
    path('', index, name='index_url'),
    path('ordered/<str:color>', ordered_index, name='ordered_index_url'),
    path('check/<int:pk>', check, name='check_url'),
    path('prior/<int:pk>', change_priority, name='prior_url'),
    # path('pos/<int:pk>', change_position, name='change_position_url'),
    path('create/', TaskCreate.as_view(), name='create_url'),
    path('detail/<int:pk>', TaskDetail.as_view(), name='detail_url'),
    path('item/<int:pk>/update', TaskUpdate.as_view(), name='update_url'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete_url'),
]
