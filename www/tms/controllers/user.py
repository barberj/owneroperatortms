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

from tms.lib.handlers import *
from google.appengine.api import users
import logging

class CreateUserHandler(BaseHandler):
    def get(self):
        """
        Returns a simple HTML form for create a new user
        """
        user = users.get_current_user()
        return """
            <!DOCTYPE hml>
            <html>
                <head>
                    <title>Create User</title>
                </head>
                <body>
                Welcome %s <a href="%s">Log Out</a>.</p>
                <form action="%s" method="post">
                    <fieldset>
                        <legend>Create user form</legend>
                        <label>Email <input type="text" name="username" placeholder="Your username" /></label>
                        <label>Password <input type="password" name="password" placeholder="Your password" /></label>
                    </fieldset>
                    <button>Create user</button>
                </form>
            </html>
        """ % (user.nickname(), users.create_logout_url('/'), self.request.url)

    def post(self):
        """
        username: Get the username from POST dict
        password: Get the password from POST dict
        """
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        # Passing password_raw=password so password will be hashed
        # Returns a tuple, where first value is BOOL. If True ok, If False no new user is created
        user = self.auth.store.user_model.create_user(username, password_raw=password)
        if not user[0]: #user is a tuple
            return 'The email address you are trying to register has already been taken.'
        else:
            # User is created, let's try redirecting to login page
            try:
                self.redirect(self.auth_config['login_url'], abort=True)
            except (AttributeError, KeyError), e:
                self.abort(403)
