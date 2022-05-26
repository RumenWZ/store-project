from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models

# Create your models here.
from StoreProject.accounts.models import Profile
from StoreProject.common.validators import validate_only_letters_and_numbers
from StoreProject.products.models import Product


class Review(models.Model):
    RATINGS = [(str(x), x) for x in range(1, 6)]

    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    description = models.TextField()

    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        null=False,
        blank=False,
        default=5,
    )

    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    review_date = models.DateTimeField(
        auto_now_add=True,
    )


class Cart(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class Sales(models.Model):
    pass