from google.appengine.ext import ndb
from datetime import date

# Model for a user that's going to be an assigne of a created task.
class User(ndb.Model):
    first_name = ndb.StringProperty()
    email = ndb.StringProperty()
    date_of_birth = ndb.DateProperty()
    # not an accurate calculation
    age = ndb.ComputedProperty(lambda self: date.today().year - self.date_of_birth.year)

