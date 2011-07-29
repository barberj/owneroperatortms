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
import urllib
import simplejson as json

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template

import tms.models as m

class MainHandler(webapp.RequestHandler):
    def get(self):
        payload_q = db.GqlQuery('SELECT * FROM Payload')
        payloads = [payload for payload in payload_q]
        self.response.out.write(
            template.render('index.html',{'payloads': payloads})
        )

    def post(self):
        logging.info('Post')
        load = m.Payload(longitude=float(self.request.get('long')),
                         latitude=float(self.request.get('lat')))
        load.put()
        logging.info('Posted')
        self.redirect('/add_payload')


class ShowPayloads(webapp.RequestHandler):
    def get(self):
        payload_q = db.GqlQuery('SELECT * FROM Payload')
        for payload in payload_q:
            self.response.out.write("%s<br />" % payload)
            self.response.out.write("Created: %s<br />" % payload.created_at)
            self.response.out.write("Updated: %s<br />" % payload.updated_at)
            self.response.out.write("Addr: %s<br />" % payload.pickup_address)
            logging.info(payload)

class GetPayload(webapp.RequestHandler):
    def post(self):
        payload = m.Payload.get_by_id(int(self.request.get('id')))
        self.response.out.write("%s<br />" % payload)
        logging.info(payload)

class UpdatePayload(webapp.RequestHandler):
    def post(self):
        payload = m.Payload.get_by_id(int(self.request.get('id')))
        payload.pickup_address = self.request.get('addr')
        payload.put()
        self.response.out.write("%s<br />%s %s" % (payload))
        logging.info(payload)

class addAddrPayload(webapp.RequestHandler):
    def post(self):
        payload = m.Payload(pickup_address=self.request.get('addr'))

        # geocode
        # http://code.google.com/apis/maps/documentation/geocoding/index.html
        # http://developer.yahoo.com/python/python-rest.html
        # url='http://maps.googleapis.com/maps/api/geocode/json'
        # params = urllib.urlencode ((
        #     ('address', payload.pickup_address),
        #    ('sensor','true')
        #))
        #print params
        url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=true' % urllib.quote(payload.pickup_address)
        #print url
        jsondata = urllib.urlopen(url).read()
        decoded = json.loads(jsondata)
        payload.latitude = decoded['results'][0]['geometry']['location']['lat']
        payload.longitude = decoded['results'][0]['geometry']['location']['lng']
        payload.put()

        self.redirect('/')

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add_payload', MainHandler),
                                          ('/add_payload_addr', addAddrPayload),
                                          ('/get_payload', GetPayload),
                                          ('/update_payload', UpdatePayload),
                                          ('/show', ShowPayloads)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
