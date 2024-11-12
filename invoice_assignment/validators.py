from django.core.exceptions import ValidationError


def validate_price(price):
    if price <= 0:
        raise ValidationError(f"it can\'t be negative or zero")
