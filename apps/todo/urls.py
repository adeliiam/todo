from django.urls import path
from .views import *
from apps.todo import views 


urlpatterns = [
    path('todo/list/', views.ToDoListView.as_view(), name='todolist'),
    path('todo/create/', views.ToDoCreateView.as_view(), name='tododcreate'),
    path('todo/update/<int:pk>/', views.ToDoUpdaetView.as_view(), name='todoupdate'),
    path('todo/delete/<int:pk>/', views.ToDoDeleteView.as_view(), name='tododelete')
]
