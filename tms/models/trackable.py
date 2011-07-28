# trackable.py
"""
Trackable model
- capable of being traced or tracked
"""

import logging

from google.appengine.ext import db

class Trackable(db.Model):
    """
    Trackable model.
    """

    latitude = db.FloatProperty()
    longitude = db.FloatProperty()

    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def __str__(self):
        """
        Return string representation for Payload object
        """
        return '[%s] Latitude: %s, Longitude %s' % ( self.key().id(), 
                                                            self.latitude, 
                                                            self.longitude )

