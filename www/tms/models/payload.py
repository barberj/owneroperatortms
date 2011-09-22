# payload.py

import logging

from google.appengine.ext import db

from contact import Address
from broker import Broker
from transporter import Transporter

"""
Trackable model
- capable of being traced or tracked
"""
class Trackable(db.Model):
    """
    Trackable model.
    """

    # the location property is related to
    # the db.GeoPt class
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
    coordinates = db.GeoPtProperty()

    def __str__(self):
        """
        Return string representation for Trackable object
        """
        return '[%s] Latitude: %s, Longitude %s' % ( self.key().id(),
                                                     self.coordinates.lat,
                                                     self.coordinates.lon )

    def __init__(self,lat=None,lon=None,*args,**kwargs):
        key = super(Trackable,self).__init__(*args,**kwargs)
        if lat and lon:
            self.coordinates=db.GeoPt(lat=lat,lon=lon)
        return key

    def set_location(self,lat,lng):
        """
        updates the GeoPt location of the trackable
        does not do .put()
        """
        self.location = db.GeoPt(lat,lng)

class Payload(db.Model):
    """
    Payload model.

    A confirmed payload requiring a pickup and delivery on a schedule.
    """
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    pickup_address = db.ReferenceProperty(Address, collection_name='pickedup_payloads')
    delivery_address = db.ReferenceProperty(Address, collection_name='delivered_payloads')

    pickedup_at = db.DateTimeProperty()
    delivered_at = db.DateTimeProperty()

    current_coordinates = db.ReferenceProperty(Trackable)
    coordinates = db.ListProperty(db.Key,default=None)

    # need references to the broker and transporter
    # and users who manipulate
    broker = db.ReferenceProperty(Broker,
                                    collection_name='payloads')#, required=True)

    transporter = db.ReferenceProperty(Transporter,
                                       collection_name='payloads')

    def __init__(self,lat=None,lon=None,*args,**kwargs):
        key = super(Payload,self).__init__(*args,**kwargs)
        if lat and lon:
            self.update_location(lat,lon)
        return key

    def __str__(self):
        if self.current_coordinates:
            return 'Payload[%s] at Longitude %s, Latitude %s' % ( self.key().id(),
                                                                  self.current_coordinates.coordinates.lon,
                                                                  self.current_coordinates.coordinates.lat ) 
        return 'Payload[%s] coordinates are unknown' % self.key().id()

    def update_location(self, lat, lon):
        """
        Update Payload location.
        """

        trackable = Trackable(lat=lat,lon=lon).put()
        self.current_coordinates=Trackable.get(trackable)
        self.coordinates.append(trackable)
        return self.current_coordinates

    def delete(self):
        """
        Don't orphan the coordinates!
        """

        self.current_coordinates=None
        for coordinates in self.coordinates:
            Trackable.get(coordinates).delete()
        db.delete(self)

    def get_nearby_transporters(self,max_distance=16093):
        """
        Return a list of the transporters available near payload.
        """
        base_query = Transporter.all().filter('available =',True)
        return Transporter.proximity_fetch(base_query,
            self.current_location,
            max_results=10,
            max_distance=max_distance) #within 10 miles
