from django import forms

from StoreProject.main.helpers import BootstrapFormMixin
from StoreProject.products.models import Product


class EditProductForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Product
        fields = ('name', 'picture', 'description', 'price', 'discount', 'in_stock')