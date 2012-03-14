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

# standard python modules
import logging
logging.root.level=logging.DEBUG

# webapp modules
from google.appengine.ext.webapp import template

# webapp2 modules
import webapp2
from webapp2_extras.appengine.auth.models import User

# proprietary modules
from tms.controllers import *


webapp2_config = {
    'webapp2_extras.sessions': {'secret_key': "I've got a lovely bunch of coconuts"},
}

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=MainHandler, name='main'),
    webapp2.Route(r'/login', handler=LoginHandler, name='login'),
    webapp2.Route(r'/logout', handler=LogoutHandler, name='logout'),
    webapp2.Route(r'/user/new', handler=CreateUserHandler, name='newuser'),
], debug=True, config=webapp2_config)
