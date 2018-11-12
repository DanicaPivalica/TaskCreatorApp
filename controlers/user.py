from base import BaseHandler
from repositories.user import UserRepository
from datetime import date
import time

# UserController - handles all user related requests
class UserController(BaseHandler):
    def get(self):
        existing_users = UserRepository.readAll()
        return self.render_template("/user/user_list.html", params={"userList": existing_users })

    # custom method - used to handle specific user data
    def get_user(self, email = None):
        existing_user = UserRepository.read(email)
        return self.render_template("/user/user_display.html", params={ "user": existing_user })

    # custom method - handles GET request for user creation
    def create_get(self):
        return  self.render_template("/user/user_create.html")

    # custom method - handles POST request for user creation
    def create_post(self):
        email = self.request.get("email")
        first_name = self.request.get("first_name")
        form_date = self.request.get("date_of_birth").split('-')
        date_of_birth = date(int(form_date[0]),int(form_date[1]),int(form_date[2]))
        new_user = UserRepository.create(first_name=first_name, email=email, date_of_birth=date_of_birth)
        # adding lag for local development
        time.sleep(1)
        return self.redirect_to('user-list')