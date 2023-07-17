from .MainWindow import MainWindow
from PySide2.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    myApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(myApp.exec_())
