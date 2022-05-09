import math

from django.core.paginator import Paginator
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


def shop_view(request):
    ITEMS_PER_PAGE = 2

    products = Product.objects.all()
    p = Paginator(Product.objects.all(), ITEMS_PER_PAGE)
    page = request.GET.get('page')
    products_page = p.get_page(page)

    next_page_twice = products_page.number + 2
    previous_page_twice = products_page.number - 2

    max_page_num = math.ceil(len(products) / ITEMS_PER_PAGE)

    for product in products:
        product.actual_price = product.price * (100 - product.discount) / 100
        product.save()

    price_range_100 = request.GET.get('price-100')
    price_range_200 = request.GET.get('price-200')
    price_range_300 = request.GET.get('price-300')

    product_contains = request.GET.get('product_contains')

    if product_contains != '' and product_contains is not None:
        products = products.filter(name__icontains=product_contains)

    products_all_count = products.count()
    products_in_range_0_100 = products.filter(actual_price__gt=0, actual_price__lt=101).count()
    products_in_range_100_200 = products.filter(actual_price__gt=100, actual_price__lt=201).count()
    products_in_range_200_300 = products.filter(actual_price__gt=200, actual_price__lt=301).count()

    print(max_page_num)

    if price_range_100:
        products = products.filter(actual_price__gt=0, actual_price__lt=101)
    elif price_range_200:
        products = products.filter(actual_price__gt=100, actual_price__lt=201)
    elif price_range_300:
        products = products.filter(actual_price__gt=200, actual_price__lt=301)

    print(f'prev twice: {previous_page_twice}')
    context = {
        'products': products,
        'products_all_count': products_all_count,
        'products_0_100': products_in_range_0_100,
        'products_100_200': products_in_range_100_200,
        'products_200_300':products_in_range_200_300,
        'products_page': products_page,
        'max_page_num': max_page_num,
        'next_page_twice': next_page_twice,
        'previous_page_twice': previous_page_twice,
    }

    return render(request, 'shop.html', context)



class ContactView(views.TemplateView):
    template_name = 'contact.html'