from rest_framework import serializers
from .models import *


class ProductsSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('id','name', 'original_price', 'discount_price', 'image', 'slug', 'category')



class CategorySerializers(serializers.ModelSerializer):
    product2 = serializers.SerializerMethodField()
    products = ProductsSerializers(read_only=True, many=True)
    class Meta:
        model = ProductCategorys
        fields = ('id', 'name', 'product2', 'products')

    def get_product2(self, obj):
        return obj.products.count()
        # return CategorySerializers(data, many=True).data
        