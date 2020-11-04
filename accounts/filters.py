import django_filters
from .models import *


class OrdersFilter(django_filters.FilterSet):
    class Meta:
        model = OrdersDetail
        fields = {
            'customer_name' : ['exact'],       
            'status' : ['exact'], 
        }