from google.appengine.ext import db
import logging

class Payload(db.Model):
    """
    Payload model. Will keep track of description, location, reference to owner.
    """

    address = db.StringProperty()
    latitude = db.FloatProperty()
    longitude = db.FloatProperty()

    def __str__(self):
        """
        Return string representation for Payload object
        """
        return 'Latitude: %s, Longitude %s' % ( self.latitude, self.longitude )
