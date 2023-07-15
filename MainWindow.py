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
        text = self.ui.functionTextBox.text()
        text2 = text.replace("^", "**")
        x = np.linspace(self.ui.startSpinBox.value(),
                        self.ui.endSpinBox.value(), self.ui.pointSpinBox.value())
        try:

            y = self.validateinput(text2)

            print(y)
            if (y == 0):
                raise Exception("Invalid input")
            elif (y == 1):
                y = eval(text2)
            elif (y == 2):
                y = [float(text2)]*len(x)
        # remove nan elements from x and y
            x, y = zip(*[(x[i], y[i])
                         for i in range(len(x)) if not np.isnan(y[i])])
        # print(x)
        # print(y)

            self.plot.update_figure(x, y, text)
        except Exception as e:
            pass

        # print(self.ui.GraphLayout.count())
    def validateinput(self, str):
        # safe parse string to number
        x = 1
        try:
            if (self.is_float(str)):
                return 2
            str = str.replace("^", "**")
            eval(str)
            return 1
        except Exception as e:

            print(e)
            return 0

    def is_float(self, element: any) -> bool:
        # If you expect None to be passed:
        if element is None:
            print("here1")
            return False
        try:
            print("here2")
            float(element)
            return True
        except ValueError:
            print("here5")
            return False
