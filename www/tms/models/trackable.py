# trackable.py
"""
Trackable model
- capable of being traced or tracked
"""

import logging

from google.appengine.ext import db

import geo.geomodel

class Trackable(geo.geomodel.GeoModel):
    """
    Trackable model.
    """

    # the location property is related to
    # the db.GeoPt class

    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def __str__(self):
        """
        Return string representation for Payload object
        """
        return '[%s] Latitude: %s, Longitude %s' % ( self.key().id(),
                                                     self.location.lat,
                                                     self.location.lon )

    def set_location(self,lat,lng):
        """
        updates the GeoPt location of the trackable
        does not do .put()
        """

        self.location = db.GeoPt(lat,lng)
        self.update_location()
