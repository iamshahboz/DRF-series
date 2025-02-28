from django.contrib import admin
from core.models import (
    Order, OrderItem, User, 
    City, Medicine, Pharmacy)

class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['']
    search_fields = ['']



admin.site.register(Order, OrderAdmin)
admin.site.register(User)
admin.site.register(City, CityAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Pharmacy,PharmacyAdmin)
