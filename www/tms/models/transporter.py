# transporter.py
"""
Transporter model
- vehicle that carries from one place to another
- independent owner operator 
"""

import logging

from google.appengine.ext import db

class Transporter(db.Model):
    """
    Transporter model.
    """

    created_at = db.DateTimeProperty(auto_now_add=True)
