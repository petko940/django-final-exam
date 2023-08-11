from django.core.exceptions import ValidationError


def cpu_name_validator(value):
    if len(value) < 3:
        raise ValidationError('CPU name should be at least 3 characters long!')


def cpu_clock_speed_validator(value):
    if value <= 0:
        raise ValidationError('Clock speed should be bigger than 0!')


def cpu_number_cores_validator(value):
    if not 0 < value <= 512:
        raise ValidationError('Number cores should be between 1 and 512!')


def cpu_cache_size_validator(value):
    if not 0 < value <= 1024:
        raise ValidationError('Cache size should be between 1 and 1024 (MB)!')
