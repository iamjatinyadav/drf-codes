from django.urls import path
from .views import student_detail, student_list


urlpatterns = [
    path('', student_list),
    path('<int:pk>/', student_detail),
]
