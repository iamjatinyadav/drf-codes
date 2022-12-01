from rest_framework import serializers
from .models import *

class ReadProductsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    products = ReadProductsSerializers(read_only=True, many=True)
    class Meta:
        model = ProductCategorys
        fields = ('id', 'name', 'product_count', 'products')

    def get_product_count(self, obj):
        return obj.products.count()


class ProductsSerializers(serializers.ModelSerializer):
    # category = CategorySerializers(read_only=True)
    related_products = serializers.SerializerMethodField()
    # category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id','name', 'original_price', 'discount_price', 'image', 'slug', 'category', 'related_products')

    def get_related_products(self, obj):
        var = obj.category.get_all_product.exclude(id = obj.id)

        return ReadProductsSerializers(var, many=True, context=self.context).data

    def get_category_name(self, obj):
        return obj.category.name





        # return CategorySerializers(data, many=True).data
        