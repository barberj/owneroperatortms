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
import unittest
import logging
import urllib
import simplejson as json

from google.appengine.ext import  db

import tms.models as m

class testModels(unittest.TestCase):


    def test1(self):
        """
        """

        chicago = m.Trackable(latitude=41.879535,longitude=-87.624333)
        self.assertTrue(chicago, '[%s] Latitude 41.879535, Longitude -87.624333' % chicago.key().id())
        print chicago
