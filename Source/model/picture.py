class Picture:

    def __init__(self, id=None, file_path=None, thumbnail_path=None, add_date=None):
        self.id = id
        self.file_path = file_path
        self.thumbnail_path = thumbnail_path
        self.add_date = add_date

    def __str__(self):
        return f'[Picture] {self.id} {self.file_path} {self.thumbnail_path} {self.add_date}'


