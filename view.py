class MenuView:

    OPTIONS = {'1': 'Add Todo Item',
               '2': 'Modify Item',
               '3': 'Delete Item',
               '4': 'Mark Item',
               '5': 'Display Items',
               '6': 'Display Specific Item',
               '7': 'Exit program'}

    def __init__(self):
        ...

    def display_menu(self):
        print('Todo App. What do you want to do?')
        for k, v in self.OPTIONS.items():
            print(' {}. {}'.format(k, v))
        print('Enter option: ')


class AddItemView:
    ...


class ModifyItemView:
    ...


class DeleteItemView:
    ...


class MarkItemView:
    ...


class DisplayListView:
    ...


class DisplaySpecificItemView:
    ...
