# Freedom to Rest of World Unit Converter

### Video Demo: https://youtu.be/UER980sdYXQ

## Description:
The final project is a unit converter made using python and is playable in the terminal by running the project.py file. A system of units is chosen from table of 3 possible conversions, then you choose which unit you would like to convert from and which unit to convert to before entering the amount to convert. The programme then prints out a statement that states what your stated unit is in the desired unit.

The program consists of a main function and 3 other subprograms/functions namely length_conv, weight_conv, temperature_conv which are called from the main function in the respective order.


### Project Requirements:
&#9745; Your project must be implemented in Python.

&#9745; Your project must have a main function and at least three other functions, each of which must be accompanied by tests that can be executed with pytest.

&#9745; Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.

&#9745; Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).

&#9745; Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).

&#9745; You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.

&#9745; Implementing your project should entail more time and effort than is required by each of the course’s problem sets.

&#9745; Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.

---

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the package [`tabulate`](https://pypi.org/project/tabulate/)
```
$ pip install tabulate
```
Use [pip](https://pip.pypa.io/en/stable/) to install the package [`pytest`](https://pypi.org/project/pytest/)
```
$ pip install pytest
```

---

## Usage
Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```


