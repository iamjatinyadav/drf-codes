from django_filters import FilterSet,RangeFilter, NumberFilter
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

class PriceFilter(FilterSet):
    discount_price = RangeFilter()

    class Meta:
        model = Product
        fields = ['discount_price']



class recentFilter(FilterSet):
    id = NumberFilter()

    class Meta:
        model = Product
        fields = ['id']