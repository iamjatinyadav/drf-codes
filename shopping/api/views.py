from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.

class ProductListView(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductsSerializers

    @action(detail=False, methods=["GET",], url_path="recent-product")
    def recent_product(self, request):
        recent_post = Product.objects.order_by('-id')[:5]
        serializer = ProductsSerializers(recent_post, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="cheap-product")
    def cheap_product(self,request):
        post = Product.objects.order_by('discount_price')[:6]
        serializer = ProductsSerializers(post, many=True, context = {'request': request})
        return Response(serializer.data)



# class ProductRecentView(generics.ListAPIView):
#     queryset = Product.objects.order_by('-id')[:4]
#     serializer_class = ProductsSerializers


# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsSerializers

class CategoryListView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategorys.objects.all()
    serializer_class = CategorySerializers



