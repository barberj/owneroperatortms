# contact.py
"""
User model
- uses or operates something
    In this case the user model is the credentials a 
       user would use to access the system.
    User can be associated with broker, transporter, or broker_client
       via a contact.
"""
import logging
from google.appengine.ext import db

class PropertyType(db.Model):
    """
    PropertyType model. Is it Work, Home, Cell or Other.
    """

    ptype = db.StringProperty()
    
    def __str__(self):
        """
        Return string representation
        """
        return self.ptype

class Contact(db.Model):
    """
    Contact model.
    """

    first_name = db.StringProperty()
    last_name = db.StringProperty()

    def __str__(self):
        """
        Return string represenation for Contact object
        """
        return '%s %s' % (self.first_name, self.last_name)

class Address(db.Model):
    """
    Address model.
    """

    address_type = db.ReferenceProperty(PropertyType)
    address = db.PostalAddressProperty()
    contact = db.ReferenceProperty(Contact,collection_name='addresses')

class EmailAddress(db.Model):
    """
    EmailAddress model.
    """

    email_type = db.ReferenceProperty(PropertyType)
    emailaddress = db.EmailProperty()
    contact = db.ReferenceProperty(Contact,collection_name='emailaddresses')

    def __str__(self):
        return self.emailaddress

class PhoneNumber(db.Model):
    """
    PhoneNumber model.
    """
    
    phone_type = db.ReferenceProperty(PropertyType)
    phone_number = db.PhoneNumberProperty(required=True)
    contact = db.ReferenceProperty(Contact,collection_name='phone_numbers')

class User(db.Model):
    """
    User model.
    """

    username = db.ReferenceProperty(EmailAddress)
    password = db.StringProperty()
