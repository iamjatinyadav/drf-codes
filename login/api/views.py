from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from .models import *

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    print(queryset)
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
