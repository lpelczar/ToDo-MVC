class TodoItem:
    """
    Class TodoItem represents a single todo item

    Attributes:
    :param name: String -> name of the task
    :param description: String -> description of the task
    :param deadline: Datetime object -> deadline of the task, default: None
    :param is_done: bool -> True if task is done else False, default: False
    """
    def __init__(self, name, description, deadline=None, is_done=False):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_done = is_done

    def mark_as_done(self):
        self.is_done = True
        self.deadline = None

    def __str__(self):
        """
        Return string representation of a task
        """
        mark = 'X' if self.is_done else ' '
        return '[{}] {}'.format(mark, self.name)
