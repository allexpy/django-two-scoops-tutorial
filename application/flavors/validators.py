from django.core.exceptions import ValidationError


from flavors.models import Flavor


def validate_title(value):
    flavors = Flavor.objects.filter(title__exact=value)
    for flavor in flavors:
        if value == flavor.title:
            msg = 'This flavor already exists.'
            raise ValidationError(msg)


def validate_tasty(value):
    """
    Raise a ValidationError if the value doesn't start with the word 'Tasty'.
    """
    if not value.startswith('Tasty') or not value.startswith('tasty'):
        msg = 'Must start with Tasty'
        raise ValidationError(msg)
