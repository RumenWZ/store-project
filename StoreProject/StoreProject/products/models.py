from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models
# Create your models here.
from StoreProject.common.validators import validate_only_letters_and_numbers


class Product(models.Model):
    NAME_MIN_LEN = 5
    NAME_MAX_LEN = 60

    SHIRT = 'Shirt'
    PANTS = 'Pants'
    SWEATER = 'Sweater'
    JACKET = 'Jacket'
    JEANS = 'Jeans'
    DRESS = 'Dress'
    SUIT = 'Suit'
    HOODIE = 'Hoodie'
    COAT = 'Coat'

    TYPES = [(x, x) for x in [SHIRT, PANTS, SWEATER, JACKET, JEANS, DRESS, SUIT, HOODIE, COAT]]

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
            validate_only_letters_and_numbers,
        ),
        null=False,
        blank=False,
    )

    description = models.TextField()

    picture = cloudinary_models.CloudinaryField('image')

    in_stock = models.BooleanField(
        default=True,
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
        null=True,
        blank=True,
        default=SHIRT,
    )