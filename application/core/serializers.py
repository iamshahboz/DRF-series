from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'price',
                  'stock',)
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0"
            )
        return value 
    
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price')
    class Meta:
        model = OrderItem
        fields = ('product_name', 
                  'product_price',
                  'quantity',
                  'item_subtotal')
    
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    # you can implement additinal logic for calculation with SerializerMethodField
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model = Order 
        fields = ('order_id', 
                  'created_at',
                  'user',
                  'status',
                  'items',
                  'total_price',)
        

'''
What if you want your serializer not to be binded to any model but just return JSON response from multiple models
'''
class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
