#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
logging.root.level=logging.DEBUG


import urllib
import simplejson as json

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template

import tms.models as m
from tms.lib.authenticated import authenticated
from gaeutilities.appengine_utilities import sessions
import time

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
            template.render('index.html',{})
        )

    def post(self):
        logging.info('Post')
        load = m.Payload(longitude=float(self.request.get('long')),
                         latitude=float(self.request.get('lat')))
        load.put()
        logging.info('Posted')
        self.redirect('/add_payload')

class Logout(webapp.RequestHandler):
    def get(self):
        session = sessions.Session()
        logging.info('Logout %s' % session['user'])
        session.delete()
        self.redirect('/')
        time.sleep(1)

    def post(self):
        logging.info('Login')
        session = sessions.Session()
        session['user']='Justin'

class Login(webapp.RequestHandler):
    def get(self):
        logging.info('Login')
        session = sessions.Session()
        session['user']='Justin'
        self.redirect('/test')
        #self.response.out.write(
        #    template.render('login.html',{})
        #)

    def post(self):
        logging.info('Login')
        session = sessions.Session()
        session['user']='Justin'


class Test(webapp.RequestHandler):

    @authenticated
    def get(self):
        robby = m.Contact(first_name='Robby',last_name='Ranshous').put()
        email = m.EmailAddress(email_type=m.PropertyType.get_by_id(285),contact=m.Contact.get(robby),emailaddress='rranshous@ootms.com').put()
        phone = m.PhoneNumber(phone_type=m.PropertyType.get_by_id(285),contact=m.Contact.get(robby),phone_number='3216263441').put()
        m.User(username=m.EmailAddress.get(email),password='password').put()
        trans = m.Transporter(contact=m.Contact.get(robby)).put()


        justin = m.Contact(first_name='Justin',last_name='Barber').put()
        email = m.EmailAddress(email_type=m.PropertyType.get_by_id(285),contact=m.Contact.get(justin),emailaddress='jbarber@ootms.com').put()
        phone = m.PhoneNumber(phone_type=m.PropertyType.get_by_id(285),contact=m.Contact.get(justin),phone_number='4048636685').put()
        m.User(username=m.EmailAddress.get(email),password='password').put()
        broker=m.Broker(contact=m.Contact.get(justin)).put()

        pay = m.Payload(broker=m.Broker.get(broker)).put()

    def delete(self):
        """
        Delete/Clean Test data
        """
        for contact in m.Contact.all():
         contact.delete()
        for broker in m.Broker.all():
         broker.delete()
        for trans in m.Transporter.all():
         trans.delete()
        for payload in m.Payload.all():
         payload.delete()
        for trackable in m.Trackable.all():
         payload.delete()

class Payload(webapp.RequestHandler):
    def delete(self, id):
        """
        Delete payload(s)
        """
        payload = m.Payload.get_by_id(int(id))
        logging.info('[Payload] Deleteing %s', payload)

    def get(self,id):
        """
        Retrieve payload
        """
        method = self.request.method
        if method and method == 'DELETE':
            self.delete(id)
        else:
            payload = m.Payload.get_by_id(int(id))
            logging.info('[Payload] Retrieving %s', payload)
            self.response.out.write(payload)

    def post(self,id):
        """
        Payloads moving!
        """
        lat = self.request.get('latitude')
        lon = self.request.get('longitude')
        tracking = m.Payload.get_by_key_name(id)
        if not tracking:
            logging.info('Posting Long: %s, Lat: %s' % lon, lat)
        tracking.update_location(lat=lat, lon=lon)

    def put(self):
        """
        Update payload(s)
        """
        pass

class Payloads(webapp.RequestHandler):
    def get(self):
        """
        Retrieve all undelievered payloads owned by a broker
        """
        broker = m.Broker.get_by_id(572)
        payloads = m.Payload.all().filter('broker =', broker).\
                     filter('delivered_at =', None)

        retVal = [payload for payload in payloads]

        return json.dumps(retVal)

class Client(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
            template.render('mobile_index.html',{})
        )
        return

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/payload/(.*)/track', Payload),
                                          ('/test', Test),
                                          ('/client', Client),
                                          ('/logout', Logout),
                                          ('/login', Login)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
