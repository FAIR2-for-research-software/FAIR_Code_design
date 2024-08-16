---
title: "The Zen of Python"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- How to write clean?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand why it is important to write good code
- 
- Write PEP8 compliant code

::::::::::::::::::::::::::::::::::::::::::::::::

## Python Enhancement Proposals and the Zen of Python

The Python Enhancement Proposals are documents that provide information to the Python community, or describing a new feature for Python or its processes or environment. Some of them are also focusing on design and style: 

 - The main one is [PEP8](https://peps.python.org/pep-0008/). It lays out rules to write clean code in Python.  
 - Docstrings convention are given in [PEP257](https://peps.python.org/pep-0257/).
 - The Zen of Python in [PEP20](https://peps.python.org/pep-0020/) gives principle for Python's design. It is accesible in any python distribution with:

```
In [1]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


## Readability counts 

As Guido van Rossum (Python creator and Benevolent dictator for life) once said ''Code is read much more often than it is written''

While coding you may spend of a few hours (days) on a piece of code and when you will be done with it you will not write it again. Nevertheless there is a very high chance that you will read it again. If the piece of code is part of an on-going project you will have to remember what that code does and why you actually wrote it. Hence, readability counts! Remembering what a code does after a few weeks/months is not easy. **If you follow the standard guidelines it will greatly help you (and save you a lot of time!)**. 

In addition, if multiple people are looking at the code and developing with you, writing readable code is paramount. If people have to decipher your coding style before actually trying to understand what you are coding that will become very difficult for everybody. PEP8 provides a standardisation of the python coding style. 


## Explicit is better than implicit.

Writing clear code is not complicated. It starts by giving meaningful name to variables, function and classes. Avoid single letter names like `x` or `y`.
For example:

``` python
# This is bad:

x = 5
y = 10
z = 2*x + 2*y

# This is much better:

width = 5
height = 10
diameter = 2*height + 2*width
```

Just by using descriptive names we can understand what the code is trying to do.

In addition, everything that you write (variables, constants, function, classes...) comes with a way to name it. The main conventions are:

* **Variables, function and methods use the `Snake_case` convention.** It means that they should use lowercase letters and words should be separated by underscore:

``` python
# This is bad
def ComputeDiameter(width, height):
    return 2*width + 2*height

# This is good
def compute_diameter(width, height):
    return 2*width + 2*height
```

* **Class names follow the PascalCase convention (also known as CamelCase).** In that convention, each word starts with a capital letter and there are **NO** underscores between words.

``` python
# This is bad
class example_class:

# This is good
class ExampleClass:
```

* **Constant name follow the UPPER_SNAKE_CASE convention.** Constants, or variables that are intended to remain unchanged, should be written in all uppercase letters, with words separated by underscores.


``` python
# This is bad:
speedoflight = 3e8
plankconstant = 6.62e-34

# This is good
SPEED_OF_LIGHT = 3e8
PLANK_CONSTANT = 6.62e-34 
```

## Beautiful is better than ugly 


In the context of Python, *beautiful* means that the code is clean, readable and well structured. *Beautiful* code is easy to understand, not only for you but also others people who might have to maintain the code in the future. It uses meaningful names and clear logic and structure.

::::::::::::::::::::::::::::::::::::: challenge

What is this code doing?

``` python
print(sum(x**2 for x in range(2, 100) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))))
```

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

This one-liner finds all prime numbers less than 100, squares them, and returns the sum of these squares.

:::::::::::::::::::::::::::::::::

'Beautiful is better than ugly' means that developers should aim for simplicity and elegant solution. It makes a code very difficult to maintain when the author tries to cram as much as much functionality as possible in a single line or function. Always tries to break down into clear single component.

Beautiful code is aesthetically pleasing because it follows good design principles (see next chapter). It is modular, reusable, and adheres to the DRY (Don't Repeat Yourself) principle. It avoids unnecessary complexity and focuses on clarity.


::::::::::::::::::::::::::::::::::::: challenge

Rewrite the one-liner given above to make it more readable and understandable.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

``` python
def is_prime(n):
    """Check if a number is prime using a basic method."""
    
    # If n is less than or equal to 1, it is not a prime number
    if n <= 1:
        return False
    
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    
    # Exclude multiples of 2 and 3
    # If n is divisible by 2 or 3, it is not a prime number
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check potential factors from 5 up to the square root of n
    # The step size is 6 because after checking 2 and 3, we only need to check numbers of the form 6k ± 1
    # This is because all prime numbers are of the form 6k ± 1, except for 2 and 3
    i = 5
    while i * i <= n:
        # If n is divisible by i, it is not a prime number
        if n % i == 0:
            return False
        # If n is divisible by i + 2, it is not a prime number
        if n % (i + 2) == 0:
            return False
        # Move to the next potential factor
        i += 6
    
    # If no divisors were found, n is a prime number
    return True


def sum_of_squares_of_primes(upper_limit):
    """
    Find all prime numbers less than 'upper_limit', square them, and return their sum.
    """
    sum_squares = 0
    
    # Iterate through numbers to find primes and calculate their squares
    for number in range(2, upper_limit):
        if is_prime(number):
            sum_squares += number ** 2

    return sum_squares

# Define the upper limit
upper_limit = 100

# Calculate and print the result
result = sum_of_squares_of_primes(upper_limit)
print(result)

```

:::::::::::::::::::::::::::::::::


## Sparse is better than dense.


When you write your code it is important to make it readable. Avoiding cluttered code by making is sparse and spaced out makes it easier to read and increase clarity and readability. Use whitespaces, correct indentation and separation will make your code quicker to understand. Moreover, when code is spread out with proper comments and breaks it is easier to modify or debug. Let's see an example:

::::::::::::::::::::::::::::::::::::: challenge

What is this code doing?

``` python
def   example_function(param1,param2):print(param1+param2*2, end=' ')
print("The result is:",  param1,param2) 
def   another_function(x,y):return x+y
class  MyClass: def __init__(self,param):self.param=param
def  method(self):if self.param >10:print("Value is greater than 10")
else:print("Value is 10 or less") 
my_list=[1,2,3,4,5]
dictionary={'key1':'value1','key2':'value2'}
result=another_function(5,10) 
print(result)
```

::::::::::::::::::::::::::::::::::::::::::::::::


So what are the rules?

* Indentation: The convention is to use 4 spaces. Tabs are not recommended as they can lead to inconsistencies:

``` python
def example_function():
    if True:
        print("Indented correctly")
```

* **Whitespaces around operators**: A single space on both sides of binary operators should be included (`+, -, *, /, =, ==, !=, <, >, <=, >=, etc`).

``` python
#This is bad
a=2
b=3
c=4
result=a+b+c


#This is good
a = 2
b = 3
c = 4
result = a + b * c
``` 

* **Comma and colon spacing**: you shoud include a single space after a comma and you should include a space after the colon in dictionary:

```python

#This is bad
dictionary={'key1':'value1','key2':'value2'}

#This is good
dictionary = {'key1': 'value1', 'key2': 'value2'}

```  

* **Blank lines**: Use two blank lines before a top-level function or class definition and use a single blank line between method definitions inside a class.


``` python
# This is bad
class MyClass:
    def method_one(self):
        pass
    def method_two(self):
        pass

# This is good

class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

```




## If the implementation is hard to explain, it’s a bad idea...If the implementation is easy to explain, it may be a good idea.

If you follow this FAIR training program you might be interested to share your code with the wider research community. If that's the case people might want to have a look at your code. This aphorism tells you that how you implemented your code matters! Code should always be easy to understand. If you are unable to explain what your code is doing then you should not leave it in your software. Conversely, if you are able to explain in an easy what your piece of code is doing, this is probably a good implementation. For example

::::::::::::::::::::::::::::::::::::: challenge

What is this code doing?

``` python

def check_number(num):
    if num % 2 == 0:
        if num % 5 == 0:
            return True
        else:
            return False
    else:
        return False
```

How could you make it easier to understand?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

The function checks if a number is both even and a multiple of 5. A better way of doing it could be:

```
def check_number(num):
    return num % 2 == 0 and num % 5 == 0
```

:::::::::::::::::::::::::::::::::


## PyLint


PyLint is a tool that analyzes Python code to find programming errors, enforce a coding standard, and look for improvements. It provides a score based on the number of issues detected, helping you writing clean and readable code.
 

### Key Features of PyLint

- Error Detection: Identifies syntax errors, undefined variables, and other potential bugs.
Detects issues such as using undefined variables, unnecessary imports, and more.

- Coding Standard Enforcement: Checks the code against PEP 8. Flags violations such as incorrect indentation, naming conventions, and line length.

- Code Quality Metrics: Provides a detailed report with metrics like code complexity, number of lines, and number of classes. Offers a score that reflects the overall quality of the code.

- Refactoring Suggestions: Suggests improvements to make the code cleaner and more efficient.
Highlights duplicated code, unused variables, and functions that can be simplified.


### Running pylint

To analyse a python file you can simply run:

``` bash
pylint your_python_file.py
```

When you run PyLint on a Python file, it provides an output with the following components:

- Messages: Each detected issue is reported with a message ID, type, line number, and a brief description.
- Statistics: Provides a summary of the issues found, such as the number of errors, warnings, and refactor suggestions.
- Score: An overall score out of 10, reflecting the code quality based on the issues detected.

::::::::::::::::::::::::::::::::::::: challenge


Let's have a look at an example: Consider that file [here](https://github.com/Romain-Thomas-Shef/FAIR_Code_design/blob/main/write_clean_code/example_bad_PEP8.py) and run PyLint on it. Try to clean up the code according to the error messages you see.
 
::::::::::::::::::::::::::::::::::::::::::::::::

### Configuration: 

PyLint can be configured to match your specific project requirements. You can create a configuration file (.pylintrc) to customize the behavior of PyLint, such as enabling/disabling certain checks, adjusting thresholds, and more. Generate a configuration file using:


``` bash
pylint --generate-rcfile > .pylintrc
```

### Integrating with IDEs

Many Integrated Development Environments (IDEs) and text editors, such as Visual Studio Code, PyCharm, and Sublime Text, support PyLint integration. This allows you to see linting results directly within your editor as you write code.
