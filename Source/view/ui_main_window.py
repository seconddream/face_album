# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolbox_frame = QtWidgets.QFrame(self.centralwidget)
        self.toolbox_frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.toolbox_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolbox_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolbox_frame.setObjectName("toolbox_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.toolbox_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.import_btn = QtWidgets.QPushButton(self.toolbox_frame)
        self.import_btn.setObjectName("import_btn")
        self.verticalLayout.addWidget(self.import_btn)
        self.photo_btn = QtWidgets.QPushButton(self.toolbox_frame)
        self.photo_btn.setObjectName("photo_btn")
        self.verticalLayout.addWidget(self.photo_btn)
        self.face_btn = QtWidgets.QPushButton(self.toolbox_frame)
        self.face_btn.setObjectName("face_btn")
        self.verticalLayout.addWidget(self.face_btn)
        self.horizontalLayout.addWidget(self.toolbox_frame)
        self.explore_frame = QtWidgets.QFrame(self.centralwidget)
        self.explore_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.explore_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.explore_frame.setObjectName("explore_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.explore_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filter_frame = QtWidgets.QFrame(self.explore_frame)
        self.filter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filter_frame.setObjectName("filter_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.filter_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.filter_frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.face_filter_cb = QtWidgets.QComboBox(self.filter_frame)
        self.face_filter_cb.setObjectName("face_filter_cb")
        self.horizontalLayout_2.addWidget(self.face_filter_cb)
        self.label_2 = QtWidgets.QLabel(self.filter_frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.emotion_filter_cb = QtWidgets.QComboBox(self.filter_frame)
        self.emotion_filter_cb.setObjectName("emotion_filter_cb")
        self.horizontalLayout_2.addWidget(self.emotion_filter_cb)
        self.filter_btn = QtWidgets.QPushButton(self.filter_frame)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout_2.addWidget(self.filter_btn)
        self.verticalLayout_2.addWidget(self.filter_frame)
        self.thumbnails_list = QtWidgets.QListWidget(self.explore_frame)
        self.thumbnails_list.setIconSize(QtCore.QSize(100, 100))
        self.thumbnails_list.setGridSize(QtCore.QSize(150, 150))
        self.thumbnails_list.setViewMode(QtWidgets.QListView.IconMode)
        self.thumbnails_list.setBatchSize(100)
        self.thumbnails_list.setSelectionRectVisible(False)
        self.thumbnails_list.setObjectName("thumbnails_list")
        self.verticalLayout_2.addWidget(self.thumbnails_list)
        self.horizontalLayout.addWidget(self.explore_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_btn.setText(_translate("MainWindow", "Import Photos"))
        self.photo_btn.setText(_translate("MainWindow", "Photos"))
        self.face_btn.setText(_translate("MainWindow", "Faces"))
        self.label.setText(_translate("MainWindow", "Face:"))
        self.label_2.setText(_translate("MainWindow", "Emotion:"))
        self.filter_btn.setText(_translate("MainWindow", "Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

