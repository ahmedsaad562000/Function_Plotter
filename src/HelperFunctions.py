import re
import webbrowser
import numpy as np


def validateInput(str):
    x = 1

    if str == "":
        raise Exception("Input can't be empty")
    elif re.match(r'^[\d()%/*^xX+]*$', str) is None:
        raise Exception(
            "<p>Character(s) not allowed </p><p> Allowed characters are:<ul> <li> 0-9</li> <li> x or X</li> <li> +</li> <li> -</li> <li> ^</li> <li> ()</li> <li> *</li> <li> /</li> </ul> </p>")
    elif re.match(r'[0-9xX]', str) is None:
        raise Exception("Function must be either constant (y = 5) or variable (y = x))")
    elif str.count("(") != str.count(")"):
        raise Exception("Parenthesis must be closed")
    elif re.search(r'[%/*^+]{2,}', str) is not None:
        raise Exception("Can't have more than one operator in a row")
    # elif re.search(r'\d+x', str) is not None:
    #     raise Exception("an operator needed between number and x")
    elif re.search(r'[xX]{2,}', str) is not None:
        raise Exception("Can't have more than one x in a row")
    elif isNumber(str):
        return 1
    else:
        try:
            str2 = str.replace("^", "**")
            eval(str2)
            return 2
        except Exception as e:
            raise Exception("Invalid input")

def isNumber(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def openRepoLink():
    link = "https://github.com/ahmedsaad562000/Master_Micro_Function_Plotter"
    webbrowser.open(link)
