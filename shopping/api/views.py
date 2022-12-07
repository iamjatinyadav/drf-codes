from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework import filters
from api.filters import PriceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductListView(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ReadProductsSerializers
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PriceFilter
    search_fields = ['name']
    filterset_fields = ['discount_price']

    ordering_fields = ('discount_price',)



    # def get_queryset(self):
    #     return self.queryset

    # def get_object(self, pk=None):
    #     ids = self.kwargs['pk']
    #     print(ids)
    #     return self.get_queryset().filter(name=ids) 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = ProductsSerializers(instance, context={'request':request})
        # print(serializers.data['category'])
        return Response(serializers.data)
    


    @action(detail=False, methods=["GET",], url_path="recent-product")
    def recent_product(self, request):
        recent_post = Product.objects.order_by('-id')[:5]
        serializer = ReadProductsSerializers(recent_post, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="cheap-product")
    def cheap_product(self,request):
        post = Product.objects.order_by('discount_price')[:6]
        serializer = ReadProductsSerializers(post, many=True, context = {'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=["GET"], url_path="cheap-product/(?P<pk>\d+)")
    def cheap_product_detail(self,request, pk=None):
        id = int(self.kwargs['pk'])
        post = list(Product.objects.order_by('discount_price')[:6].values_list("id", flat=True))
        if id in post:
            post = Product.objects.get(pk=id)
            serializer = ProductsSerializers(post, context = {'request': request})
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)


    @action(detail=False, methods=["GET"], url_path="recent-product/(?P<pk>\d+)")
    def recent_product_detail(self,request, pk=None):
        id = int(self.kwargs['pk'])
        post = list(Product.objects.order_by('-id')[:6].values_list("id", flat=True))
        if id in post:
            post = Product.objects.get(pk=id)
            serializer = ProductsSerializers(post, context = {'request': request})
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)
    




# class ProductRecentView(generics.ListAPIView):
#     queryset = Product.objects.order_by('-id')[:4]
#     serializer_class = ProductsSerializers


# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsSerializers

class CategoryListView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategorys.objects.all()
    serializer_class = CategorySerializers

class ContactPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass

class ContactPostView(ContactPostViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [IsAuthenticated]


class ReviewListPostViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    pass


class ReviewViewSet(ReviewListPostViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NewsletterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsLetterSerializers

class WishlistViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = None


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        username = self.request.user
        queryset=queryset.filter(user__username = username)
        if queryset:
            serializer = WishlistReadSerializers(queryset, many=True, context={'request':request})
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)