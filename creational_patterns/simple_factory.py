class Book:
    def __init__(self, title):
        self.title = title

class DVD:
    def __init__(self, title):
        self.title = title

class LibraryItemFactory:
    @staticmethod
    def create_item(item_type, title):
        if item_type == "book":
            return Book(title)
        elif item_type == "dvd":
            return DVD(title)
        else:
            raise ValueError("Invalid item type")
