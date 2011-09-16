# payload.py

import logging

from google.appengine.ext import db

"""
Trackable model
- capable of being traced or tracked
"""
class Trackable(db.Model, db.GeoPt):
    """
    Trackable model.
    """

    # the location property is related to
    # the db.GeoPt class
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def __init__(lat,lon):
        super(Trackable,self).__init__(lat=lat,lon=lon)

    def __str__(self):
        """
        Return string representation for Trackable object
        """
        return '[%s] Latitude: %s, Longitude %s' % ( self.key().id(),
                                                     self.lat,
                                                     self.lon )

"""
Payload model
- the load carried by a vehicle exclusive of what is necessary for its operation
"""
from broker import Broker
from transporter import Transporter
from contact import Address
class PlannedPayload(db.Model):
    """
    PlannedPayload model.

    A Payload without a schedule.
    Used to coordinate and see if any drivers are currently avaialable.
    If confirmed would create a Payload.
    """
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    pickup_address = db.ReferenceProperty(Address, collection_name='plannedpayload_pickups')
    delivery_address = db.ReferenceProperty(Address, collection_name='plannedpayload_deliverys')

    broker = db.ReferenceProperty(Broker,
                                    collection_name='planned_payloads', required=True)

    def __str__(self):
        return 'Planned Payload%s' % super(PlannedPayload,self).__str__()

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

    current_location = db.GeoPtProperty()

    coordinates = db.ListProperty(db.Key)

    # need references to the broker and transporter
    # and users who manipulate
    broker = db.ReferenceProperty(Broker,
                                    collection_name='payloads', required=True)

    transporter = db.ReferenceProperty(Transporter,
                                       collection_name='payloads')

    def __str__(self):
        return 'Payload%s' % super(Payload,self).__str__()


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
