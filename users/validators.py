from django.core.exceptions import ValidationError
import re


def validate_phone_number(value):
    if not re.fullmatch(r"^0[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}$", value):
        raise ValidationError("Phone number is not correct")

    return value
