import os
import cv2
import uuid
import model.settings as settings
from datetime import datetime
import model.database_manager as DB
from model.face_recognizer import FaceRecognizer
from model.crop import FaceCropper
from model.facial_expression import ExpressionDetector

# the main model of the app, the libaray
class PhotoLibrary:

    def __init__(self):
        self.faceCropper = FaceCropper()
        # the variable that holds all the pictures in the library
        self.library = None
        # the variable that holds all the people in the library
        self.personList = None
        self.faceRecognizer = FaceRecognizer()
        # load the library
        self.loadLibrary()
        # load the person info
        self.loadPersonList()
        self.expressionDetector = ExpressionDetector()
# the function follows use the database_manager to do database task
    def loadLibrary(self):
        self.library = DB.getAllPictures()

    def filterLibrary(self, id, emotion):
        self.library = DB.getPicWithPersonAndEmotion(id, emotion)

    def loadPersonList(self):
        self.personList = DB.getAllPerson()

    def createPerson(self, name, thumbnail_path):
        return DB.createNewPerson(name,thumbnail_path)

    def updatePerson(self, person):
        DB.updatePerson(person)

    def getPictureWithID(self, pic_id):
        picture = DB.getPictureByID(pic_id)
        if picture is not None:
            return picture
        else:
            return None

    def getFacesInPicture(self, pic_id):
        return DB.getFaceInPic(pic_id)

    def getPersonByName(self, name):
        return DB.getPersonByName(name)

    def updateFaceInPic(self, face):
        DB.updateFaceInPic(face)

    def getPersonById(self, id):
        return DB.getPersonById(id)

    def generatePictureThumbnail(self, image):
        width = settings.picture_thumbnail_width
        height = int(len(image)*width/len(image[0]))
        picture_thumbnail = cv2.resize(image, (width, height))
        return picture_thumbnail

    def loadImageFromDisk(self, path):
        return cv2.imread(path)

    def deleteFaceInPic(self, face_id):
        DB.deleteFaceInPic(face_id)


    def importImage(self, path):
        image = self.loadImageFromDisk(path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_thumbnail = self.generatePictureThumbnail(image)
        file_name = str(uuid.uuid4()) + '.jpg'



        #save picture
        picture_path = os.path.join(settings.picture_path, file_name)
        try:
            cv2.imwrite(picture_path, image)
        except Exception as err:
            print(f'[PhotoLibrary/importImage]: can not write picture {err}')
            return False

        #save thumbnail
        picture_thumbnail_path = os.path.join(settings.picture_thumbnail_path, file_name)
        try:
            cv2.imwrite(picture_thumbnail_path, image_thumbnail)
        except Exception as err:
            print(f'[PhotoLibrary/importImage]: can not write picture thumbnail {err}')
            return False

        #write database
        picture = DB.createPicture(picture_path, picture_thumbnail_path, datetime.now())
        if picture is None:
            return False

        # crop the face out and pre-process it for later handling, save the image into training set
        face_positions = self.faceCropper.crop(image_gray)
        for position in face_positions:
            x, y, w, h = position
            # pre-process steps: resize, smoothing, histo eql
            face_image = image[y:(y+h), x:(x+w)]
            face_image = cv2.resize(face_image, settings.face_training_image_size)
            # face_image = cv2.blur(face_image, settings.face_training_image_blur_ksize)
            # face_image = cv2.equalizeHist(face_image)
            face_image_file_name = str(uuid.uuid4())+'.jpg'
            face_image_file_path = os.path.join(settings.face_training_image_path, face_image_file_name)
            # write to disk
            try:
                cv2.imwrite(face_image_file_path, face_image)
            except Exception as err:
                print(f'[PhotoLibrary/importImage]: can not write training image {err}')

            # determine emotion
            emotion = self.expressionDetector.test_emotion(face_image_file_path)
            # write to database
            DB.createFaceInPic(picture.id, int(x), int(y), int(w), int(h), face_image_file_path, emotion)







































