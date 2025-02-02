from django.contrib import admin
from core.models import Order, OrderItem, User, City

class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



admin.site.register(Order, OrderAdmin)
admin.site.register(User)
admin.site.register(City, CityAdmin)
