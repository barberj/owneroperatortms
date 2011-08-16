# broker.py
"""
Broker model
- transporter firm that acts as an agent for a shipper to commission
    a transporter
"""

import logging

from google.appengine.ext import db

class Broker(db.Model):
    """
    Broker model.
    """

    created_at = db.DateTimeProperty(auto_now_add=True)
