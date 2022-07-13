from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models
# Create your models here.
from StoreProject.common.validators import validate_only_letters_and_numbers, validate_image_resolution


class Product(models.Model):
    NAME_MIN_LEN = 5
    NAME_MAX_LEN = 60

    PRODUCT_PRICE_MAX_DIGITS = 5

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
            # validate_only_letters_and_numbers,
        ),
        null=False,
        blank=False,
    )

    description = models.TextField()

    picture = cloudinary_models.CloudinaryField(
        'image',
        blank=False,
        null=False,
        validators=(
            validate_image_resolution,
        ),
    )

    in_stock = models.BooleanField(
        default=True,
    )

    price = models.DecimalField(
        max_digits=PRODUCT_PRICE_MAX_DIGITS,
        decimal_places=2,
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
        null=True,
        blank=True,
        default=SHIRT,
    )

    discount = models.IntegerField(
        default=0,
    )

    actual_price = models.FloatField(
        null=True,
        blank=True,
    )

    @property
    def get_price(self):
        return self.price * (100 - self.discount) / 100

    def __str__(self):
        return f"{self.name} - {self.type}"


# class ExtraPictures(models.Model):
#     product_id = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#     )
#
#     picture = cloudinary_models.CloudinaryField('image')

