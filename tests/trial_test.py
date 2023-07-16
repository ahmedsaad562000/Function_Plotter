from .src.MainWindow import MainWindow


def assdsa(x):
    return x + 1


def test_trial():
    window = MainWindow()
    assert window is not None
    assert window.is_float("1.2") == True
    assert assdsa(3) == 4
