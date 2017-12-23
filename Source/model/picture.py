class Picture:

    def __init__(self, photo_id=None, pic_file_path=None, thumbnail_path=None, add_date=None, created_date=None,face_in_pic=None):
        self.photo_id = photo_id
        self.pic_file_path = pic_file_path
        self.thumbnail_path = thumbnail_path
        self.add_date = add_date
        self.created_date = created_date
        self.face_in_pic = face_in_pic

    def __str__(self):
        return f'[Picture] {self.photo_id} {self.pic_file_path} {self.thumbnail_path} {self.add_date} {self.created_date} face in pic {self.face_in_pic}'


