from django.urls import path 
from . import views 

app_name = "core"


urlpatterns = [
    path('products/',views.product_list, name='product_list'),
    path('products/<int:pk>/',views.product_detail, name='product_detail'),
    path('products/make_excel', views.make_excel, name='make_excel'),
    path('orders/',views.order_list, name='order_list'),
]