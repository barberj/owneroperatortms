# payload.py
"""
Payload model
- the load carried by a vehicle exclusive of what is necessary for its operation
"""

import logging

from google.appengine.ext import db

from trackable import Trackable
from operator import Operator
from transporter import Transporter

class PlannedPayload(Trackable):
    """
    PlannedPayload model.

    A Payload without a schedule.
    Used to coordinate and see if any drivers are currently avaialable.
    If confirmed would create a Payload.
    """

    pickup_address = db.StringProperty()
    delivery_address = db.StringProperty()

    operator = db.ReferenceProperty(Operator,
                                    collection_name='planned_payloads')

    def __str__(self):
        return 'Planned Payload%s' % super(PlannedPayload,self).__str__()

class Payload(PlannedPayload):
    """
    Payload model.

    A confirmed payload requiring a pickup and delivery on a schedule.
    """

    pickedup_at = db.DateTimeProperty()
    delivered_at = db.DateTimeProperty()
    # need references to the owner and operator
    # and users who manipulate

    transporter = db.ReferenceProperty(Transporter,
                                       collection_name='payloads')

    def __str__(self):
        return 'Payload%s' % super(PlannedPayload,self).__str__()
