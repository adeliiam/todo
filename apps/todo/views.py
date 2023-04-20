from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import ToDo
from utils.permissions import IsOwner
# Create your views here.


class ToDoListView(generics.ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
    filterset_fields = ['is_completed']
    permission_classes=[IsOwner]


class ToDoCreateView(generics.CreateAPIView):
        queryset=ToDo.objects.all()
        serializer_class=ToDoSerializer
        permission_classes=[AllowAny ]

class ToDoUpdaetView(generics.UpdateAPIView):
        queryset=ToDo.objects.all()
        serializer_class=ToDoSerializer
        permission_classes=[IsOwner]

class ToDoDeleteView(generics.DestroyAPIView):
        queryset=ToDo.objects.all()
        serializer_class=ToDoSerializer
        permission_classes=[IsOwner]
    

