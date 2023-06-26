from django.core.exceptions import ValidationError


def validate_username(value: str):
    error_msg = ""
    if " " in value:
        error_msg = "Username must be one word only"

    elif value[0].isdigit():
        error_msg = "Username cannot start with a digit"

    elif len(value) < 3:
        error_msg = "Username must be at least 3 characters"

    elif not value.isalnum():
        error_msg = "Username must be alphanumeric"

    if error_msg:
        raise ValidationError(error_msg)
