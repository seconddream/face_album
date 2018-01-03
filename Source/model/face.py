class Face:

    def __init__(self, id=None, person_id=None, picture_id=None, x=None, y=None, w=None, h=None, emotion=None, sample_path=None, verified=None):
        self.id = id
        self.picture_id = picture_id
        self.person_id = person_id
        self.emotion = emotion
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sample_path = sample_path
        self.verified = verified

    def __str__(self):
        return f'face: {self.id} {self.sample_path}'


    