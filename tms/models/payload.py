# payload.py
"""
Payload model
"""

import logging

from google.appengine.ext import db

class Payload(db.Model):
    """
    Payload model. Will keep track of description, location, reference to owner.
    """

    address = db.StringProperty()
    latitude = db.FloatProperty()
    longitude = db.FloatProperty()
    # need references to the owner and operator 
    # and probably some time stamps

    def __str__(self):
        """
        Return string representation for Payload object
        """
        return 'Payload[%s] Latitude: %s, Longitude %s' % ( self.key().id(), 
                                                            self.latitude, 
                                                            self.longitude )
