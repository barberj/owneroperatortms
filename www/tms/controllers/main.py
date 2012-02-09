"""
A real simple app for using webapp2 with auth and session.

It just covers the basics. Creating a user, login, logout and a decorator for protecting certain handlers.

PRE-REQUIREMENTS:

Set at secret_key in webapp2 config:
webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': 'Im_an_alien',
}

You need to either set upp the following routes:

app = webapp2.WSGIApplication([
    webapp2.Route(r'/login/', handler=LoginHandler, name='login'),
    webapp2.Route(r'/logout/', handler=LogoutHandler, name='logout'),
    webapp2.Route(r'/login/', handler=SecureRequestHandler, name='secure'),
    webapp2.Route(r'/secure/', handler=CreateUserHandler, name='create-user'),

])

OR:

Change the urls in BaseHandler.auth_config to match LoginHandler/LogoutHandler
And also change the url in the post method of the LoginHandler to redirect to to a page requiring a user session
"""
import webapp2
from webapp2_extras import auth
from webapp2_extras import sessions
from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError
from google.appengine.ext.webapp import template

from tms.lib.handlers import BaseHandler

import logging
logging.root.level=logging.DEBUG

class MainHandler(BaseHandler):
    def get(self, **kwargs):
        """
        """
        return template.render('tms/templates/index.html',
                                {})
