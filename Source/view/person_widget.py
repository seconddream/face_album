from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from view.ui_person_widget import Ui_PersonWidget
import model.database_manager as DB


class FAPersonWidget(QWidget, Ui_PersonWidget):

    def __init__(self, mainController):
        super().__init__()
        self.setupUi(self)
        self.persons = None
        self.connectEvents()
        self.mainController = mainController
        self.updatePersonList()

    def connectEvents(self):
        self.person_list.itemClicked.connect(self.faceSelected)
        self.update_btn.clicked.connect(self.updatePerson)
        self.delete_btn.clicked.connect(self.deletePerson)

    def updatePerson(self):
        person = self.person_list.currentItem().data(Qt.UserRole)
        if person is None:
            return
        new_name = self.name_cb.currentText()
        if new_name != '' and new_name is not None and person is not None:
            person.name = new_name
            DB.updatePerson(person)
            self.updatePersonList()

    def deletePerson(self):
        person = self.person_list.currentItem().data(Qt.UserRole)
        if person is not None:
            DB.deletePerson(person)
            self.updatePersonList()


    def faceSelected(self, item):
        person = item.data(Qt.UserRole)
        index = self.name_cb.findText(person.name)
        if index != -1:
            self.name_cb.setCurrentIndex(index)


    def updatePersonList(self):
        self.name_cb.clear()
        self.person_list.clear()
        self.name_cb.addItem('', None)
        self.persons = DB.getAllPerson()
        if self.persons:
            for person in self.persons:
                item = QListWidgetItem(self.person_list)
                icon = QIcon(person.thumbnail_path)
                item.setIcon(icon)
                item.setData(Qt.UserRole, person)
                self.person_list.addItem(item)
                self.name_cb.addItem(person.name)
        self.mainController.updateFaceCB()





