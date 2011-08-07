
"""
The pattern here is going to be the client connects for the
first time (operator).  We return a page w/ channel token.

Once the client has settup the channel it will request a full data dump
of all it's delivery locations, as well as a dump of drivers.

Responses for this data will be send back over the channel in chunks.

Requests for the data are sent as GET requests
"""

import simplejson as json
import logging
import time

from google.appengine.api import channel, users
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template

class Main(webapp.RequestHandler):
    """
    returns the client application w/ the channel token embedded
    """
    def get(self):

        # check that we are logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        # setup a new channel
        # TODO: use something other than just the user id
        token = channel.create_channel(user.user_id())

        # return our main page w/ the token embedded
        template_values = {'channel_token':token,
                           'user':user}

        self.response.out.write(template.render('index_streaming.html'),
                                template_values)


class SendFullUpdate(webapp.RequestHandler):
    """
    Returns (in chunks) all the users delivery data and driver locations via
    the client channel
    """
    def get(self):
        # grab the user
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        # grab the user's operator obj
        operator = Operator.gql('WHERE user = :1', user)

        # grab the operator's planned payloads
        planned_payloads = PlannedPayloads.gql('WHERE operator = :1', operator)

        # TODO: send in chunks
        # send our planned payload json data over the wire
        channel.send_message(
            user.user_id(),
            json.dumps(
                map(lambda o: o.to_json(), planned_payloads))
        )

        # now grab the payloads
        payloads = Payloads.gql('WHERE operator = :1',operator)

        # TODO: send in chunks
        # send on down the line
        channel.send_message(
            user.user_id,
            json.dumps(
                map(lambda o: o.to_json(), payloads))
        )

        # TODO: only grab transporters w/in a certian distance
        #       of the users planned/payloads
        # TODO: in chunks
        # now they want the transporter data
        transporters = Transport.all()

        # send down the line
        channel.send_message(
            user.user_id(),
            json.dumps(
                map(lambda o: o.to_json(), transporters))
        )

        # and we're done
        return


def main():
    application = webapp.WSGIApplication([('/', Main),
                                          ('/request_full_update', SendFullUpdate)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

