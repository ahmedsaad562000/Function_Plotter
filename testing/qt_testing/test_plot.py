from PySide2 import QtCore
from Qbot import app

# test the initial plot label
def test_plot_label(app):
    assert app.plot.axes.get_title() == "Y = $x$"
# test the plot label after clicking the draw button
def test_plot_label_after_click(app, qtbot):
    qtbot.mouseClick(app.ui.drawButton, QtCore.Qt.LeftButton)
    assert app.plot.axes.get_title() == "Y = $x^2$"

# test the plot label after clicking the draw button
# and changing the function
def test_plot_label_update(app, qtbot):
    app.ui.functionTextBox.setText("x^3")
    qtbot.mouseClick(app.ui.drawButton, QtCore.Qt.LeftButton)
    assert app.plot.axes.get_title() == "Y = $x^3$"