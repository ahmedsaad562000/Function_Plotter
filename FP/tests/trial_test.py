

# from src.MainWindow import MainWindow
# import sys
# from pathlib import Path

# sys.path.insert(
#     1, str(Path(__file__).resolve().parent.parent) + "\src")


def test_trial_2():
    window = MainWindow()
    assert window is not None
    assert 1 == 1
