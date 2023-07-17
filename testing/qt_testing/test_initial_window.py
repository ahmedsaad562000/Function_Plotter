

from PySide2 import QtGui
from Qbot import app

# test the initial window color
def test_window_color(app):
    assert app.palette().color(QtGui.QPalette.Window) == QtGui.QColor(29, 29, 97)

# test the initial function text box value
def test_function_initial_value(app):
    assert app.ui.functionTextBox.text() == "x^2"

# test the initial start spin box value
def test_start_spin_box_value(app):
    assert app.ui.startSpinBox.value() == -10

# test the initial end spin box value
def test_end_spin_box_value(app):
    assert app.ui.endSpinBox.value() == 10

# test the initial points spin box value
def test_points_spin_box_value(app):
    assert app.ui.pointSpinBox.value() == 10

# test the initial Label text
def test_label_text(app):
    assert app.ui.mainLabel.text() == "Function Plotter"

# test the initial Label font
def test_label_font(app):
    assert app.ui.mainLabel.font().family() == "Myanmar Text"
    assert app.ui.mainLabel.font().pointSize() == 36