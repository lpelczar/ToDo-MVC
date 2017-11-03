from todo_item import TodoItem


class Model:

    def __init__(self):
        self.todo_items = []

    def add_item(self, name, description):
        self.todo_items.append(TodoItem(name, description))

    def modify_item(self, index, name, description):
        self.todo_items[index] = TodoItem(name, description)

    def mark_as_done(self, index):
        self.todo_items[index].mark_as_done()

    def delete_item(self, index):
        self.todo_items.pop(index)

    def get_items(self):
        return self.todo_items
