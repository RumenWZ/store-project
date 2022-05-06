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

    product_contains = request.GET.get('product_contains')

    if product_contains != '' and product_contains is not None:
        products = products.filter(name__icontains=product_contains)

    context = {
        'products': products,
    }

    print(product_contains)
    return render(request, 'shop.html', context)



class ContactView(views.TemplateView):
    template_name = 'contact.html'