from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.routers import DefaultRouter

student_list = StudentViewSet.as_view({
    'get':'list',
    'post': 'create',
})
student_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy',

})
user_list = UserViewSet.as_view({
    'get': 'list',
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename="student")
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [
    
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns([
    # # path('', studentView, name ='index'),
    # path('student/', StudentView.as_view(), name ='student-list'),
    # # path('<int:pk>/', studentDetail, name ='index'),
    # path('student/<int:pk>/', StudentDetail.as_view(), name ='student-detail'),
    # path('users/', UserListView.as_view(), name = 'user-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # path('', api_root),


# ])
