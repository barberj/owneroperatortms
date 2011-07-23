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

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template

import tms.models as m

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


class ShowPayloads(webapp.RequestHandler):
    def get(self):
        payload_q = db.GqlQuery('SELECT * FROM Payload')
        logging.info(payload_q)
        for payload in payload_q:
            logging.info(payload)

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add_payload', MainHandler),
                                          ('/show', ShowPayloads)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
