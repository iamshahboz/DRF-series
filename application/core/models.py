from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 


class User(AbstractUser):
    pass 


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    @property
    def in_stock(self):
        return self.stock > 0 
    
    def __str__(self):
        return self.name 
    

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
    order_id  = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices,
                              default=StatusChoices.PENDING)
    
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')
    
    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, 
                              on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"
    
# # Project models 

# class CityChoices(models.TextChoices):
#     DUSHANBE = 1, 'Душанбе'
#     KHUJAND = 2, 'Худжанд'
#     KHORUG = 3, 'Хорог'
#     KULOB = 4, 'Куляб'
#     BOKHTAR = 5, 'Бохтар'
#     ISTARAVSHAN = 6, 'Истаравшан'
#     MURGOB = 7, 'Мургаб'
#     NORAK = 8, 'Нурек'
#     PANJAKENT = 9, 'Пенджикент'
#     VAKHSH = 10, 'Вахш'
#     HISOR = 11, 'Гисар'
#     ISFARA = 12, 'Исфара'
#     KONIBODOM = 13, 'Канибадам'
#     KURGONTEPPA = 14, 'Курагантюбе'
#     BUSTON = 15, 'Бустон'
#     GULISTON = 16, 'Гулистон'
#     TURSUNZODA = 17, 'Турсунзаде'


# class City(models.Model):
#     name = models.IntegerField(choices=CityChoices.choices)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Город'
#         verbose_name_plural = 'Города'

# class Medicine(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     manufacturer = models.CharField(max_length=100)
#     expired_at = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name 
    
#     class Meta:
#         verbose_name = 'Лекарство'
#         verbose_name_plural = 'Лекарства'


# class Pharmacy(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.IntegerField(choices=CityChoices.choices)
#     phone_number = models.CharField(max_length=20)
#     debt = models.DecimalField(max_digits=6,decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name 
    
#     class Meta:
#         verbose_name = 'Аптека'
#         verbose_name_plural = 'Аптеки'
    


