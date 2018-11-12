from google.appengine.ext import ndb
from user import User

# Model that represents one task in our application
class ToDoItem(ndb.Model):
    title = ndb.StringProperty()
    completed = ndb.BooleanProperty()
    description = ndb.TextProperty()
    dueDate = ndb.DateProperty(auto_now_add = True)
    assigne = ndb.StructuredProperty(User)

