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

import logging

class MainHandler(BaseHandler):
    @authenticated
    def get(self, **kwargs):
        """
        """
        return template.render('tms/templates/index.html',
                                {})

class LoginHandler(BaseHandler):
    def get(self):
        """
        Returns a simple HTML form for login
        """
        return """
            <!DOCTYPE hml>
            <html>
                <head>
                    <title>Ten Twenty</title>
                </head>
                <body>
                <form action="%s" method="post">
                    <fieldset>
                        <legend>Please Login</legend>
                        <label>Username <input type="text" name="username" placeholder="Your username" /></label>
                        <label>Password <input type="password" name="password" placeholder="Your password" /></label>
                    </fieldset>
                    <button>Login</button>
                </form>
            </html>
        """ % self.request.url

    def post(self):
        """
        username: Get the username from POST dict
        password: Get the password from POST dict
        """
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        # Try to login user with password
        # Raises InvalidAuthIdError if user is not found
        # Raises InvalidPasswordError if provided password doesn't match with specified user
        try:
            self.auth.get_user_by_password(username, password)
            self.redirect('/')
        except (InvalidAuthIdError, InvalidPasswordError), e:
            logging.error('Unable to authenticate %s with credentials %s', username, password)
            #return "The username or password you entered is incorrect. <a href='%s'>Forgot your password<?/a>" % self.uri_for('forgot')
            return "The username or password you entered is incorrect. <a href='%s'>Forgot your password<?/a>" % 'i forgot'


class LogoutHandler(BaseHandler):
    pass
