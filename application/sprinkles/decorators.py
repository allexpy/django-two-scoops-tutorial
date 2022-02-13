from functools import wraps


from . import utils


def can_sprinkle(view_func):
    """Check if a user can add sprinkles"""
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):

        request = utils.check_sprinkles(request)

        response = view_func(request, *args, **kwargs)

        return response
    return new_view_func
