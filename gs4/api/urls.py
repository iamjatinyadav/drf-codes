from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = format_suffix_patterns([
    # path('', studentView, name ='index'),
    path('student/', StudentView.as_view(), name ='student-list'),
    # path('<int:pk>/', studentDetail, name ='index'),
    path('student/<int:pk>/', StudentDetail.as_view(), name ='student-detail'),
    path('users/', UserListView.as_view(), name = 'user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', api_root),
])
