from google.appengine.ext import ndb

class Character(ndb.Model):
    name=ndb.StringProperty(required=True)
    speed=ndb.IntegerProperty(required=True)
    skill=ndb.IntegerProperty(required=True)
    strength=ndb.IntegerProperty(required=True)
    color=ndb.StringProperty(required=True)
    wiki_link=ndb.StringProperty(required=True)
    #sm=ndb.UserProperty(required=True)
    #we had problems putting it as a dic thinking of making seperate properties
