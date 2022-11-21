from django.urls import path
from .views import student_create
urlpatterns = [
    path('', student_create),
]
