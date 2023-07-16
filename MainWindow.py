from tokenize import Number
from PySide2.QtWidgets import QMainWindow
from MainWindow_UI import MainWindow_UI
from PySide2 import QtGui
from PlotWidget import PlotWidget
import numpy as np
import re
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)
        self.setIcon("assets\images\icon.jpg")
        self.plot = PlotWidget(self, width=6.3, height=4.4, dpi=100)
        self.ui.GraphLayout.addWidget(self.plot)
        self.ui.drawButton.clicked.connect(self.showPlot)
        self.ui.actionAbout_2.triggered.connect(self.openRepoLink)

    def setIcon(self, path):
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowIconText("asd")

    def openRepoLink(self):
        link = "https://github.com/ahmedsaad562000/Master_Micro_Function_Plotter"
        webbrowser.open(link)

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

            y = self.validateinput(text)
            if y == 2:
                text2 = text.replace("^", "**")
                y = eval(text2)
                print(y)
                if isinstance(y, np.ndarray):
                    pass
                elif self.is_float(y):
                    text = str(float(y))
                    y = [float(y)] * len(x)
            elif y == 1:
                y = [float(text)] * len(x)
            # x, y = zip(*[(x[i], y[i])
            #              for i in range(len(x)) if not np.isnan(y[i])])

            self.plot.update_figure(x, y, text)
        except Exception as e:
            self.ui.setErrorText(str(e))
            pass

        # print(self.ui.GraphLayout.count())
    def validateinput(self, str):
        x = 1

        if str == "":
            raise Exception("Input can't be empty")
        elif re.match(r'^[\d()%/*^xX+]*$', str) is None:
            raise Exception(
                "<p>Character(s) not allowed </p><p> Allowed characters are:<ul> <li> 0-9</li> <li> x or X</li> <li> +</li> <li> -</li> <li> ^</li> <li> ()</li> <li> *</li> <li> /</li> </ul> </p> ")
        elif str.count("(") != str.count(")"):
            raise Exception("Parenthesis must be closed")
        elif re.search(r'[%/*^+]{2,}', str) is not None:
            raise Exception("Can't have more than one operator in a row")
        elif re.search(r'[xX]{2,}', str) is not None:
            raise Exception("Can't have more than one x in a row")
        elif self.is_float(str):
            return 1
        else:
            str2 = str.replace("^", "**")

            eval(str2)
            return 2

    def is_float(self, element: any) -> bool:
        try:
            float(element)
            return True
        except ValueError:
            return False
