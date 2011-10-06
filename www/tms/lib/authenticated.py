# authenticated.py
"""
Decorators for authenticating users
"""
import logging

from decorator import decorator
from gaeutilities.appengine_utilities import sessions

def authenticated(func, cls, *args, **kwargs):
    logging.info('Authenticating')
    session = sessions.Session()
    if 'user' in session:
        logging.info('User in session %s' % session['user'])
        return func(cls, *args, **kwargs)
    else:
        logging.info('Not Authnticated')
        cls.redirect('/')

authenticated = decorator(authenticated)
