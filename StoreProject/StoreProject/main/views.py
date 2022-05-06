from django.shortcuts import render

# Create your views here.
from django.views import generic as views

from StoreProject.products.filters import ProductFilter
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

# class ShopView(views.TemplateView):
#     template_name = 'shop.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         products = Product.objects.all()
#
#         print(products)
#
#         myFilter = ProductFilter(request.GET,)
#
#         context.update({
#             'myFilter': myFilter,
#             'products': products,
#         })
#
#         return context

def shop_view(request):
    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {
        'products': products,
        'myFilter': myFilter,
    }

    return render(request, 'shop.html', context)



class ContactView(views.TemplateView):
    template_name = 'contact.html'