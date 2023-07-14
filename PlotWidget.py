from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PlotWidgetBaseClass(FigureCanvas):
    # Returns a QWidget containing the plot.

    def __init__(self, parent=None, width=10, height=10, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def compute_initial_figure(self):
        pass


class PlotWidget(PlotWidgetBaseClass):

    def __init__(self, *args, **kwargs):
        PlotWidgetBaseClass.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # initial plot (y=x) from -10 to 10
        points = [i for i in range(10, 11)]
        self.axes.plot(points, points, 'r')

    def update_figure(self, x, y):
        # clear previous function
        self.axes.cla()
        # plot the new function using the points given
        self.axes.plot(x, y, 'r')
        self.draw()
