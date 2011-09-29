# authorization.py
"""
Decorators for verifying users authorization
"""
from authentication import authenticated
from decorator import decorator


@authenticated
def authorized(func, *args, **kwargs):
    """
    Decorator to check that the logged in user is authorized
    for the requested url
    """

    return func(*args, **kwargs)

authorized = decorator(authorized)
