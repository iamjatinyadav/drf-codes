from django.db import models
from django_extensions.db.models import TimeStampedModel, AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models import Sum
from django_countries.fields import CountryField
from django.db.models import Q
from .choices import *
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

    @property
    def get_product_review(self):
        return self.reviews.all()

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


class Newsletter(TimeStampedModel):
    email = models.EmailField(max_length=40, unique=True, error_messages= {"unique":"this email already register with newsletter"})

    class Meta:
        db_table = 'Newsletter'
        managed = True
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self) -> str:
        return self.email


class WishList(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_wishlist")
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Wishlists'
        managed = True
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self) -> str:
        return self.product.name


class Cart(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercart')
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'Carts'
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self) -> str:
        return self.user.username

    @property
    def cart_items_count(self):
        total = 0
        for counts in self.cartitems.all():
            total += counts.count
        return total


    @property
    def total_value(self):
        total = self.cartitems.all().aggregate(Sum('total_price'))
        # print(type(str(total)))
        # print(type(total['total_price__sum']))
        if total['total_price__sum'] == None:
            return 0
        return total['total_price__sum']

    @property
    def all_items(self):
        return self.cartitems.all()

    


class CartItems(TimeStampedModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cartitems')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='cartproducts')
    count = models.IntegerField(default=1)
    total_price = models.FloatField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Cartitem'
        managed = True
        verbose_name = 'Cartitem'
        verbose_name_plural = 'Cartitems'


    def __str__(self) -> str:
        return self.product.name 


    def save(self, *args, **kwargs):

        self.total_price = self.count * self.product.discount_price
        super(CartItems, self).save(*args, **kwargs)


class Address(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="useraddress")
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    mobileno = models.CharField(max_length=13)
    addressline1 = models.CharField(max_length=50)
    addressline2 = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    default_address = models.BooleanField(default=False)


    class Meta:
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['user'],
        #         condition=Q(default_address=True),
        #         name='unique_default_address_per_user'
        #     )
        # ]
        db_table = 'Address'
        managed = True
        verbose_name = 'Address'
        verbose_name_plural = 'Addresss'


    def __str__(self) -> str:
        return str(self.id)

    
    def save(self, *args, **kwargs):
        if self.default_address:
            self.__class__._default_manager.filter(user = self.user.id, default_address=True).update(user =self.user.id , default_address=False)
        super().save(*args, **kwargs)



class Checkout(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkout')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='checkout', null=True)
    payment = models.IntegerField(choices=Payment_choices.choices,default=Payment_choices.Paypal)
    product = models.JSONField()
    total = models.FloatField(default=0) 


    class Meta:
        db_table = 'Checkout'
        managed = True
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'

    def __str__(self) -> str:
        return self.user.username +" spend "+ self.total

