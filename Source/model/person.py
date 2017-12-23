class Person:

    def __init__(self, person_id=None, first_name=None, last_name=None, thumbnail_path=None):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.thumbnail_path = thumbnail_path

    def __str__(self):
        return f'[Person] {self.person_id} {self.first_name} {self.last_name} {self.thumbnail_path}'


