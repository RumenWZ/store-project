from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Must contain only letters')


def validate_only_letters_and_numbers(value):
    for ch in value:
        if not ch.isalpha() or not ch.isnumeric():
            raise ValidationError('Must contain only letters')


def validate_image_resolution(value):
    w, h = get_image_dimensions(value)
    if w != h:
        raise ValidationError('The image height must be the same as the width.')