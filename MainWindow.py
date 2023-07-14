from PySide2.QtWidgets import QApplication, QMainWindow
from MainWindow_UI import MainWindow_UI


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)
