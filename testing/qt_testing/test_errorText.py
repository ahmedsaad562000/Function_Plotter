import pytest
from Qbot import app
from PySide2 import QtCore

# test the initial error text
def test_initial_error_text(app):

    assert app.ui.errorText.toPlainText() == ""

errors_test_cases = [
    ("", "Input can't be empty"),
    ("2+","Invalid input"),
    ("2++","Can't have more than one operator in a row"),
    ("(()","Parenthesis must be closed"),
    ("*^","Function must be either constant (y = 5) or variable (y = x))"),
    ("xx","Can't have more than one x in a row"),
    ]


def runTestCases(TestCases):
    for test_case in TestCases:
        yield test_case

# test the error text after inputting a function
# and clicking the draw button
@pytest.mark.parametrize("str,result", runTestCases(errors_test_cases))
def test_new_error_text(str, result, app, qtbot):
    app.ui.functionTextBox.setText(str)
    qtbot.mouseClick(app.ui.drawButton, QtCore.Qt.LeftButton)
    assert app.ui.errorText.toPlainText() == result

