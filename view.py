class MenuView:

    @staticmethod
    def display(options):
        print('Todo App. What do you want to do?')
        for k, v in options.items():
            print(' {}. {}'.format(k, v))
        print(' ')


class AddItemView:

    @staticmethod
    def display(name):
        print('Item {} successfully added to list!'.format(name))


class ModifyItemView:

    @staticmethod
    def display(index):
        print('Item {} successfully modified!'.format(index + 1))


class DeleteItemView:

    @staticmethod
    def display(index):
        print('Item {} has been successfully deleted!'.format(index + 1))


class MarkItemView:

    @staticmethod
    def display(index):
        print('Item {} successfully marked as done!'.format(index + 1))


class DisplayListView:

    @staticmethod
    def display(items):
        for k, v in enumerate(items):
            print(k + 1, v)


class DisplaySpecificItemView:

    @staticmethod
    def display(item):
        print(item, '--', item.description)
