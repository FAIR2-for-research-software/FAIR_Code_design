---
title: "Code structure"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions

- How to structure a code in a scalable and reusable way?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Learn to use functions and classes
- Understand how to organise your code in modules and packages

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

When you're writing code, making it consistent and well-structured is just as
essential as ensuring it produces the correct result. You should think about how
you structure your code as you write it, as this will make it easier to read and
maintain in the future both by yourself and others.

It's important to follow the design principles of the programming language you are using.
Python is known as an **object-oriented** programming language, which means Python code is
structured around creating, using, and interacting with code **objects**. There are many
different types of objects in Python, such as basic integers or text strings, lists or
dictionaries which contain multiple objects, and functions that operate on objects.
It's also encouraged to create your own classes of objects, to make your code more
modular and reusable.

When your code grows in size and complexity, it's a good idea to split it into multiple
files, known as **modules**, and organise these modules into **packages**. This makes
your code easier to manage and maintain, and allows you to reuse code across multiple
projects.

## Functions

**Functions** are a way to group code together that performs a specific task. There
are many built-in functions in Python, such as `print()` to output values or `len()`
to get the length of a list. But you can also create your own functions, to perform
tasks that you need to do multiple times.

Functions are defined using the `def` keyword, followed by the function name and a set
of parentheses containing any **parameters** the function takes. The function body is
then indented and contains the code that the function will execute. The `return` keyword
is used to specify what the function should output.

Below is a very basic function that simply takes two parameters and returns their sum.
Once you have defined a function, you can call it by using its name and passing in the
required parameters as **arguments** to the function. In this case the parameters `a` and
`b` are set to `2` and `6` respectively, and the result of the function is stored in the
`result` variable:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```
```output
8
```

:::::::::::: callout

#### Whitespace

If you're used to other programming languages like C or R, you might be surprised to see that
Python does not use curly braces `{}` to define blocks like functions.
Instead, Python uses **indentation** to define blocks of code, either with spaces or tabs (known
as **whitespace**).

It's important to be consistent with your indentation, as mixing different numbers of spaces or
tabs can cause errors. Most code editors will automatically indent and convert tabs to spaces when
writing Python.

::::::::::::


This is obviously a very simple example, but functions can be much more complex and
can take multiple parameters, return multiple values, or raise errors if something goes wrong.

Any function acts as a reusable block of code that can be called multiple times within
your program. Building your code out of small, modular functions makes it easier to read
and maintain, by not having to repeat the same code multiple times you save space and only need to
edit the code in one place when making changes. It's also easier and more reliable to test the
output of individual functions to make sure they work correctly, rather than having to run the
entire program.
There will be a future session on [Testing and Continuous Integration](https://rse.shef.ac.uk/training/fair4rs/#testing-and-continuous-integration) which will cover this in more detail.


#### Scope

When you define a variable inside a function, it is only accessible within that function.
This is known as the **scope** of the variable. If you try to access a variable that is
defined inside a function from outside the function, you will get an error:

```python
def my_function():
    x = 10
    return x

result = my_function()
print(x)
```
```output
NameError: name 'x' is not defined
```

Anything defined outside of a function is said to be in the **global scope**, and can be
accessed from anywhere in the program (including within functions). However, it's generally
considered good practice to avoid using global variables, as they can make your code harder
to understand and debug.

:::::::::::: challenge

#### Challenge 1

What will be the output of this code?

```python
x = 5
y = 10

def my_function(z):
    x = 20
    return x + y + z
result = my_function(3)

print('x:', x)
print('y:', y)
print('Result:', result)
print('z:', z)
```
::::::::::::

:::::::::::: solution

```output
x: 5
y: 10
Result: 33
NameError: name 'z' is not defined
```

The `x` variable inside the function is a different variable to the `x` variable outside,
so changing it inside the function does not affect the global `x` variable.

The `y` variable is accessible inside the function because it is defined in the global scope.

The `result` variable is the sum of the function's `x` variable, the global `y` variable and the
argument `z`.

The `z` variable is not defined outside the function, so trying to print it in the main body of the script will raise an error.
::::::::::::


## Classes

**Classes** are a way to group functions and data together into a single object. Classes
act as a blueprint for creating objects, which are then called **instances** of the class.

Similar to functions, classes are defined using the `class` keyword, followed by the class
name. The class body is then indented and contains any **properties** or **methods** (i.e.
functions) that the class has.

Below is a very simple class for a `Rectangle` object, which has properties for its width and
height, as well as a method to calculate its area:

```python
class Rectangle:
   width = 5
   height = 3

    def get_area(self):
        return self.width * self.height
```

:::::::::::: callout

#### The `self`  parameter

Methods in a class always define `self` as the first parameter, which is used as a reference to the
instance of the class that the method is being called on.
In this case the `get_area` method uses the width and height properties of the `Rectangle` instance.
You can actually call this parameter anything you like, but `self` is the convention in Python.

::::::::::::

You can then create an instance of this class by calling the class name as if it were a
function, and you can access its properties and methods using the `.` operator:
```python
my_rectangle = Rectangle()
print('This rectangle has a width of', my_rectangle.width, 'and a height of', my_rectangle.height)
print('Its area is', my_rectangle.get_area())
```
```output
This rectangle has a width of 5 and a height of 3
Its area is 15
```

In this case the class is not very reusable, as the width and height are fixed. You can
pass arguments when creating an instance of the class by defining a special `__init__()` method.
The `__init__()` method at is called whenever a new instance of the class is created,
and it can take values to set the initial state of the object. In the example below,
the `Rectangle` class takes `width` and `height` parameters and stores them as properties of the
`self` object (i.e. the instance of the class that is being created):

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

my_rectangle = Rectangle(10, 20)
print('This rectangle has a width of', my_rectangle.width, 'and a height of', my_rectangle.height)
print('Its area is', my_rectangle.get_area())
```
```output
This rectangle has a width of 10 and a height of 20
Its area is 200
```
:::::::::::: callout

#### "Dunder" methods

In Python, methods that start and end with double underscores are called "dunder" (short
for "double underscore") or "magic" methods. These methods are special and have specific
built-in meanings, such as `__init__()` being called when an instance of a class is initialised.
We'll see more examples of "dunders" later in this section.

::::::::::::

Classes are a powerful way to structure your code, as they allow you to group related
functions and data together in a way that is reusable and easy to understand.


:::::::::::: challenge

#### Challenge 2

In the code below, we have multiple lists representing items in a grocery store.
Each fruit has a name, price, and the number in stock.

```python
fruits = ['apple', 'banana', 'orange']
fruit_prices = [1.00, 0.50, 0.75]
fruit_count = [10, 20, 15]
```

Create a class called `Stock` that has properties called `name`, `price`, `count`, and two
methods: `display()` that prints out the name and unit price of the fruit, and `get_total_value()` that returns the total value of the stock.

Then create a new list of `Stock` objects, and call the `display()` method on each object.

::::::::::::

:::::::::::: solution

```python
class Stock:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def display(self):
        print(f'Each {self.name} costs £{self.price}')

    def get_total_value(self):
        return self.price * self.count


fruits = [
    Stock('apple', 1.00, 10),
    Stock('banana', 0.50, 20),
    Stock('orange', 0.75, 15)
]
for fruit in fruits:
    fruit.display()
```

```output
Each apple costs £1.0
Each banana costs £0.5
Each orange costs £0.75
```

::::::::::::


:::::::::::: challenge

#### Challenge 3

Now, create a `Shop` class that has a property called `stock` that is a list of `Stock` objects.
The `Shop` class should have a method called `display_stock()` that calls the `display()` method
on each item in the `stock` list, and a method called `get_total_stock_value()` that returns the
total value of all items in the `stock` list.

Then create a new `Shop` object with the `fruits` list as the input, and call the
`display_stock()` and `get_total_stock_value()` methods.

::::::::::::

:::::::::::: solution

```python
class Shop:
    def __init__(self, stock):
        self.stock = stock

    def display_stock(self):
        for item in self.stock:
            item.display()

    def get_total_stock_value(self):
        total = 0
        for item in self.stock:
            total += item.get_total_value()
        return total

shop = Shop(fruits)
shop.display_stock()
print('Total stock value:', shop.get_total_stock_value())
```

```output
Each apple costs £1.0
Each banana costs £0.5
Each orange costs £0.75
Total stock value: 31.25
```

::::::::::::

:::::::::::: callout

#### Naming conventions

Note that in each of these examples, the variables, properties and class names are written as nouns
(e.g. `result`, `Rectangle`, `width` or `Shop`), while the functions and class methods are
lowercase verbs or short phrases (e.g. `add()`, `get_area()` or `display_stock()`).
This is a common convention in Python, and following it can help you write more readable code and
understand the difference between objects and functions more easily.

We will see more examples of coding conventions like this in later sections.

::::::::::::


## Scripts and Modules

A Python **script** is a file containing Python code that can be executed by the Python
interpreter. You can run a script by calling the Python interpreter with the script file
as an argument, like this:

```bash
python my_script.py
```

When you're writing a large program, it's a good idea to split your code into multiple
files to make it easier to manage, and to make it easier to reuse code in other projects.
Each file containing Python code is called a **module**, and you can import modules into
scripts and other modules to use the functions and classes they contain.

For example, you could create a file called `calculator.py` that contains the `add()` function
we defined earlier, as well as other functions for subtraction, multiplication, and division.

```python
"""calculator.py"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

Now, in another script or module, you can import the `calculator` module and use its functions by using the `import` keyword:

```python
"""script.py"""
import calculator

result = calculator.add(5, 3)
print(result)
```
```output
8
```

You can also import specific functions or classes from a module, rather than importing the
whole module. This can be useful if you only need one or two functions, as it
saves some time and can make your code more readable:

```python
from calculator import add

result = add(5, 3)
```

Python comes with a lot of built-in modules that you can import and use in your code, collectively  known as the **Standard Library**. These work in the same way, for instance if you wanted
trigonometric functions you can do `from math import sin, cos, tan` and then use those functions
in your code.

#### Running a module as a script

In some cases, you might want a mixture of code that executes when the module is run as a script
as well as functions and classes that can be imported into other modules. Too keep the two separate,
you can use another special "**dunder**" method called `__name__`. This is a built-in variable that
is set to `'__main__'` when the module is run as a script, and is set to the module name when the
module is imported into another module.

As such, if you include a check for `if __name__ == '__main__':` in your module, you can define
code that only runs when the module is run as a script:

```python
"""calculator.py"""
def add(a, b):
    return a + b

if __name__ == '__main__':
    result = add(5, 3)
    print('Test result:', result)
```

```bash
$ python calculator.py
Test result: 8
```

If you didn't include the `if __name__ == '__main__':` check, then every time you tried to
import the `add()` function from the `calculator` module, the test code would run as well and print
out the result.


## Packages

Once you have a collection of modules that you want to reuse across multiple projects, you can
organise them into a **package**. A package is a directory containing multiple modules, along with
a special `__init__.py` file that tells Python that the directory is a package (this is yet another
example of a "dunder" being used as a special marker in Python, in this case being used to signify
that a directory is importable).

For example, you could create a package called `my_package` that contains the `calculator` module
we defined earlier, as well as a new module called `geometry` that contains functions for working
with shapes. When organising these modules into a package, the directory structure would look like this:

```
my_package/
    __init__.py
    calculator.py
    geometry.py
```

The `__init__.py` file can be empty, but it can also contain code that runs when the package is imported.

You can then import the modules from the package in the same way as before, but you need to include
the package name either as a prefix or by using the `from` keyword:

```python
import my_package.calculator
my_package.calculator.add(5, 3)

OR

from my_package import calculator
calculator.add(5, 3)

OR

from my_package.calculator import add
add(5, 3)
```

If your package grows large enough, you can also create sub-packages within your package by creating
subdirectories with their own `__init__.py` files. This allows you to organise your code into a
hierarchical structure that makes it easier to manage and understand.

:::::::::::: challenge

#### Challenge 4

A researcher has all of their code for a project in a single Python file, and they want to split it
into multiple modules within a package. Here is a list of the functions and classes they have
defined in their script:

- `load_data()`: a function that reads data from a file
- `clean_data()`: a function that removes any missing values from the data
- `plot_data()`: a function that plots the data
- `Data`: a class that holds the data, returned by `load_data()`
- `Model`: a class that represents a machine learning model created from the data
- `test_data()`: a function that tests the data class is working correctly
- `test_model()`: a function that tests the model class is working correctly
- `run_experiment()`: a function that runs the entire experiment, taking a data file as an input

There is also a test file called `test_data.csv` that contains some example data, and is
used by the `test_data()` and `test_model()` functions.

How would you organise this code into a package?

::::::::::::

:::::::::::: solution

Here is an example of how you could organise the code into a package:

```
research_project/
    __init__.py
    data/
        __init__.py
        data.py
    model/
        __init__.py
        model.py
    plot/
        __init__.py
        plot.py
    scripts/
        __init__.py
        run_experiment.py
    tests/
        __init__.py
        test_data.csv
        test_data.py
        test_model.py
```

- The `data` module would contain the `load_data()` and `clean_data()` functions and the `Data` class.
- The `model` module would contain the `Model` class definition.
- The `plot` module would contain the `plot_data()` function.
- The `scripts` module would contain the `run_experiment()` function in a standalone script.
- The `tests` module would contain the `test_data()` and `test_model()` functions, as well as the `test_data.csv` file.

For instance, if you wanted to load and plot the data in a different script, you could import the `data` and `plot` modules like this:

```python
from research_project.data import load_data
from research_project.plot import plot_data

data = load_data('data.csv')
plot_data(cleaned_data)
```

Although it seems like a lot of files for a small amount of code, this structure makes it easier to
manage and maintain the project over time, and will make it easier to reuse the code in other projects in the future.

::::::::::::

Once you have your package organised, you can share it with others by using a code hosting platform
like GitHub, or uploading it to the **Python Package Index** (PyPI, https://pypi.org/).
If you do this there are some additional files you should include to make your package more
user-friendly, such as a `README` file that explains what the package does and how to use it,
and a `LICENSE` file that specifies the terms under which the code can be used. There is another
session on [Packaging](https://rse.shef.ac.uk/training/fair4rs/#packaging) which will go
into more detail on how to create and share Python packages.
