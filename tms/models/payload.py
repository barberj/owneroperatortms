from google.appengine.ext import db
import logging

class Payload(db.Model):
    """
    Payload model. Will keep track of description, location, reference to owner.
    """

    address = db.StringProperty()
    latitude = db.FloatProperty()
    longitude = db.FloatProperty()

    def __init__(self,**kwargs):
        logging.info('Initializing a payload')
        logging.info('Lat %s', kwargs['latitude'])
        logging.info('Long %s', kwargs['longitude'])
        db.Model.__init__(self,**kwargs)
        self.address = kwargs['address']
        self.longitute = kwargs['longitude']
        self.latitude = kwargs['latitude']
