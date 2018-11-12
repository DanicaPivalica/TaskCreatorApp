from base import BaseHandler

# Controller that handles actions regarding items (to-do tasks in our app)
class ItemController(BaseHandler):
    def get(self):
        return self.render_template("index.html")