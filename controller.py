from view import *
from model import Model


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
        self.menuview = MenuView(self.OPTIONS)

    def begin(self):
        self.show_menu()
        while True:
            option = input('Choose option: ')
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.add_todo_item()

    def show_menu(self):
        self.menuview.display_menu()
