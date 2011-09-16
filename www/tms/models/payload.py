# payload.py

import logging

from google.appengine.ext import db

from contact import Address
from broker import Broker
from transporter import Transporter

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

    current_coordinates = db.GeoPtProperty()
    coordinates = db.ListProperty(db.GeoPt,default=None)

    # need references to the broker and transporter
    # and users who manipulate
    broker = db.ReferenceProperty(Broker,
                                    collection_name='payloads')#, required=True)

    transporter = db.ReferenceProperty(Transporter,
                                       collection_name='payloads')

    def __init__(self,*args,**kwargs):
        key = super(Payload,self).__init__(*args,**kwargs)
        self.coordinates.append(self.current_coordinates)
        return key

    def __str__(self):
        if self.current_coordinates:
            return 'Payload[%s] at Longitude %s, Latitude %s' % ( self.key().id(),
                                                                  self.current_coordinates.lon,
                                                                  self.current_coordinates.lat ) 
        return 'Payload[%s] coordinates are unknown' % self.key().id()

    def set_location(self, latitude, longitude):
        """
        Update Payload location.
        """

        new_coordinate = Trackable(lat=latitude,lon=longitude)
        self.coordinates.append(new_coordinate)
        self.current_location = new_coordinate

        return self.current_location

    def get_nearby_transporters(self,max_distance=16093):
        """
        Return a list of the transporters available near payload.
        """
        base_query = Transporter.all().filter('available =',True)
        return Transporter.proximity_fetch(base_query,
            self.current_location,
            max_results=10,
            max_distance=max_distance) #within 10 miles
