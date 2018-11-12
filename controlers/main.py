from base import BaseHandler

# MainController - handles root route load
class MainController(BaseHandler):
    def get(self):
        return self.render_template("index.html")