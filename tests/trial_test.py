

import sys
from pathlib import Path

sys.path.insert(
    1, str(Path(__file__).resolve().parent.parent) + "\src")

from src.MainWindow import MainWindow

def assdsa(x):
    print(str(Path(__file__).resolve().parent.parent) + "\src\MainWindow.py")
    return x + 1


def test_trial():
    window = MainWindow()
    assert window is not None
    assert window.is_float("1.2") == True
    assert assdsa(3) == 4
