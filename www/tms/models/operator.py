# operator.py
"""
Operator model
- the organization or individual who creates and manages deliveries
"""

from google.appengine.ext import db

class Operator(db.Model):
    """
    Operator Model

    Organization which schedules deliveries and is in need of transport
    Associated to many users who are able to admin over the deliveries
    """

    # users able to admin the account
    users = db.ListProperty(db.Key)

