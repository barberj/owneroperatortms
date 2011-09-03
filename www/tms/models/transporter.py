# transporter.py
"""
Transporter model
- vehicle that carries from one place to another
- independent owner operator 
"""

from google.appengine.ext import db

from trackable import Trackable
from contact import Contact

class Transporter(Trackable):
    """
    Transporter model.
    """

    contact = db.ReferenceProperty(Contact, required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
