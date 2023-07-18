from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PlotWidgetBaseClass(FigureCanvas):
    # Returns a QWidget containing the plot.
    def __init__(self, parent=None, width=10, height=10, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, frameon=False)

        self.axes = fig.add_subplot(111)
        # setting the x and y labels
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')

        # plot the initial figure
        self.compute_initial_figure()
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def compute_initial_figure(self):
        pass


class PlotWidget(PlotWidgetBaseClass):

    def __init__(self, *args, **kwargs):
        PlotWidgetBaseClass.__init__(self, *args, **kwargs)
        self.axes.grid(color='black', linestyle=':', linewidth=1)

    def compute_initial_figure(self):
        # initial plot (y=x) from -10 to 10 with step 2
        points = [i for i in range(-10, 11,2)]
        # setting the title of the plot
        self.axes.set_title('Y = $x$', {'fontsize': 18,
                                              'color': 'b'})
        self.axes.plot(points, points, 'r')

    def update_figure(self, x, y, functionStr):
        # clear previous function
        functionStr = functionStr.replace("*", "")
        self.axes.cla()
        # set the grid lines of the plot to black dotted lines with width 1
        self.axes.grid(color='black', linestyle=':', linewidth=1)
        self.axes.set_title(f'Y = ${functionStr}$', {'fontsize': 18,
                                                     'color': 'b'})
        # setting the x and y labels
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')

        # plot the new function using the points given
        self.axes.plot(x, y, 'r')
        self.draw()
