from django import forms
from django.contrib.auth import get_user_model

from StoreProject.main.helpers import BootstrapFormMixin
from StoreProject.main.models import Review
from StoreProject.products.models import Product


class EditProductForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Product
        fields = ('name', 'picture', 'description', 'price', 'discount', 'in_stock')


class ReviewProductForm(BootstrapFormMixin, forms.ModelForm):

    RATINGS = [(x, x) for x in range(1, 6)]

    description = forms.CharField(
        widget=forms.Textarea,
    )

    rating = forms.ChoiceField(
        choices=RATINGS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    def save(self, commit=True):
        user = get_user_model()

        review = Review(
            description=self.cleaned_data['description'],
            rating=self.cleaned_data['rating'],
            reviewer=user,
        )

        if commit:
            review.save()
        return user


    class Meta:
        model = Review
        fields = ('rating', 'description',)
