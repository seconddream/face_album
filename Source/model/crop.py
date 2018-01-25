import cv2
import os
import uuid
import model.settings as settings

# this class is responsable for cropping the face out from pictures
class FaceCropper:

    def __init__(self):
        # here i used the pre trained frontal face haar like cascade for the classifier
        self.faceCascade = cv2.CascadeClassifier(settings.haarcascade_path)

    def crop(self, image):
        # determine the size of the cropped face image by the crop ratio in settings
        width = len(image[0])
        height = len(image)
        max_size = max([width, height])
        max_size = int(max_size*settings.crop_ratio)
        cropMinSize = (max_size, max_size)
        # detect face in image, the result are saved in face_position, the x, y, width, hight of the face image in the picutre
        face_positions = self.faceCascade.detectMultiScale(
            image,
            scaleFactor=settings.crop_scale_factor,
            minNeighbors=settings.crop_mini_neighbours,
            minSize=cropMinSize
        )
        return face_positions





