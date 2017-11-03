from view import *
from model import Model


class Controller:

    def __init__(self):
        self.model = Model()
        self.menuview = MenuView()

    def show_menu(self):
        self.menuview.display_menu()
