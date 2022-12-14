from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework import filters
from api.filters import PriceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
# Create your views here.

class ProductListView(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ReadProductsSerializers
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PriceFilter
    search_fields = ['name']
    filterset_fields = ['discount_price',]

    ordering_fields = ('discount_price','id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductsSerializers
        # if self.action == 'recent_product':
        #     recent_post = Product.objects.order_by('-id')[:5]
        #     serializer= self.serializer_class(recent_post, many=True, context={'request': request})
        #     return Response(serializer.data)

        return self.serializer_class

    # def get_queryset(self):
    #     queryset = Product.objects.all()[:5]





    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializers = ProductsSerializers(instance, context={'request':request})
    #     # print(serializers.data['category'])
    #     return Response(serializers.data)
    

    # @action(detail=False, methods=["GET",], url_path="recent-product")
    # def recent_product(self, request):
    #     recent_post = Product.objects.order_by('-id')[:5]
    #     serializer = ReadProductsSerializers(recent_post, many=True, context={'request': request})
    #     return Response(serializer.data)


    # @action(detail=False, methods=["GET"], url_path="cheap-product")
    # def cheap_product(self,request):
    #     post = Product.objects.order_by('discount_price')[:6]
    #     serializer = ReadProductsSerializers(post, many=True, context = {'request': request})
    #     return Response(serializer.data)
    

    # @action(detail=False, methods=["GET"], url_path="cheap-product/(?P<pk>\d+)")
    # def cheap_product_detail(self,request, pk=None):
    #     id = int(self.kwargs['pk'])
    #     post = list(Product.objects.order_by('discount_price')[:6].values_list("id", flat=True))
    #     if id in post:
    #         post = Product.objects.get(pk=id)
    #         serializer = ProductsSerializers(post, context = {'request': request})
    #         return Response(serializer.data)
    #     else:
    #         return Response(status=HTTP_404_NOT_FOUND)


    # @action(detail=False, methods=["GET"], url_path="recent-product/(?P<pk>\d+)")
    # def recent_product_detail(self,request, pk=None):
    #     id = int(self.kwargs['pk'])
    #     post = list(Product.objects.order_by('-id')[:6].values_list("id", flat=True))
    #     if id in post:
    #         post = Product.objects.get(pk=id)
    #         serializer = ProductsSerializers(post, context = {'request': request})
    #         return Response(serializer.data)
    #     else:
    #         return Response(status=HTTP_404_NOT_FOUND)
    


class CategoryListView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategorys.objects.all()
    serializer_class = CategorySerializers


class ContactPostView(mixins.CreateModelMixin, viewsets.GenericViewSet):
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


class CartViewSets(viewsets.ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializers
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        username = self.request.user.id
        queryset=queryset.filter(cart= username)
        if queryset:
            serializer = self.get_serializer(queryset, many=True, context={'request':request})
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cartitem = CartItems.objects.filter(product = serializer.validated_data['product'])
        if cartitem:
            for i in cartitem:
                i.count += serializer.validated_data['count']
                i.save()
        else:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer):
        cart = Cart.objects.get(user = self.request.user)
        serializer.save(cart=cart)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CartItemsRetriveSerializers(instance,context={'request':request})
        return Response(serializer.data)
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class AddressViewSets(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers
    permission_classes = [IsAuthenticated]



    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        username = self.request.user.id
        queryset=queryset.filter(user= username)
        if queryset:
            serializer = AddressReadSerializers(queryset, many=True, context={'request':request})
            return Response(serializer.data)
        else:
            return Response(status=HTTP_404_NOT_FOUND)



class CheckoutViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None




@api_view(['GET'])
def last_five(request):

    if request.method == 'GET':
        queryset = Product.objects.order_by("-id")[:5]
        Data = []
        for i in queryset:
            Data.append(i.detail())
        return Response(Data)
        # serializer = UniqueSerializer(queryset, many=True)

        # return Response(serializer.data)

