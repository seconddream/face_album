from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt
from view.ui_view_photo_widget import Ui_ViewPhotoWidget
import model.database_manager as DB


class FAViewPhotoWidget(QWidget, Ui_ViewPhotoWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.picture_id = None
        self.picture = None
        self.face_thumbnail = None










