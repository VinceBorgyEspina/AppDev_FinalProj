from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'created_at', 'updated_at')
    list_filter = ('customer',)
    search_fields = ('customer__first_name', 'customer__last_name')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'display_products', 'quantity', 'created_at', 'updated_at')
    list_filter = ('order__customer', 'products__category')

    def display_products(self, obj):
        return ', '.join([str(product) for product in obj.products.all()])

    display_products.short_description = 'Products'
