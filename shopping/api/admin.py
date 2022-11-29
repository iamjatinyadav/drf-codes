from django.contrib import admin
from .models import *
# Register your models here.




@admin.register(ProductCategorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'discount_price', 'slug', 'category']