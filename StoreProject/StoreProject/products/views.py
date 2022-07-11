from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib import messages

from StoreProject.main.forms import EditProductForm
from StoreProject.main.models import Review, Cart
from StoreProject.products.models import Product


class AddProductView(UserPassesTestMixin, LoginRequiredMixin, views.CreateView):
    template_name = 'products/product_add.html'
    login_url = '/accounts/login/'
    model = Product
    fields = ('name', 'description', 'picture', 'type', 'price',)
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProductView(UserPassesTestMixin, views.UpdateView):
    template_name = 'products/product_edit.html'
    form_class = EditProductForm
    model = Product
    success_url = reverse_lazy('index')

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


# class ProductDetailsView(views.DetailView):
#     template_name = 'products/product_detail.html'
#     model = Product
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#
#         return


def product_details(request, pk):
    sizes = {
        'XS': request.GET.get('size-XS'),
        'S': request.GET.get('size-S'),
        'M': request.GET.get('size-M'),
        'L': request.GET.get('size-L'),
        'XL': request.GET.get('size-XL'),
    }

    for size, value in sizes.items():
        if value is not None:
            size = size
            break
        else:
            size = None

    if size:
        user = request.user
        if user.is_anonymous:
            return redirect('login')
        product = Product.objects.get(pk=pk)

        cart = Cart(
            customer=user,
            product=product,
            size=size,
            price=product.get_price,
            picture=product.picture,
            product_name=product.name,

        )
        cart.save()
        messages.success(request, 'Item successfully added to cart.')

    may_also_like = Product.objects.all()
    product = Product.objects.get(pk=pk)
    # may_also_like.pop(product)
    reviews_for_product = Review.objects.all().filter(product_id=pk)
    reviews_count = len(reviews_for_product)
    if reviews_for_product:
        avg_reviews = sum([int(review.rating) for review in reviews_for_product]) / reviews_count
        avg_reviews_decimal = int(str(avg_reviews)[2])
    else:
        avg_reviews = None
        avg_reviews_decimal = None

    context = {
        'product': product,
        'reviews': reviews_for_product,
        'reviews_count': reviews_count,
        'average_reviews': avg_reviews,
        'average_reviews_decimal': avg_reviews_decimal,
        'may_also_like': may_also_like,
    }

    return render(request, 'products/product_detail.html', context)


class ProductDeleteView(views.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('shop')

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result
