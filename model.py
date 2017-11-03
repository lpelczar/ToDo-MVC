from todo_item import TodoItem
import csv
import datetime


class Model:

    def __init__(self):
        self.todo_items = []

    def add_item(self, name, description, deadline):
        self.todo_items.append(TodoItem(name, description, deadline))

    def modify_item(self, index, name, description, deadline):
        self.todo_items[index] = TodoItem(name, description, deadline)

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
                writer.writerow([i.name, i.description, i.deadline if i.deadline else 'None', i.is_done])

    def read_from_file(self):
        name_index = 0
        description_index = 1
        deadline_index = 2
        is_done_index = 3

        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[deadline_index] != 'None':
                    date = row[deadline_index].split('-')
                    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                else:
                    date = None
                self.todo_items.append(TodoItem(row[name_index], row[description_index], date,
                                       True if row[is_done_index] == 'True' else False))
