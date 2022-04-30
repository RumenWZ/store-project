from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from StoreProject.common.validators import validate_only_letters


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

