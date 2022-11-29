from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField
# Create your models here.

class ProductCategorys(models.Model):
    name = models.CharField(max_length=244, null=True, blank=True)
    slug = AutoSlugField(populate_from = 'name')

    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'     

    def __str__(self) -> str:
        return self.name   

    @property
    def get_all_product(self):
        return self.products.all()

class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    original_price = models.FloatField(max_length=100)
    discount_price = models.FloatField(max_length=100)
    image = models.FileField(upload_to="products_image/", max_length=100)
    slug = AutoSlugField(populate_from = 'name', editable = True)
    category = models.ForeignKey('ProductCategorys', on_delete= models.CASCADE, related_name= 'products')

    class Meta:
        db_table = 'Products'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return self.name
