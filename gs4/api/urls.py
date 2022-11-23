from django.urls import path
from .views import studentView, studentDetail
urlpatterns = [
    path('', studentView, name ='index'),
    path('<int:pk>/', studentDetail, name ='index'),
]
