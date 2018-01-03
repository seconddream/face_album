import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from controller import FAController

app = QtWidgets.QApplication(sys.argv)
controller = FAController(app)
sys.exit(app.exec_())

