from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = format_suffix_patterns([
    # path('', studentView, name ='index'),
    path('', StudentView.as_view(), name ='index'),
    # path('<int:pk>/', studentDetail, name ='index'),
    path('<int:pk>/', StudentDetail.as_view(), name ='index'),
])
