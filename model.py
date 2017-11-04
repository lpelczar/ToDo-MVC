from todo_item import TodoItem
import csv
import datetime


class Model:
    """
    Stores todo items in a list and operates on the items in list.
    """
    def __init__(self):
        self.todo_items = []

    def add_item(self, name, description, deadline):
        """
        Add item to todo items list
        :param name: string -> name of the todo item
        :param description: string -> description of the todo item
        :param deadline: Datetime -> deadline of the todo item
        """
        self.todo_items.append(TodoItem(name, description, deadline))

    def modify_item(self, index, name, description, deadline):
        """
        Modify item by index
        :param index: int -> index of item we want to modify
        :param name: string -> name of the todo item
        :param description: string -> description of the todo item
        :param deadline: Datetime -> deadline of the todo item
        """
        self.todo_items[index] = TodoItem(name, description, deadline)

    def mark_as_done(self, index):
        """
        Mark item with specific index as done
        :param index: int -> index of the item
        """
        self.todo_items[index].mark_as_done()

    def delete_item(self, index):
        """
        Deletes item with specific index
        :param index: int -> index of the item
        """
        self.todo_items.pop(index)

    def get_items(self):
        """
        Returns list of todo items
        :returns: list
        """
        return self.todo_items

    def get_specific_item(self, index):
        """
        Returns specific todo item from list by index
        :param index: int -> index of the item we want to get
        :returns: Todo Item -> Todo Item object
        """
        return self.todo_items[index]

    def save_to_file(self):
        """
        Save all items in todo items list to file 'data.csv'
        """
        with open('data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for i in self.todo_items:
                writer.writerow([i.name, i.description, i.deadline if i.deadline else 'None', i.is_done])

    def read_from_file(self):
        """
        Read items from file and append all items to todo items list
        """
        name_index = 0
        description_index = 1
        deadline_index = 2
        is_done_index = 3
        year_index = 0
        month_index = 1
        day_index = 2

        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[deadline_index] != 'None':
                    date = row[deadline_index].split('-')
                    date = datetime.date(int(date[year_index]), int(date[month_index]), int(date[day_index]))
                else:
                    date = None
                self.todo_items.append(TodoItem(row[name_index], row[description_index], date,
                                       True if row[is_done_index] == 'True' else False))
