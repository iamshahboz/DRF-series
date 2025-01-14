from core.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from core.models import Product, Order
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .utils import generate_excel
from django.db.models import Max 

# we can write function based views
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def make_excel(request):
    products = get_list_or_404(Product)  # Get all customers or 404 if none exist
    return generate_excel(products)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price = Max('price'))['max_price']
    })
    return Response(serializer.data)

    
