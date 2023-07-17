
import pytest
import sys
sys.path.append('.')
from src import MainWindow

# initialize the Qbot
# this is a fixture that will be used by all tests to access the MainWindow
# it will be passed as an argument to the test functions
@pytest.fixture
def app(qtbot):
    test_hello_app = MainWindow()
    qtbot.addWidget(test_hello_app)
    return test_hello_app