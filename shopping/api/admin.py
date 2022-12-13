from django.contrib import admin
from .models import *
# Register your models here.




@admin.register(ProductCategorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'discount_price', 'slug', 'view_category']

    def view_category(self, obj):
        return obj.category.slug


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'email', 'rating', 'product', 'created']


@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cart_items_count', 'total_value']

@admin.register(CartItems)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'count', 'total_price']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'firstname', 'addressline1', 'country', 'zipcode', 'default_address']

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'payment', 'total']