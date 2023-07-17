
from PySide2.QtWidgets import QMainWindow
from .MainWindow_UI import MainWindow_UI
from PySide2 import QtGui
from .PlotWidget import PlotWidget
import numpy as np
from .HelperFunctions import isNumber, validateInput, openRepoLink


# This is the main window class
# It inherits from QMainWindow
# It's UI is an instance of MainWindow_UI class
# It has a plot widget that is an instance of PlotWidget class
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow_UI()
        self.ui.setupUi(self)
        # set the icon of the window
        self.setIcon("assets\images\icon.jpg")
        # create the plot widget
        self.plot = PlotWidget(self, width=6.3, height=4.4, dpi=100)
        # add the plot widget to the layout
        self.ui.GraphLayout.addWidget(self.plot)
        # connect the draw button to the showPlot function
        self.ui.drawButton.clicked.connect(self.showPlot)
        # connect the about action to the openRepoLink function
        self.ui.actionAbout_2.triggered.connect(openRepoLink)
        

    # This function sets the icon of the window
    def setIcon(self, path):
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowIconText("asd")


    # This function shows the plot
    def showPlot(self):
        # clear the error text
        self.ui.errorText.setText("")
        text = self.ui.functionTextBox.text()
        text = text.replace(" ", "")
        try:
            text2 = ""
            start = self.ui.startSpinBox.value()
            end = self.ui.endSpinBox.value()
            points = self.ui.pointSpinBox.value()
            # validate the input
            # if the start value is greater than the end value 
            # raise an exception
            if start >= end:
                raise Exception("Start value must be less than end value")
            # if the number of points is less than 2
            # raise an exception 
            if points < 2:
                raise Exception("Points must be greater than 1")
            
            # create the x values
            x = np.linspace(start,end, points)
            # validate the input
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

            # update the figure
            self.plot.update_figure(x, y, text)
        except Exception as e:
            # if an exception is raised
            # set the error text to the exception message
            self.ui.setErrorText(str(e))
            pass

