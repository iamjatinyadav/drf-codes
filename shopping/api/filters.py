from django_filters import FilterSet,RangeFilter
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

class PriceFilter(FilterSet):
    discount_price = RangeFilter()

    class Meta:
        model = Product
        fields = ['discount_price']


# class idorder(OrderingFilter):

#     def get_ordering_value(self, param):
#         descending = param.startswith("-")
#         param = param[:5] if descending else param
#         field_name = self.param_map.get(param, param)

#         return "-%s" % field_name if descending else field_name






