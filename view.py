class MenuView:

    def __init__(self, options):
        self.options = options

    def display(self):
        print('Todo App. What do you want to do?')
        for k, v in self.options.items():
            print(' {}. {}'.format(k, v))


class AddItemView:

    @staticmethod
    def display(name):
        print('Item {} successfully added to list!'.format(name))


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
