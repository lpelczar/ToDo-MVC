STARTING_INDEX = 1


class MenuView:
    """
    View which shows the menu of the program
    """
    @staticmethod
    def display(options):
        """
        :param options: dict -> dictionary with number keys and option names values for menu
        """
        print('Todo App. What do you want to do?')
        for k, v in options.items():
            print(' {}. {}'.format(k, v))
        print(' ')


class AddItemView:
    """
    View which shows the result of adding new item to tasks list
    """
    @staticmethod
    def display(name):
        """
        :param name: String -> name of the todo item
        """
        print('Item {} successfully added to list!'.format(name))


class ModifyItemView:
    """
    View which shows the result of modifying the item in task list
    """
    @staticmethod
    def display(index):
        """
        :param index: int -> index of the specific item
        """
        print('Item {} successfully modified!'.format(index + STARTING_INDEX))


class DeleteItemView:
    """
    View which shows the result of deleting item in task list
    """
    @staticmethod
    def display(index):
        """
        :param index: int -> index of the specific item
        """
        print('Item {} has been successfully deleted!'.format(index + STARTING_INDEX))


class MarkItemView:
    """
    View which shows the result of marking item as done
    """
    @staticmethod
    def display(index):
        """
        :param index: int -> index of the specific item
        """
        print('Item {} successfully marked as done!'.format(index + STARTING_INDEX))


class DisplayListView:
    """
    View which shows the list of all todo items
    """
    @staticmethod
    def display(items):
        """
        :param items: list -> list of todo items objects
        """
        if not items:
            print('List is empty!')
        else:
            for k, v in enumerate(items):
                print(k + STARTING_INDEX, v.deadline if v.deadline else '', v)


class DisplaySpecificItemView:
    """
    View which shows the specific item informations: deadline, index, is_done, name, description
    """
    @staticmethod
    def display(index, item):
        """
        :param index: int -> index of the specific item
        :param item: TodoItem -> single TodoItem object
        """
        print(index + STARTING_INDEX, item.deadline if item.deadline else '', item, '->', item.description)
