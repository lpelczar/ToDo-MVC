from view import *
from model import Model
import os
import sys
import datetime

MAX_NAME_CHARS = 20
MAX_DESC_CHARS = 150
STARTING_INDEX = 1


class Controller:
    """
    The middle man. Operates on model and updates the view to show information to user.
    """
    OPTIONS = {'1': 'Add Todo Item',
               '2': 'Modify Item',
               '3': 'Delete Item',
               '4': 'Mark Item',
               '5': 'Display Items',
               '6': 'Display Specific Item',
               '7': 'Save tasks to file',
               '8': 'Read from file',
               '0': 'Exit program'}

    def __init__(self):
        self.model = Model()

    def menu(self):
        """
        Show menu to the user and ask to chose option.
        """
        os.system('clear')
        self.show_menu()
        while True:
            option = input('Choose option: ')
            os.system('clear')
            self.show_menu()
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.add_todo_item()
                elif option == '2':
                    self.modify_item()
                elif option == '3':
                    self.delete_item()
                elif option == '4':
                    self.mark_as_done()
                elif option == '5':
                    self.display_items()
                elif option == '6':
                    self.display_specific_item()
                elif option == '7':
                    self.save_to_file()
                elif option == '8':
                    self.read_from_file()
                elif option == '0':
                    sys.exit()

    def show_menu(self):
        """
        Update menu view
        """
        MenuView.display(self.OPTIONS)

    def add_todo_item(self):
        """
        Add to do item to todo_items list and update view
        """
        name = self.ask_name_input()
        description = self.ask_description_input()
        date = self.ask_date_input()
        self.model.add_item(name, description, date)
        AddItemView.display(name)

    def modify_item(self):
        """
        Modify selected item and update view
        """
        index = self.ask_index_input()
        name = self.ask_name_input()
        description = self.ask_description_input()
        date = self.ask_date_input()
        try:
            self.model.modify_item(index, name, description, date)
            ModifyItemView.display(index)
        except IndexError:
            print('Wrong index!')

    def mark_as_done(self):
        """
        Mark selected item as done and update view
        """
        index = self.ask_index_input()
        try:
            self.model.mark_as_done(index)
            MarkItemView.display(index)
        except IndexError:
            print('Wrong index!')

    def delete_item(self):
        """
        Delete selected item and update the view
        """
        index = self.ask_index_input()
        try:
            self.model.delete_item(index)
            DeleteItemView.display(index)
        except IndexError:
            print('Wrong index!')

    def display_items(self):
        """
        Update the view showing all items in todo items list
        """
        DisplayListView.display(self.model.get_items())

    def display_specific_item(self):
        """
        Display selected item by updating the view
        """
        index = self.ask_index_input()
        try:
            item = self.model.get_specific_item(index)
            DisplaySpecificItemView.display(index, item)
        except IndexError:
            print('Wrong index!')

    def save_to_file(self):
        """
        Save all todo items to file
        """
        self.model.save_to_file()

    def read_from_file(self):
        """
        Read todo items from file
        """
        self.model.read_from_file()

    @staticmethod
    def ask_index_input():
        """
        Ask user index input and handle possible exceptions
        :return: int -> index
        """
        while True:
            try:
                index = int(input('Enter index of item: '))
                return index - STARTING_INDEX
            except ValueError:
                print('You need to enter a number!')

    @staticmethod
    def ask_name_input():
        """
        Ask user about todo item name (max 20 characters)
        :returns: string -> name
        """
        while True:
            name = input('Enter name (max 20 characters): ').strip()
            if len(name) > MAX_NAME_CHARS:
                print('Name is too long!')
            else:
                return name

    @staticmethod
    def ask_description_input():
        """
        Ask user about todo item description (max 150 characters)
        :returns: string -> description
        """
        while True:
            description = input('Enter description (max 150 characters): ').strip()
            if len(description) > MAX_DESC_CHARS:
                print('Description is too long!')
            else:
                return description

    @staticmethod
    def ask_date_input():
        """
        Ask user about deadline date for todo item and return it as datetime object
        :returns: Datetime object or None if no date entered
        """
        year_index = 0
        month_index = 1
        day_index = 2

        while True:
            try:
                date = input('Enter date in the following syntax or press enter to add without date: year,month,day ')
                if not date:
                    return None
                date = date.split(',')
                deadline = datetime.date(int(date[year_index]), int(date[month_index]), int(date[day_index]))
                return deadline
            except:
                print('Wrong input!')
