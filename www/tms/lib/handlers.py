import webapp2
from webapp2_extras import auth
from webapp2_extras import sessions
from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

import logging
logging.root.level=logging.DEBUG

class BaseHandler(webapp2.RequestHandler):
    """
    BaseHandler for all requests

    Holds the auth and session properties so they are reachable for all requests
    """
    def dispatch(self):
        """
        Save the sessions for preservation across requests
        """
        try:
            response = super(BaseHandler, self).dispatch()
            self.response.write(response)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def auth(self):
        return auth.get_auth()

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def auth_config(self):
        """
        Dict to hold urls for login/logout
        """
        return {
            'login_url': self.uri_for('login'),
            'logout_url': self.uri_for('logout')
        }

    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()
