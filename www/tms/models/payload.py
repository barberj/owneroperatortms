# payload.py
"""
Payload model
- the load carried by a vehicle exclusive of what is necessary for its operation
"""

import logging

from google.appengine.ext import db

from trackable import Trackable
from broker import Broker
from transporter import Transporter
from contact import Address

class PlannedPayload(Trackable):
    """
    PlannedPayload model.

    A Payload without a schedule.
    Used to coordinate and see if any drivers are currently avaialable.
    If confirmed would create a Payload.
    """

    pickup_address = db.ReferenceProperty(Address, collection_name='plannedpayload_pickups')
    delivery_address = db.ReferenceProperty(Address, collection_name='plannedpayload_deliverys')

    broker = db.ReferenceProperty(Broker,
                                    collection_name='planned_payloads', required=True)

    def __str__(self):
        return 'Planned Payload%s' % super(PlannedPayload,self).__str__()

class Payload(Trackable):
    """
    Payload model.

    A confirmed payload requiring a pickup and delivery on a schedule.
    """

    pickup_address = db.ReferenceProperty(Address, collection_name='pickedup_payloads')
    delivery_address = db.ReferenceProperty(Address, collection_name='delivered_payloads')

    pickedup_at = db.DateTimeProperty()
    delivered_at = db.DateTimeProperty()

    # need references to the broker and transporter
    # and users who manipulate
    broker = db.ReferenceProperty(Broker,
                                    collection_name='payloads', required=True)

    transporter = db.ReferenceProperty(Transporter,
                                       collection_name='payloads')

    def __str__(self):
        return 'Payload%s' % super(PlannedPayload,self).__str__()

    def get_nearby_transporters(self,max_distance=16093):
        """
        Return a list of the transporters available near payload.
        """
        base_query = Transporter.all().filter(available=True)
        return Transporter.proximity_fetch(base_query,
            self.location,
            max_results=10,
            max_distance=max_distance) #within 10 miles
