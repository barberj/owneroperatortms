# authenticated.py
"""
Decorators for authenticating users
"""

from decorator import decorator

def authenticated(func, *args, **kwargs):


authenticated = decorator(authenticated)
