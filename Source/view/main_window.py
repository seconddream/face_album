from PyQt5.QtWidgets import QMainWindow
from view.ui_main_window import Ui_MainWindow
import model.database_manager as DB

class FAMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, QCloseEvent):
        DB.closeConnection()

