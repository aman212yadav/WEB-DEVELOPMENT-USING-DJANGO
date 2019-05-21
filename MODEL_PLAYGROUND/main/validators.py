from django.core.exceptions import  ValidationError
def validate_even_number(value):
    if value%2:
        raise ValidationError("Given no is Not Even ")
        