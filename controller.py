from view import MenuView, AddItemView
from model import Model
import os


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
        self.menu_view = MenuView(self.OPTIONS)
        self.add_item_view = AddItemView()

    def begin(self):
        os.system('clear')
        self.show_menu()
        while True:
            option = input('Choose option: ')
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.add_todo_item()
                if option == '2':
                    self.modify_item()

    def show_menu(self):
        self.menu_view.display()

    def add_todo_item(self):
        name = self.ask_name_input()
        description = self.ask_description_input()
        self.model.add_item(name, description)
        self.add_item_view.display(name)

    @staticmethod
    def ask_name_input():
        while True:
            name = input('Enter name (max 20 characters): ')
            if len(name) > 20:
                print('Name is too long!')
            else:
                return name

    @staticmethod
    def ask_description_input():
        while True:
            description = input('Enter description (max 150 characters): ')
            if len(description) > 150:
                print('Description is too long!')
            else:
                return description
