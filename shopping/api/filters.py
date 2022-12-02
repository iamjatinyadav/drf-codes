from django_filters import FilterSet,RangeFilter, NumericRangeFilter
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend

class PriceFilter(FilterSet):
    discount_price = RangeFilter()

    class Meta:
        model = Product
        fields = ['discount_price']


def fil(DjangoFilterBackend):

    pass