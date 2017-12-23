import os
import cv2
import model.settings as settings


class Cropper:

    def __init__(self):
        if not os.path.exists(settings.person_thumbnail_path):
            os.makedirs(settings.person_thumbnail_path)
        self.faceCascade = cv2.CascadeClassifier(settings.haarcascade_path)

    def cropFaceOut(self):


