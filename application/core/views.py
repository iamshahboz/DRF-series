from core.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from core.models import Product, Order
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .utils import generate_excel
from django.db.models import Max 
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly, 
    IsAdminUser,
    AllowAny
    )
from rest_framework import generics 
from rest_framework.views import APIView

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('name','price')

    '''
    In the lines below, what we want to do is to resrict post request 
    so that only Admin users can create a product
    '''

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

 
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

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
    
class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)
    

# think of the case where we might want to return the products which is not out of stock(stock> 0) and we have to override get_queryset
# method 
# queryset = Product.objects.filter(stock__gt=0)


# @api_view(['GET'])
# def make_excel(request):
#     products = get_list_or_404(Product)  # Get all customers or 404 if none exist
#     return generate_excel(products)


