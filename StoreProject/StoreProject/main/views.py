import math

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from StoreProject.main.forms import ReviewProductForm, CheckoutForm
from StoreProject.main.models import Review, Cart, Sales, SoldItems
from StoreProject.products.models import Product
from django.contrib import messages


def home_view(request):
    trandy_products = Product.objects.all()[:4]

    context = {
        'trandy_products': trandy_products
    }

    return render(request, 'main/index.html', context)


class ItemDetailsView(views.TemplateView):
    template_name = 'main/detail.html'


def cart_view(request):
    user = request.user

    cart_products = Cart.objects.filter(customer_id=user.pk).order_by('product_name')

    cart_summary = sum([x.price * x.quantity for x in cart_products])
    if cart_summary > 0:
        cart_summary_after_shipping = cart_summary + 10
    else:
        cart_summary_after_shipping = 0

    context = {
        'cart_products': cart_products,
        'cart_summary': cart_summary,
        'cart_summary_after_shipping': cart_summary_after_shipping,
    }

    return render(request, 'main/cart.html', context)


def cart_remove_quantity(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')


def cart_add_quantity(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def cart_remove_item(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    cart_item.delete()

    return redirect('cart')


def updateCart(request):
    product_id = request.data['productId']
    print(f"View: {product_id}")

    return JsonResponse('Item was removed', safe=False)


def checkout_view(request):
    user = request.user
    cart_products = Cart.objects.filter(customer_id=user.pk).order_by('product_name')
    cart_summary = sum([x.price * x.quantity for x in cart_products])

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        payment_method = form['payment_method'].value()
        if form.is_valid():
            products = []

            sale = Sales(
                customer=user,
                payment_method=payment_method,
                sale_price=cart_summary + 10
            )
            sale.save()

            for product in cart_products:
                item = Product.objects.get(pk=product.product_id)
                products.append([item, product.size, product.picture, product.price, product.product_name, product.quantity])
                product.delete()

            for product in products:
                product_sale = SoldItems(
                    sale=sale,
                    customer=user,
                    product=product[0],
                    size=product[1],
                    picture=product[2],
                    price=product[3],
                    name=product[4],
                    quantity=product[5],
                )
                product_sale.save()

            return redirect('thank you for shopping')

    else:
        form = CheckoutForm()

    if cart_summary > 0:
        cart_summary_after_shipping = cart_summary + 10
    else:
        cart_summary_after_shipping = 0

    context = {
        'cart_products': cart_products,
        'cart_summary': cart_summary,
        'cart_summary_after_shipping': cart_summary_after_shipping,
        'form': form,
    }

    return render(request, 'main/checkout.html', context)


def shop_view(request):
    ITEMS_PER_PAGE = 3

    # Filters
    price_range_100 = request.GET.get('price-100')
    price_range_200 = request.GET.get('price-200')
    price_range_300 = request.GET.get('price-300')
    product_contains = request.GET.get('product_contains')

    products = Product.objects.all().order_by('id')
    p = Paginator(Product.objects.all().order_by('id'), ITEMS_PER_PAGE)

    if price_range_100:
        p = Paginator(Product.objects.all().filter(actual_price__gt=0, actual_price__lt=101).order_by('id'),
                      ITEMS_PER_PAGE)
    elif price_range_200:
        p = Paginator(Product.objects.all().filter(actual_price__gt=100, actual_price__lt=201).order_by('id'),
                      ITEMS_PER_PAGE)
    elif price_range_300:
        p = Paginator(Product.objects.all().filter(actual_price__gt=200, actual_price__lt=301).order_by('id'),
                      ITEMS_PER_PAGE)

    if product_contains != '' and product_contains is not None:
        p = Paginator(Product.objects.all().filter(name__icontains=product_contains).order_by('id'), ITEMS_PER_PAGE)

    page = request.GET.get('page')
    products_page = p.get_page(page)

    next_page_twice = products_page.number + 2
    previous_page_twice = products_page.number - 2

    max_page_num = math.ceil(len(products) / ITEMS_PER_PAGE)

    for product in products:
        product.actual_price = product.price * (100 - product.discount) / 100
        product.save()

    products_all_count = products.count()
    products_in_range_0_100 = products.filter(actual_price__gt=0, actual_price__lt=101).count()
    products_in_range_100_200 = products.filter(actual_price__gt=100, actual_price__lt=201).count()
    products_in_range_200_300 = products.filter(actual_price__gt=200, actual_price__lt=301).count()

    context = {
        'products': products,
        'products_all_count': products_all_count,
        'products_0_100': products_in_range_0_100,
        'products_100_200': products_in_range_100_200,
        'products_200_300': products_in_range_200_300,
        'products_page': products_page,
        'max_page_num': max_page_num,
        'next_page_twice': next_page_twice,
        'previous_page_twice': previous_page_twice,
    }

    return render(request, 'main/shop.html', context)


def review_view(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)

    sales = Sales.objects.all().filter(customer_id=request.user)
    purchased_products = []

    for sale in sales:
        products = SoldItems.objects.all().filter(sale_id=sale.pk)
        for x in products:
            purchased_products.append(x)

    have_purchased = product.pk in [x.product_id for x in purchased_products]
    if not have_purchased:
        messages.warning(request, 'You do not own this product.')
        # return redirect('index')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if request.method == 'POST':
        form = ReviewProductForm(request.POST)
        rating = form['rating'].value()
        description = form['description'].value()

        if form.is_valid():
            review = Review(
                product_id=product.id,
                description=description,
                rating=rating,
                reviewer=user,
                reviewer_name=user.username
            )

            review.save()

            return HttpResponseRedirect('/')
    else:
        form = ReviewProductForm()

    context = {
        'form': form,
        'pk': pk,
        'product': product,
    }

    return render(request, 'main/review.html', context)


def my_purchases_view(request):
    sales = Sales.objects.all().filter(customer_id=request.user)
    purchased_products = []

    for sale in sales:
        products = SoldItems.objects.all().filter(sale_id=sale.pk)
        for product in products:
            purchased_products.append(product)

    context = {
        'purchased_products': purchased_products,
    }

    return render(request, 'main/purchases.html', context)



class ContactView(views.TemplateView):
    template_name = 'main/contact.html'


class CartDeleteView(views.DeleteView):
    model = Cart
    template_name = 'main/cart.html'
    success_url = reverse_lazy('cart')


def thank_you_for_shopping_view(request):
    context = {

    }

    return render(request, 'main/thank_you_shopping.html', context)


def error_400(request, exception):
    return render(request, 'errors/400.html', status=403)


def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)


def error_404(request):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html', status=500)
