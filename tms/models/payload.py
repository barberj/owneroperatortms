# payload.py
"""
Payload model
- the load carried by a vehicle exclusive of what is necessary for its operation
"""

import logging
from datetime import datetime

from google.appengine.ext import db

class Payload(db.Model):
    """
    Payload model. Will keep track of description, location, reference to owner.
    """

    pickup_address = db.StringProperty()
    delivery_address = db.StringProperty()

    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
    delivered_at = db.DateTimeProperty()

    latitude = db.FloatProperty()
    longitude = db.FloatProperty()
    # need references to the owner and operator 
    # and users who manipulate

    def __str__(self):
        """
        Return string representation for Payload object
        """
        return 'Payload[%s] Latitude: %s, Longitude %s' % ( self.key().id(), 
                                                            self.latitude, 
                                                            self.longitude )
