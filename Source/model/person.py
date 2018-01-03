class Person:

    def __init__(self, id=None, name=None, thumbnail_path=None):
        self.id = id
        self.name = name
        self.thumbnail_path = thumbnail_path

    def __str__(self):
        return f'[Person] {self.id} {self.name} {self.thumbnail_path}'


