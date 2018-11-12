from models.item import ToDoItem
from user import UserRepository

# Handles CRUD methods for ToDoItem objects
class ToDoItemRepository():
    @staticmethod
    def create(title, completed, description, dueDate, user_email):
        user = UserRepository.read(email= user_email)
        task = ToDoItem(title=title, completed=completed, description=description, dueDate=dueDate, assigne=user)
        return task.put()

    @staticmethod
    def read(title):
        result = ToDoItem.query(ToDoItem.title == title).fetch(1)
        if result:
            return result

    @staticmethod
    def readAll():
        return ToDoItem.query().order(ToDoItem.title)

    @staticmethod
    def readAllOfUser(user_email):
        user = UserRepository.read(email= user_email)
        return ToDoItem.query(ToDoItem.assigne == user)

    @staticmethod
    def update(title, changes):
        saved_task = ToDoItemRepository.read(title)
        if changes.completed:
            saved_task.completed = changes.completed
        if changes.dueDate:
            saved_task.dueDate = changes.dueDate
        if changes.description:
            saved_task.description = changes.description
        return saved_task.put()

    @staticmethod
    def delete(title):
        saved_task = ToDoItemRepository.read(title)
        saved_task.delete()