from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    model=Product
    context_object_name='product_list'
    template_name='product/product_list_view.html'

class ProductDetailView(DetailView):
    model=Product
    context_object_name='product_detail'
    template_name='product/product_detail_view.html'
    
