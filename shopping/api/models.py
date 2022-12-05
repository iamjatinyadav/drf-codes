from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator

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
        return str(self.id)


class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=255)
    message = models.TextField()


    class Meta:
        db_table = 'Contacts'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


    def __str__(self) -> str:
        return self.name

class Review(TimeStampedModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],help_text="please enter value in  1 to 5 ", default=1)

    class Meta:
        db_table = 'reviews'
        managed = True
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self) -> str:
        return self.name
