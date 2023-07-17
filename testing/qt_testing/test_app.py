
import pytest
import sys
sys.path.append('.')
from src import MainWindow
from PySide2 import QtCore, QtGui



@pytest.fixture
def app(qtbot):
    test_hello_app = MainWindow()
    qtbot.addWidget(test_hello_app)
    return test_hello_app


def test_window_color(app):
    assert app.palette().color(QtGui.QPalette.Window) == QtGui.QColor(29, 29, 97)

def test_function_initial_value(app):
    assert app.ui.functionTextBox.text() == "x^2"

def test_start_spin_box_value(app):
    assert app.ui.startSpinBox.value() == -10

def test_end_spin_box_value(app):
    assert app.ui.endSpinBox.value() == 10

def test_points_spin_box_value(app):
    assert app.ui.pointSpinBox.value() == 10

def test_label_text(app):
    assert app.ui.label.text() == "Function Plotter"

def test_label_font(app):
    assert app.ui.label.font().family() == "Myanmar Text"
    assert app.ui.label.font().pointSize() == 36

def test_initial_error_text(app):
    assert app.ui.errorText.toPlainText() == ""

errors_test_cases = [
    ("", "Input can't be empty"),
    ("2+","Invalid input"),
    ("2++","Can't have more than one operator in a row"),
    ("((x)","Function must be either constant (y = 5) or variable (y = x))"),
    ("*^","Function must be either constant (y = 5) or variable (y = x))"),
    ("xx","Can't have more than one x in a row"),
    ]


def runTestCases(TestCases):
    for test_case in TestCases:
        yield test_case


@pytest.mark.parametrize("str,result", runTestCases(errors_test_cases))
def test_new_error_text(str, result, app, qtbot):
    app.ui.functionTextBox.setText(str)
    qtbot.mouseClick(app.ui.drawButton, QtCore.Qt.LeftButton)
    assert app.ui.errorText.toPlainText() == result






def test_plot_label(app):
    assert app.plot.axes.get_title() == "Y = $x$"

def test_plot_label_after_click(app, qtbot):
    qtbot.mouseClick(app.ui.drawButton, QtCore.Qt.LeftButton)
    assert app.plot.axes.get_title() == "Y = $x^2$"

def test_plot_label_update(app, qtbot):
    app.ui.functionTextBox.setText("x^3")
    qtbot.mouseClick(app.ui.drawButton, QtCore.Qt.LeftButton)
    assert app.plot.axes.get_title() == "Y = $x^3$"
