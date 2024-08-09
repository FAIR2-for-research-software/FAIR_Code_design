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


## Readbility counts 

As Guido van Rossum (Python creator and Benevolent dictator for life) once said ''Code is read much more often than it is written''

While coding you may spend of a few hours (days) on a piece of code and when you will be done with it you will not write it again. Nevertheless there is a very high chance that you will read it again. If the piece of code is part of an on-going project you will have to remember what that code does and why you actually wrote it. Hence, readability counts! Remembering what a code does after a few weeks/months is not easy. **If you follow the standard guidelines it will greatly help you (and save you a lot of time!)**. 

In addition, if multiple people are looking at the code and developing with you, writing readable code is paramount. If people have to decipher your coding style before actually trying to understand what you are coding that will become very difficult for everybody. PEP8 provides a standardisation of the python coding style. 


## Explicit is better than implicit.

Naming convention

## Beautiful is better than ugly 

Code layout, indentation, maximum line length

## Sparse is better than dense.

Whitespace


## If the implementation is hard to explain, it’s a bad idea...If the implementation is easy to explain, it may be a good idea.


Comments and documentation strings




## Errors should never pass silently....Unless explicitly silenced



## Simple is better than complex...complex is better than complicated


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


Let's have a look at an example: Consider that file [here]() and run PyLint on it.
 
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

You should get a result that look like this:

```bash

```

:::::::::::::::::::::::::::::::::




### Configuration: 

PyLint can be configured to match your specific project requirements. You can create a configuration file (.pylintrc) to customize the behavior of PyLint, such as enabling/disabling certain checks, adjusting thresholds, and more. Generate a configuration file using:


``` bash
pylint --generate-rcfile > .pylintrc
```

### Integrating with IDEs

Many Integrated Development Environments (IDEs) and text editors, such as Visual Studio Code, PyCharm, and Sublime Text, support PyLint integration. This allows you to see linting results directly within your editor as you write code.
