# hooked_module.py
"""
Monkey patching db.Model
"""
from google.appengine.api import datastore
from google.appengine.ext import db


# TY Nick: http://blog.notdot.net/2010/04/Pre--and-post--put-hooks-for-Datastore-models
old_put = db.put
def hooked_put(models, **kwargs):
    print 'hooked'
    for model in models:
        if isinstance(model, HookedModel):
            print 'hi'
            print model 
            model.before_put()
    key = old_put(model, **kwargs)
    for model in models:
        if isinstance(model, HookedModel):
            model.after_put()
    return key
db.put = hooked_put

class HookedModel(db.Model):
    def before_put(self):
        pass

    def after_put(self):
        pass

    def put(self,**kwargs):
        self.before_put()
        key = super(HookedModel, self).put(**kwargs)
        #config = datastore._GetConfigFromKwargs(kwargs)
        #self._populate_internal_entity()
        #key= datastore.Put(self._entity, config=config)
        #db.put(self)
        self.after_put()
        return key
