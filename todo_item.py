class TodoItem:

    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def modify_item(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        return 'Name: {} Description: {}'.format(self.name, self.description)
