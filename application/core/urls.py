from django.urls import path 
from . import views 

app_name = "core"


urlpatterns = [
    path('products/',views.ProductListAPIView.as_view()),
    path('products/<int:pk>/',views.ProductDetailAPIView.as_view()),
    # path('products/make_excel', views.make_excel, name='make_excel'),
    # path('orders/',views.order_list, name='order_list'),
]