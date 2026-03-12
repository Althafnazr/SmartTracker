from django.contrib import admin
from .models import Product, ServiceRequest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'stock_quantity', 'selling_price')
    search_fields = ('brand', 'category')
    list_filter = ('category',)


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product', 'service_status', 'received_date')
    list_filter = ('service_status',)
    search_fields = ('customer_name', 'product__brand')
