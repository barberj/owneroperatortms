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

from lepl.apps.rfc3696 import Email

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
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def __str__(self):
        """
        Return string represenation for Contact object
        """
        return '%s %s' % (self.first_name, self.last_name)

    def delete(self):
        """
        Implementing cascading deletes
        """

        # delete all relations
        for email in self.emailaddresses:
            email.delete()

        for phone_num in self.phone_numbers:
            phone_num.delete() 

        for address in self.addresses:
            address.delete()

        # finally delete self 
        db.delete(self)

class Address(db.Model):
    """
    Address model.
    """

    address_type = db.ReferenceProperty(PropertyType)
    address = db.PostalAddressProperty()
    contact = db.ReferenceProperty(Contact,collection_name='addresses')
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class EmailAddress(db.Model):
    """
    EmailAddress model.
    """

    email_type = db.ReferenceProperty(PropertyType)
    emailaddress = db.EmailProperty()
    contact = db.ReferenceProperty(Contact,collection_name='emailaddresses')
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

    def before_put(self):
        """
        Before we save to the Datastore we want to
        validate its an email
        """

        validator = Email()
        return validator(self.emailaddress)

    def put(self):
        """
        Save to Datastore
        """
        
        if self.before_put():
            super(EmailAddress,self).put()
        else:
            raise Exception('Invalid EmailAddress')

    def __str__(self):
        return self.emailaddress

    def delete(self):
        """
        Implementing cascading deletes
        """

        # delete all relations
        # in reality there should 
        # only be one user in the set
        for user in self.user_set:
            user.delete()

        # finally delete self
        db.delete(self)
        

class PhoneNumber(db.Model):
    """
    PhoneNumber model.
    """
    
    phone_type = db.ReferenceProperty(PropertyType)
    phone_number = db.PhoneNumberProperty(required=True)
    contact = db.ReferenceProperty(Contact,collection_name='phone_numbers')
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)

class User(db.Model):
    """
    User model.
    """

    username = db.ReferenceProperty(EmailAddress)
    password = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
