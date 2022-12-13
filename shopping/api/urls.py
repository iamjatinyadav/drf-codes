from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register("product", ProductListView)
router.register('category', CategoryListView)
router.register('contact', ContactPostView)
router.register('review', ReviewViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('wishlist', WishlistViewSet)
router.register('cart', CartViewSets)
router.register('address', AddressViewSets)
router.register('checkout', CheckoutViewSet)

urlpatterns = [
    # path('product/', ProductListView.as_view()),
    # path('recent/', ProductRecentView.as_view()),
    # path('category/', CategoryListView.as_view()),
    # path('product/<int:pk>/', ProductDetailView.as_view()),
    # path('contact/', ContactPostView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name= 'register'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns+=router.urls