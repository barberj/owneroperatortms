# broker.py
"""
Broker model
- the organization or individual who creates and manages deliveries
- transporter firm that acts as an agent for a shipper to commission
    a transporter
"""

from google.appengine.ext import db

class Broker(db.Model):
    """
    Broker model.
    
    Organization which schedules deliveries and is in need of transport
    Associated to many users who are able to admin over the deliveries
    """

    created_at = db.DateTimeProperty(auto_now_add=True)
