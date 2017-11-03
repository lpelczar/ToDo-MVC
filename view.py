STARTING_INDEX = 1


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
        print('Item {} successfully modified!'.format(index + STARTING_INDEX))


class DeleteItemView:

    @staticmethod
    def display(index):
        print('Item {} has been successfully deleted!'.format(index + STARTING_INDEX))


class MarkItemView:

    @staticmethod
    def display(index):
        print('Item {} successfully marked as done!'.format(index + STARTING_INDEX))


class DisplayListView:

    @staticmethod
    def display(items):
        for k, v in enumerate(items):
            print(k + STARTING_INDEX, v)


class DisplaySpecificItemView:

    @staticmethod
    def display(item):
        print(item, '--', item.description)
