from tokenize import Number
from PySide2.QtWidgets import QMainWindow
from MainWindow_UI import MainWindow_UI
from PySide2 import QtGui
from PlotWidget import PlotWidget
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)
        self.setIcon("assets\images\icon.jpg")
        self.plot = PlotWidget(self, width=6.3, height=4.4, dpi=100)
        self.ui.GraphLayout.addWidget(self.plot)
        self.ui.drawButton.clicked.connect(self.showPlot)

    def setIcon(self, path):
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowIconText("asd")

    def showPlot(self):

        self.ui.errorText.setText("")
        text = self.ui.functionTextBox.text()
        try:
            text2 = text.replace("^", "**")
            start = self.ui.startSpinBox.value()
            end = self.ui.endSpinBox.value()
            points = self.ui.pointSpinBox.value()
            if start >= end:
                raise Exception("Start value must be less than end value")
            if points < 2:
                raise Exception("Points must be greater than 1")

            x = np.linspace(start,
                            end, points)

            y = self.validateinput(text2)
            if y == 2:
                y = eval(text2)
            elif y == 1:
                y = np.array([float(text2) for i in x])
            x, y = zip(*[(x[i], y[i])
                         for i in range(len(x)) if not np.isnan(y[i])])

            self.plot.update_figure(x, y, text)
        except Exception as e:
            self.ui.errorText.setText(str(e))
            pass

        # print(self.ui.GraphLayout.count())
    def validateinput(self, str):
        x = 1
        if str == "":
            raise Exception("Input Caan't be empty")

        elif self.is_float(str):
            return 1

        else:
            eval(str)
            return 2

    def is_float(self, element: any) -> bool:
        try:
            float(element)
            return True
        except ValueError:
            return False
