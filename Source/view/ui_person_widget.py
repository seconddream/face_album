# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_person_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PersonWidget(object):
    def setupUi(self, PersonWidget):
        PersonWidget.setObjectName("PersonWidget")
        PersonWidget.resize(832, 551)
        self.verticalLayout = QtWidgets.QVBoxLayout(PersonWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.person_list = QtWidgets.QListWidget(PersonWidget)
        self.person_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.person_list.setIconSize(QtCore.QSize(50, 50))
        self.person_list.setViewMode(QtWidgets.QListView.IconMode)
        self.person_list.setObjectName("person_list")
        self.verticalLayout.addWidget(self.person_list)
        self.frame = QtWidgets.QFrame(PersonWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_cb = QtWidgets.QComboBox(self.frame)
        self.name_cb.setMaximumSize(QtCore.QSize(200, 16777215))
        self.name_cb.setEditable(True)
        self.name_cb.setObjectName("name_cb")
        self.horizontalLayout.addWidget(self.name_cb)
        self.update_btn = QtWidgets.QPushButton(self.frame)
        self.update_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.delete_btn = QtWidgets.QPushButton(self.frame)
        self.delete_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(PersonWidget)
        QtCore.QMetaObject.connectSlotsByName(PersonWidget)

    def retranslateUi(self, PersonWidget):
        _translate = QtCore.QCoreApplication.translate
        PersonWidget.setWindowTitle(_translate("PersonWidget", "Faces"))
        self.label.setText(_translate("PersonWidget", "Name:"))
        self.update_btn.setText(_translate("PersonWidget", "Update"))
        self.delete_btn.setText(_translate("PersonWidget", "Delete"))

