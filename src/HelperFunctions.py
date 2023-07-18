import re
import webbrowser

# Used to validate the input
# It returns 1 if the input is a number
# It returns 2 if the input is a function
# It throws an exception with a specific message if the input is invalid
def validateInput(str):
    x = 1
    # if input is empty
    if str == "":
        raise Exception("Input can't be empty")
    # if input contains characters not allowed
    elif re.match(r'^[\d()%/*^xX+]*$', str) is None:
        raise Exception(
            "<p>Character(s) not allowed </p><p> Allowed characters are:<ul> <li> 0-9</li> <li> x or X</li> <li> +</li> <li> -</li> <li> ^</li> <li> ()</li> <li> *</li> <li> /</li> </ul> </p>")
    # if parenthesis are not closed
    elif str.count("(") != str.count(")"):
        raise Exception("Parenthesis must be closed")
    # if input is not a number or a function
    elif re.match(r'[0-9xX]', str) is None:
        raise Exception("Function must be either constant (y = 5) or variable (y = x))")
    # if input contains more than one operator in a row
    elif re.search(r'[%/*^+]{2,}', str) is not None:
        raise Exception("Can't have more than one operator in a row")
    # if input contains more than one x in a row    
    elif re.search(r'[xX]{2,}', str) is not None:
        raise Exception("Can't have more than one x in a row")
    # if input is a number
    elif isNumber(str):
        return 1
    else:
        try:
            str2 = str.replace("^", "**")
            eval(str2)
            return 2
        except Exception as e:
            # if input is invalid for other reasons
            raise Exception("Invalid input")

# This Function is used to check if a string is a number
def isNumber(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

# This Function is used to open the repository link in the browser
def openRepoLink():
    link = "https://github.com/ahmedsaad562000/Master_Micro_Function_Plotter"
    webbrowser.open(link)
