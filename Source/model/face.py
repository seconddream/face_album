# this class is for store a detected face in a picture
class Face:

    def __init__(self, id=None, person_id=None, picture_id=None, x=None, y=None, w=None, h=None, emotion=None, sample_path=None, verified=None):
        self.id = id
        self.picture_id = picture_id
        self.person_id = person_id
        self.emotion = emotion
        # x, y, width, height for this face in that picture
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # the cropped out sample path stored on disk
        self.sample_path = sample_path
        # if a face is give a name by the user, or the predicted name is confirmed by user, then verified is 1
        self.verified = verified

    def __str__(self):
        return f'face: {self.id} {self.sample_path}'


    