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

    # available will be toggled when loaded and transporting
    # or when a transporter simple isn't working
    available = db.BooleanProperty(default=True)
