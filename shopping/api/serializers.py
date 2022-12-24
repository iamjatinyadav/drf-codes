from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator


class ReadProductsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ('id','url', 'name','original_price','discount_price','image', 'slug', 'category','created', 'modified')

    def get_product_count(self, obj):
        return obj.products.count()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(style={'input_type': 'password'},write_only=True, required=True )
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password field didn't match"})
        return attrs

    def create(self, vaildate_data):
        user = User.objects.create(username=vaildate_data['username'], email=vaildate_data['email'])
        user.set_password(vaildate_data['password'])
        user.is_active = True
        user.save()
        return user



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
    category_name = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    related_review = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'original_price', 'discount_price', 'image', 'slug', 'category_name', 
        'review_count', 'related_products', 'related_review')

    def get_related_products(self, obj):
        var = obj.category.get_all_product.exclude(id = obj.id)

        return ReadProductsSerializers(var, many=True, context=self.context).data

    def get_related_review(self, obj):
        return ReviewShowSerializers(obj.get_product_review.all(), many=True, context = self.context).data

    def get_category_name(self, obj):
        return obj.category.name

    def get_review_count(self, obj):
        return obj.reviews.count()


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'subject', 'message')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'product', 'name', 'email', 'review', 'rating', 'created')


class ReviewShowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'review', 'rating', 'created')


class NewsLetterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'email')


class WishlistSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = WishList
        fields = ('id','user', 'product')

    def validate(self,attrs):
            log_user_id = self.context['request'].user.id
            if WishList.objects.filter(user_id = log_user_id) and WishList.objects.filter(product= attrs['product']):
                raise serializers.ValidationError({'product': "Product already in your wishlist"})
            return attrs


class WishlistReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'product')
        depth = 1


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemsSerializers(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CartItems
        fields = ('id', 'cart', 'product', 'count')


class CartItemsRetriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ('id', 'product', 'count')
        depth = 1


class AddressSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Address
        fields = "__all__"


class AddressReadSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Address
        fields = "__all__"


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"


class UniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
