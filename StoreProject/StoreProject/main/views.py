from django.shortcuts import render

# Create your views here.
from django.views import generic as views

from StoreProject.products.models import Product


class HomeView(views.ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'


class ItemDetailsView(views.TemplateView):
    template_name = 'detail.html'

class CartView(views.TemplateView):
    template_name = 'cart.html'

class CheckoutView(views.TemplateView):
    template_name = 'checkout.html'

class ShopView(views.TemplateView):
    template_name = 'shop.html'