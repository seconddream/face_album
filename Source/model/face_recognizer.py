import os
import cv2
import model.settings as settings
import model.database_manager as DB
import numpy as np


class FaceRecognizer:
    def __init__(self):
        self.model = cv2.face.LBPHFaceRecognizer_create(threshold=70)
        if not os.path.exists(settings.face_recognizer_model_path):
            self.model.write(settings.face_recognizer_model_path)
        else:
            self.model.read(settings.face_recognizer_model_path)

    def empty(self):
        if self.model.getLabels() is None:
            return True
        else:
            return False

    def loadImage(self, path):
        image = cv2.imread(path, 0)
        image = cv2.equalizeHist(image)
        image = cv2.blur(image, settings.face_training_image_blur_ksize)
        return image

    def predict(self):
        face_list = DB.getAllFaceInPic()
        unverified_face_list = [f for f in face_list if f.verified == -1]
        for face in unverified_face_list:
            test = self.loadImage(face.sample_path)
            label, confident = self.model.predict(test)
            if label != -1:
                face.person_id = label
                DB.updateFaceInPic(face)

    def trainModel(self):
        person_list = DB.getAllPerson()
        if person_list is None:
            return
        if len(person_list)<2:
            return
        face_list = DB.getAllFaceInPic()
        verified_face_list = [f for f in face_list if f.verified == 1]
        if len(verified_face_list)<10:
            return
        training_images = []
        training_labels = []
        for face in verified_face_list:
            print(f'training with face {face}')
            training_images.append(self.loadImage(face.sample_path))
            training_labels.append(face.person_id)

        self.model.train(training_images, np.array(training_labels))
        # self.model.write(settings.face_recognizer_model_path)
        self.predict()



















