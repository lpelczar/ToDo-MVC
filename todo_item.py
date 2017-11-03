class TodoItem:

    def __init__(self, name, description, deadline=None, is_done=False):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_done = is_done

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        mark = 'X' if self.is_done else ' '
        return '[{}] {}'.format(mark, self.name)
