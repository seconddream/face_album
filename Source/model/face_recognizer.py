import os
import cv2
import model.settings as settings
import model.database_manager as DB
import numpy as np

# this class is for facial recognition
class FaceRecognizer:
    def __init__(self):
        # init the LBPH model
        self.model = cv2.face.LBPHFaceRecognizer_create(threshold=70)
        if not os.path.exists(settings.face_recognizer_model_path):
            # save the newly created model on disk
            self.model.write(settings.face_recognizer_model_path)
        else:
            # load it if it is already exist
            self.model.read(settings.face_recognizer_model_path)
    # check if the model contains no label, that is if the model is trained
    def empty(self):
        if self.model.getLabels() is None:
            return True
        else:
            return False
    # helper function to load a traning image on disk
    def loadImage(self, path):
        image = cv2.imread(path, 0)
        image = cv2.equalizeHist(image)
        image = cv2.blur(image, settings.face_training_image_blur_ksize)
        return image
    # predict face name in the library
    def predict(self):
        # load all face that is detected
        face_list = DB.getAllFaceInPic()
        # find out those are not verified, verified face will not be give to the classification model
        unverified_face_list = [f for f in face_list if f.verified == -1]
        for face in unverified_face_list:
            test = self.loadImage(face.sample_path)
            # get the predicted label
            label, confident = self.model.predict(test)
            # if the label is not -1 then, the face is recognized by the model
            if label != -1:
                # use the labe as the person id of the face
                face.person_id = label
                # write in database face in pic
                DB.updateFaceInPic(face)

    def trainModel(self):
        # check if there is enough samples for training in db
        person_list = DB.getAllPerson()
        if person_list is None:
            return
        # at least 2 person are inside the db
        if len(person_list)<2:
            return
        face_list = DB.getAllFaceInPic()
        verified_face_list = [f for f in face_list if f.verified == 1]
        # at least 10 faces are detected
        if len(verified_face_list)<10:
            return
        # prepare the training data set and labels
        training_images = []
        training_labels = []
        # train the model with only verified face, use the sample image as sample data, the person id as label
        for face in verified_face_list:
            print(f'training with face {face}')
            training_images.append(self.loadImage(face.sample_path))
            training_labels.append(face.person_id)

        self.model.train(training_images, np.array(training_labels))
        # after training, run the predict funtion of this class to do a prediction of all the other faces(not verified)
        self.predict()



















