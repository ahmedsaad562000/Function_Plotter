from PySide2.QtWidgets import QMainWindow
from MainWindow_UI import MainWindow_UI
from PySide2 import QtGui
from PlotWidget import PlotWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)
        self.setIcon("assets\images\icon.jpg")
        self.dc = PlotWidget(self, width=6.3, height=4.4, dpi=100)
        self.ui.GraphLayout.addWidget(self.dc)
        # self.ui.drawButton.clicked.connect(self.showPlot)

    def setIcon(self, path):
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowIconText("asd")
