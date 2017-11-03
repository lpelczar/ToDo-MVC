from todo_item import TodoItem


class Model:

    def __init__(self):
        self.todo_items = []

    def add_item(self, name, description):
        self.todo_items.append(TodoItem(name, description))

    def modify_item(self, index, name, description):
        self.todo_items[index] = TodoItem(name, description)
