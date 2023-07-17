import pytest
import sys
sys.path.append('.')
from src import isNumber, validateInput

# TestCases
isNumber_test_cases = [("1.2", True), ("1", True),
                       ("1.2.3", False), ("1.2a", False), ("a", False)]
validateInput_test_cases = [
    ("2", 1), ("x^2", 2),
    ("", "Input can't be empty"),
    ("pg","<p>Character(s) not allowed </p><p> Allowed characters are:<ul> <li> 0-9</li> <li> x or X</li> <li> +</li> <li> -</li> <li> ^</li> <li> ()</li> <li> *</li> <li> /</li> </ul> </p>"),
    ("2+","Invalid input"),
    ("2++","Can't have more than one operator in a row"),
    ("((x)","Function must be either constant (y = 5) or variable (y = x))"),
    ("*^","Function must be either constant (y = 5) or variable (y = x))"),
    ("xx","Can't have more than one x in a row"),
    ]


def runTestCases(TestCases):
    for test_case in TestCases:
        yield test_case


@pytest.mark.parametrize("str,result", runTestCases(isNumber_test_cases))
def test_isNumber(str, result):
    assert isNumber(str) == result


@pytest.mark.parametrize("inp,result", runTestCases(validateInput_test_cases))
def test_validateInput(inp, result):
    try:
        x = validateInput(inp)
        assert  x == result
    except Exception as e:
        assert str(e) == result
