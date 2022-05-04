from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from StoreProject.main.forms import EditProductForm
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


class ProductDetailsView(views.DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'