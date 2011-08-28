# transporter.py
"""
Transporter model
- vehicle that carries from one place to another
- independent owner operator 
"""

import logging

from google.appengine.ext import db

from trackable import Trackable

class Transporter(Trackable):
    """
    Transporter model.
    """

    user = db.UserProperty()
