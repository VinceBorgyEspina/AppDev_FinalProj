from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product, Customer, Order, OrderItem

class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = "base.html"
    paginate_by = 3  # Set the number of items per page
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 3  # Set the number of items per page

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 3  # Set the number of items per page

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    paginate_by = 3  # Set the number of items per page

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 3  # Set the number of items per page

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'order_item_list.html'
    context_object_name = 'order_items'
    paginate_by = 3  # Set the number of items per page

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'order_item_detail.html'
    context_object_name = 'order_item'
