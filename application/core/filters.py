import django_filters
from core.models import Product 


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product 
        fields = {
            'name': ['exact','contains'],
            'price': ['exact','lt','gt','range']
            }