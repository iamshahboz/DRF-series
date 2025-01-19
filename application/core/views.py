from core.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from core.models import Product, Order
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .utils import generate_excel
from django.db.models import Max 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics 

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        qs = super().get_queryset()
        return qs.filter(user=user)

# think of the case where we might want to return the products which is not out of stock(stock> 0) and we have to override get_queryset
# method 
# queryset = Product.objects.filter(stock__gt=0)


# @api_view(['GET'])
# def make_excel(request):
#     products = get_list_or_404(Product)  # Get all customers or 404 if none exist
#     return generate_excel(products)


