# authorization.py
"""
Decorators for verifying users authorization
"""
import logging

from decorator import decorator
from authentication import authenticated

@authenticated
def authorized(func, *args, **kwargs):
    """
    Decorator to check that the logged in user is authorized
    for the requested url
    """

    logging.debug('Authorizing')
    return func(*args, **kwargs)

authorized = decorator(authorized)
