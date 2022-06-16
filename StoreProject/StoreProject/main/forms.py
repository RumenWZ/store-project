from django import forms
from django.contrib.auth import get_user_model

from StoreProject.main.helpers import BootstrapFormMixin
from StoreProject.main.models import Review, Sales
from StoreProject.products.models import Product


class EditProductForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Product
        fields = ('name', 'picture', 'description', 'price', 'discount', 'in_stock')


class ReviewProductForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Review
        fields = ('rating', 'description',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 126, 'rows': 10}),
        }


class CheckoutForm(BootstrapFormMixin, forms.ModelForm):

    payment_methods = [(x, x) for x in Sales.PAYMENT_METHODS]

    payment_method = forms.ChoiceField(
        choices=payment_methods,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Sales
        fields = ('payment_method',)
