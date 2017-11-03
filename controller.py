from view import MenuView, AddItemView, ModifyItemView, DeleteItemView, MarkItemView, DisplayListView
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
        self.modify_item_view = ModifyItemView()
        self.delete_item_view = DeleteItemView()
        self.mark_item_view = MarkItemView()
        self.display_list_view = DisplayListView()

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

    def show_menu(self):
        self.menu_view.display()

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
        except IndexError:
            print('Wrong index!')
        self.modify_item_view.display(index)

    def mark_as_done(self):
        index = self.ask_index_input()
        try:
            self.model.mark_as_done(index)
        except IndexError:
            print('Wrong index!')
        self.mark_item_view.display(index)

    def delete_item(self):
        index = self.ask_index_input()
        try:
            self.model.delete_item(index)
        except IndexError:
            print('Wrong index!')
        self.delete_item_view.display(index)

    def display_items(self):
        self.display_list_view.display(self.model.get_items())

    @staticmethod
    def ask_index_input():
        while True:
            try:
                index = int(input('Enter index of item: '))
                return index - 1
            except ValueError:
                print('You need to enter a number!')

    @staticmethod
    def ask_name_input():
        while True:
            name = input('Enter name (max 20 characters): ').strip()
            if len(name) > 20:
                print('Name is too long!')
            else:
                return name

    @staticmethod
    def ask_description_input():
        while True:
            description = input('Enter description (max 150 characters): ').strip()
            if len(description) > 150:
                print('Description is too long!')
            else:
                return description
