class MenuView:

    def __init__(self, options):
        self.options = options

    def display_menu(self):
        print('Todo App. What do you want to do?')
        for k, v in self.options.items():
            print(' {}. {}'.format(k, v))


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
