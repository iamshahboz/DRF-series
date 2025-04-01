from django.urls import path 
from . import views 

app_name = "core"


urlpatterns = [
    path('products/',views.ProductListCreateAPIView.as_view()),
    path('products/<int:product_id>/',views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/info',views.ProductInfoAPIView.as_view()),
    path('orders/',views.OrderListAPIView.as_view()),
    path('user-orders/',views.UserOrderListAPIView.as_view(), name='user-orders'),
    # path('products/make_excel', views.make_excel, name='make_excel'),
    # path('orders/',views.order_list, name='order_list'),
]