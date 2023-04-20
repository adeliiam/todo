from apps.users.views import *
from apps.users import views
from django.urls import path

urlpatterns = [
    path('user/list/', views.UserListView.as_view(), name='userlist'),
    path('user/create/', views.UserCreateView.as_view(), name='usercreate'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(),name='userupdate'), 
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='userdelete')

]
