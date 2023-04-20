from django.shortcuts import render
from rest_framework import generics
from apps.users.serializers import UserSerializer
from apps.users.models import NewUser
from rest_framework.permissions import IsAdminUser, AllowAny
from utils.permissions import IsCurrentUser

class UserListView(generics.ListAPIView):
    queryset=NewUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAdminUser ]


class UserCreateView(generics.CreateAPIView):
    queryset=NewUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class UserUpdateView(generics.UpdateAPIView):
    queryset=NewUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsCurrentUser]


class UserDeleteView(generics.DestroyAPIView):
    queryset=NewUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsCurrentUser]

# Create your views here.
