
from PySide2.QtWidgets import QMainWindow
from .MainWindow_UI import MainWindow_UI
from PySide2 import QtGui
from .PlotWidget import PlotWidget
import numpy as np
from .HelperFunctions import isNumber, validateInput, openRepoLink


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)
        self.setIcon("assets\images\icon.jpg")
        self.plot = PlotWidget(self, width=6.3, height=4.4, dpi=100)
        self.ui.GraphLayout.addWidget(self.plot)
        self.ui.drawButton.clicked.connect(self.showPlot)
        self.ui.actionAbout_2.triggered.connect(openRepoLink)

    def setIcon(self, path):
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowIconText("asd")



    def showPlot(self):

        self.ui.errorText.setText("")
        text = self.ui.functionTextBox.text()
        text = text.replace(" ", "")
        try:
            text2 = ""
            start = self.ui.startSpinBox.value()
            end = self.ui.endSpinBox.value()
            points = self.ui.pointSpinBox.value()
            if start >= end:
                raise Exception("Start value must be less than end value")
            if points < 2:
                raise Exception("Points must be greater than 1")

            x = np.linspace(start,
                            end, points)

            y = validateInput(text)
            if y == 2:
                text2 = text.replace("^", "**")
                y = eval(text2)
                if isinstance(y, np.ndarray):
                    pass
                elif isNumber(y):
                    text = str(float(y))
                    y = [float(y)] * len(x)
            elif y == 1:
                y = [float(text)] * len(x)

            self.plot.update_figure(x, y, text)
        except Exception as e:
            self.ui.setErrorText(str(e))
            pass

