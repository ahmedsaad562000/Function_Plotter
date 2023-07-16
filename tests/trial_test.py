

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def assdsa(x):
    print(os.path.abspath(__file__))
    return x + 1


def test_trial():
    # window = MainWindow()
    # assert window is not None
    # assert window.is_float("1.2") == True
    assert assdsa(3) == 4


test_trial()
