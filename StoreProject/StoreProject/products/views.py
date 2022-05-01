from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from StoreProject.products.models import Product


class AddProductView(views.CreateView):
    template_name = 'products/product_add.html'
    model = Product
    fields = ('name', 'description', 'picture', 'type')
    success_url = reverse_lazy('index')