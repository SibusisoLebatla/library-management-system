import copy

class BookPrototype:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def clone(self):
        return copy.deepcopy(self)
