# testModels.py
"""
Unittest to test the models
"""

import sys
sys.path.append(r"/cygdrive/c/Users/jbarber/Dropbox/Personal/TMS/www")

import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

import tms.models as m

class testModels(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Create a consistency policy that will simulate the High Replication consistency model.
        self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=0)
        # Initialize the datastore stub with this policy.
        self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)

    def tearDown(self):
        self.testbed.deactivate()    

    def test_1(self):
        """
        Test Email Model
        """

        # Test validator
        self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='junk').put)
        self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='junk.com').put)
        #self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='junk.@junk.com').put)
        #self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='.junk@junk.com').put)
        self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='junk@.junk.com').put)
        self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='junk@..com').put)
        self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='junk@junk').put)
        #self.assertRaises(m.InvalidEmailAddress,m.EmailAddress(emailaddress='.@junk.com').put)

        # Create a good Email
        email = m.EmailAddress(emailaddress='test@ootms.com').put()
        print email
        if sys.version_info >= (2,7):
            self.assertIsNotNone(email)
        self.assertEquals('test@ootms.com', m.EmailAddress.get(email).emailaddress)
    
    
    def test_2(self):
        """
        Test Contact Model
        """
        justin = m.Contact(first_name='Justin',last_name='Barber').put()
        self.assertEquals('Justin', m.Contact.get(justin).first_name)
