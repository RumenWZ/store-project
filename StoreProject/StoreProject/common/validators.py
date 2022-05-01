from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Must contain only letters')


def validate_only_letters_and_numbers(value):
    for ch in value:
        if not ch.isalpha() or not ch.isnumeric():
            raise ValidationError('Must contain only letters')
