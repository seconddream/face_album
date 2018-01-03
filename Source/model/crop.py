import cv2
import os
import uuid
import model.settings as settings


class FaceCropper:

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier(settings.haarcascade_path)

    def crop(self, image):

        width = len(image[0])
        height = len(image)
        max_size = max([width, height])

        max_size = int(max_size*settings.crop_ratio)

        cropMinSize = (max_size, max_size)

        face_positions = self.faceCascade.detectMultiScale(
            image,
            scaleFactor=settings.crop_scale_factor,
            minNeighbors=settings.crop_mini_neighbours,
            minSize=cropMinSize
        )
        return face_positions





