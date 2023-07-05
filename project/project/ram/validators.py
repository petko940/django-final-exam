from django.core.exceptions import ValidationError


def capacity_validator(value):
    if value < 1:
        raise ValidationError('Capacity should be greater than 0!')
