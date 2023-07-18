
<h1><span style="color:blue">Master_Micro_Function_Plotter</span></h1>
<img src="assets\images\icon.jpg" alt= “Icon_Image” width="100" height="100">


<h2><i>a Python GUI program that plots an arbitrary user-entered function</i><h2>
</br>

## Description
Function Plotter is a Python GUI program that plots an arbitrary user-entered function. The program is written in Python and uses the PySide2 library for the GUI. The program is designed to be user-friendly and easy to use. The user can enter a function in the text box with start , end and number of points then the program will plot it.

## Screenshots
- ### Working Examples
    - Function of x
        <img src="screenshots/normal_function.png" alt= “Example1_Image” >
    - Constant
        <img src="screenshots/Constant.png" alt= “Example2_Image” >
- ### Errors
  - Empty Text Box
  - 
    <img src="screenshots/Empty_input_error.png" alt= “Error1_Image” height=400 width=300> 
  - Allowed Characters
  - 
    <img src="screenshots/Allowed_Characters_Error.png" alt= “Error2_Image” height=400 width=300>
    <img src="screenshots/Allowed_Characters_Error2.png" alt= “Error3_Image” height=200 width=300>   
  - Paranthesis Error
  - 
    <img src="screenshots/paranthesis_error.png" alt= “Error4_Image” height=400 width=300>
  
  - Wrong Function
  - 
    <img src="screenshots/function_structure.png" alt= “Error5_Image” height=400 width=300>

- ### Testing (31 total tests)
    <img src="screenshots/QT-Tests.png" alt= “PyTest-Qt_Image” height=400 width=300>
    <img src="screenshots/QT-Tests-2.png" alt= “PyTest-Qt_Image” height=400 width=300>

## Technologies Used
- Python
- PySide2
- Matplotlib
- Numpy

## Run in command prompt
<ol>
<li>Clone the repository</li>

```bash
git clone https://github.com/ahmedsaad562000/Master_Micro_Function_Plotter.git
```

<li>Create Virtual Environment</li>

```bash
python -m venv path/to/new/virtual/environment
```
<li>Activate Your virtual Environment</li>

- cmd
  
```bash
path/to/new/virtual/environment/Scripts/activate
```
- powershell

```bash
. path/to/new/virtual/environment/Scripts/Activate.ps1
```

<li>Install Requirements</li>

```bash
pip install -r requirements.txt
```

<li>Run the program</li>

```bash
python -m src
```

</ol>