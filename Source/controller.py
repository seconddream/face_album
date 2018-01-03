import sys
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QProgressDialog
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QImage
from PyQt5.QtCore import Qt
from view.main_window import FAMainWindow
from view.view_photo_widget import FAViewPhotoWidget
from view.person_widget import FAPersonWidget
from model.photo_library import PhotoLibrary
from model.face_recognizer import FaceRecognizer
import model.settings as settings
import os


class FAController:
    def __init__(self, app):
        self.PL = PhotoLibrary()
        self.app = app
        self.faceRecognizer = FaceRecognizer()
        self.main_window = FAMainWindow()
        self.main_window.show()
        self.view_photo_widget = FAViewPhotoWidget()
        self.view_photo_widget.hide()
        self.person_widget = FAPersonWidget(self)
        self.person_widget.hide()

        self.cur_displayed_picture = None
        self.cur_displayed_picture_index = None
        self.cur_displayed_picture_id = None
        self.face_toggled = False

        self.face_list_item_update_event = None

        self.connectEvent()
        self.updateThumbnailsList()
        self.updateFaceCB()
        self.updateEmotionCB()

    def connectEvent(self):
        self.main_window.import_btn.clicked.connect(self.importImages)
        self.main_window.thumbnails_list.itemDoubleClicked.connect(self.displayPicture)
        self.main_window.photo_btn.clicked.connect(self.returnToFullLibrary)
        self.main_window.filter_btn.clicked.connect(self.filterLibrary)
        self.main_window.face_btn.clicked.connect(self.showPersonWidget)
        self.view_photo_widget.face_btn.clicked.connect(self.showFaceInPicture)
        self.view_photo_widget.face_list_remove_btn.clicked.connect(self.removeFaceInFaceList)
        self.view_photo_widget.face_list_update_btn.clicked.connect(self.faceUpdate)


    def showPersonWidget(self):
        self.person_widget.show()


    def filterLibrary(self):
        person_id = self.main_window.face_filter_cb.currentData(Qt.UserRole)
        emotion = self.main_window.emotion_filter_cb.currentData(Qt.UserRole)
        print((person_id, emotion))
        self.PL.filterLibrary(person_id, emotion)
        self.updateThumbnailsList()



    def updateEmotionCB(self):
        self.main_window.emotion_filter_cb.clear()
        self.main_window.emotion_filter_cb.addItem('Happy', 'happy')
        self.main_window.emotion_filter_cb.addItem('Sad', 'sadness')
        self.main_window.emotion_filter_cb.addItem('Surprise', 'surprise')

    def updateFaceCB(self):
        self.main_window.face_filter_cb.clear()
        self.PL.loadPersonList()
        for p in self.PL.personList:
            self.main_window.face_filter_cb.addItem(p.name, p.id)

    def returnToFullLibrary(self):
        self.PL.loadLibrary()
        self.updateThumbnailsList()

    def faceUpdate(self):
        n = self.view_photo_widget.face_list.count()
        for i in range(0,n):
            face = self.view_photo_widget.face_list.item(i).data(Qt.UserRole)
            name = self.view_photo_widget.face_list.item(i).text()
            if name != 'Unknown':
                person = self.PL.getPersonByName(name)
                if person is None:
                    person = self.PL.createPerson(name, face.sample_path)
                    face.person_id = person.id
                    face.verified = 1
                    self.PL.updateFaceInPic(face)
                else:
                    face.person_id = person.id
                    face.verified = 1
                    self.PL.updateFaceInPic(face)
        self.faceRecognizer.trainModel()

    def removeFaceInFaceList(self):

        item = self.view_photo_widget.face_list.selectedItems()[0]
        face = item.data(Qt.UserRole)
        self.PL.deleteFaceInPic(face.id)
        self.view_photo_widget.face_list.takeItem(self.view_photo_widget.face_list.row(item))

    def showFaceInPicture(self):
        if self.face_toggled:
            picture_scaled = self.cur_displayed_picture.scaled(self.view_photo_widget.picture_lb.sizeHint(),
                                                               Qt.KeepAspectRatio)
            self.view_photo_widget.picture_lb.setPixmap(picture_scaled)
            self.face_toggled = False
            return

        faces = self.PL.getFacesInPicture(self.cur_displayed_picture_id)
        if faces is None:
            return
        overlay = QPixmap(self.cur_displayed_picture)
        painter = QPainter(overlay)
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(10)
        painter.setPen(pen)
        for face in faces:
            painter.drawRect(face.x, face.y, face.w, face.h)
            emoji = QImage(os.path.join(settings.emoji_path, face.emotion+'.png')).scaled(300,300)
            painter.drawImage(int(face.x+face.w/2-150), (face.y+face.h), emoji)

        painter.end()
        overlay_scaled = overlay.scaled(self.view_photo_widget.picture_lb.sizeHint(), Qt.KeepAspectRatio)
        self.view_photo_widget.picture_lb.setPixmap(overlay_scaled)
        self.face_toggled = True


    def displayPicture(self, item):
        pic_id, index = item.data(0)
        picture = self.PL.getPictureWithID(pic_id)
        self.cur_displayed_picture = QPixmap(picture.file_path)
        self.cur_displayed_picture_index = index
        self.cur_displayed_picture_id = pic_id
        picture_scaled = self.cur_displayed_picture.scaled(self.view_photo_widget.picture_lb.sizeHint(), Qt.KeepAspectRatio)
        self.view_photo_widget.picture_lb.setPixmap(picture_scaled)

        self.view_photo_widget.face_list.clear()
        faces = self.PL.getFacesInPicture(pic_id)
        if faces is None:
            return
        for face in faces:
            face_item = QListWidgetItem(self.view_photo_widget.face_list)
            icon = QIcon(face.sample_path)
            face_item.setIcon(icon)
            if face.person_id is None:
                face_item.setText('Unknown')
            else:
                person = self.PL.getPersonById(face.person_id)
                face_item.setText(person.name)
            face_item.setData(Qt.UserRole, face)
            face_item.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.view_photo_widget.face_list.addItem(face_item)
        self.view_photo_widget.show()


    def importImages(self):
        fname = QFileDialog.getOpenFileNames(self.main_window, 'Open files')
        if fname[0]:
            progress = QProgressDialog('Importing images...', 'Abort', 0, len(fname[0]), self.main_window)
            progress.show()
            for i,  f in enumerate(fname[0]):
                print(f)
                self.PL.importImage(path=f)
                progress.setValue(i)
                self.app.processEvents()
            progress.setValue(len(fname[0]))
            self.PL.loadLibrary()
            self.updateThumbnailsList()

    def updateThumbnailsList(self):
        self.main_window.thumbnails_list.clear()
        if self.PL.library:
            for index, pic in enumerate(self.PL.library):
                item = QListWidgetItem(self.main_window.thumbnails_list)
                icon = QIcon(pic.thumbnail_path)
                item.setIcon(icon)
                item.setData(0, (pic.id, index))
                self.main_window.thumbnails_list.addItem(item)

    def disconnectFaceListSignal(self):
        if self.face_list_item_update_event is not None:
            self.face_list_item_update_event.disconnect()
            self.face_list_item_update_event = None

    def connectFaceListSignal(self):
        if self.face_list_item_update_event is None:
            self.face_list_item_update_event = self.view_photo_widget.face_list.itemChanged.connect(self.faceUpdate)















