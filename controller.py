from view import *
from model import Model
import os
import sys

MAX_NAME_CHARS = 20
MAX_DESC_CHARS = 150
STARTING_INDEX = 1


class Controller:

    OPTIONS = {'1': 'Add Todo Item',
               '2': 'Modify Item',
               '3': 'Delete Item',
               '4': 'Mark Item',
               '5': 'Display Items',
               '6': 'Display Specific Item',
               '7': 'Exit program'}

    def __init__(self):
        self.model = Model()
        self.menu_view = MenuView()
        self.add_item_view = AddItemView()
        self.modify_item_view = ModifyItemView()
        self.delete_item_view = DeleteItemView()
        self.mark_item_view = MarkItemView()
        self.display_list_view = DisplayListView()
        self.display_specific_item_view = DisplaySpecificItemView()

    def begin(self):
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
                    sys.exit()

    def show_menu(self):
        self.menu_view.display(self.OPTIONS)

    def add_todo_item(self):
        name = self.ask_name_input()
        description = self.ask_description_input()
        self.model.add_item(name, description)
        self.add_item_view.display(name)

    def modify_item(self):
        index = self.ask_index_input()
        name = self.ask_name_input()
        description = self.ask_description_input()
        try:
            self.model.modify_item(index, name, description)
            self.modify_item_view.display(index)
        except IndexError:
            print('Wrong index!')

    def mark_as_done(self):
        index = self.ask_index_input()
        try:
            self.model.mark_as_done(index)
            self.mark_item_view.display(index)
        except IndexError:
            print('Wrong index!')

    def delete_item(self):
        index = self.ask_index_input()
        try:
            self.model.delete_item(index)
            self.delete_item_view.display(index)
        except IndexError:
            print('Wrong index!')

    def display_items(self):
        self.display_list_view.display(self.model.get_items())

    def display_specific_item(self):
        index = self.ask_index_input()
        try:
            item = self.model.get_specific_item(index)
            self.display_specific_item_view.display(item)
        except IndexError:
            print('Wrong index!')

    @staticmethod
    def ask_index_input():
        while True:
            try:
                index = int(input('Enter index of item: '))
                return index - STARTING_INDEX
            except ValueError:
                print('You need to enter a number!')

    @staticmethod
    def ask_name_input():
        while True:
            name = input('Enter name (max 20 characters): ').strip()
            if len(name) > MAX_NAME_CHARS:
                print('Name is too long!')
            else:
                return name

    @staticmethod
    def ask_description_input():
        while True:
            description = input('Enter description (max 150 characters): ').strip()
            if len(description) > MAX_DESC_CHARS:
                print('Description is too long!')
            else:
                return description
