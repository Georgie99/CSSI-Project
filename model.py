from google.appengine.ext import ndb

class Character(ndb.Model):
    name=ndb.StringProperty(required=True)
    speed=ndb.IntegerProperty(required=True)
    skill=ndb.IntegerProperty(required=True)
    strength=ndb.IntegerProperty(required=True)
    color=ndb.StringProperty(required=True)
    wiki_link=ndb.StringProperty(required=True)
    image_url=ndb.StringProperty()
    up_b=ndb.StringProperty()
    side_b=ndb.StringProperty()
    down_b=ndb.StringProperty()

class User(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email_address = ndb.StringProperty()
  saved_chars = ndb.StringProperty(repeated=True)
