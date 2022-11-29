from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("product", ProductListView)
urlpatterns = [
    # path('product/', ProductListView.as_view()),
    path('recent/', ProductRecentView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]

urlpatterns+=router.urls