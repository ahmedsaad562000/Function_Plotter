
from src.MainWindow import MainWindow


def triial_test():
    window = MainWindow()
    assert window.ui.functionTextBox.text() == ""


triial_test()
