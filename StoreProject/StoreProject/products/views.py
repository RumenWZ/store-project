from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from StoreProject.main.forms import EditProductForm
from StoreProject.main.models import Review
from StoreProject.products.models import Product

class AddProductView(views.CreateView):
    template_name = 'products/product_add.html'
    model = Product
    fields = ('name', 'description', 'picture', 'type', 'price',)
    success_url = reverse_lazy('index')

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
    product = Product.objects.get(pk=pk)
    reviews_for_product = Review.objects.all().filter(product_id=pk)
    reviews_count = len(reviews_for_product)
    if reviews_for_product:
        avg_reviews = sum([int(review.rating) for review in reviews_for_product]) / reviews_count
    else:
        avg_reviews = 0

    context = {
        'product': product,
        'reviews': reviews_for_product,
        'reviews_count': reviews_count,
        'average_reviews': avg_reviews,
    }

    return render(request, 'products/product_detail.html', context)


class ProductDeleteView(views.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('shop')

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result
