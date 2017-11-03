from todo_item import TodoItem
import csv


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

    def get_specific_item(self, index):
        return self.todo_items[index]

    def save_to_file(self):
        with open('data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for i in self.todo_items:
                writer.writerow([i.name, i.description, i.is_done])

    def read_from_file(self):
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.todo_items.append(TodoItem(row[0], row[1], True if row[2] == 'True' else False))
