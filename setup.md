---
title: Setup
---


## Setup

## Installing Python

::::::::::::::::::::::::::::::::::::::: discussion

In order to teach this course we will work on some short pieces of code. [Python][python] has been chosen as the language to fulfill that task. 

If you already have python 3 installed in your system then you are good to go. If not I suggest you use Anaconda to setup a virtual environment. To that end you should install [Miniconda3][miniconda3] on your system prior to
attending the course.

If you are already familiar with Python and Virtual Environments you can simply create a fresh virtual environment to
use for the course.

:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: solution

### Installing Miniconda

Please follow the instructions at [Installing Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)
for your Operating System.

:::::::::::::::::::::::::

:::::::::::::::: solution

### Creating A Virtual Environment

You will have to create a virtual environment to undertake the course. If you have installed Miniconda as described
above you open a terminal (Windows use the Git Bash Shell) and create a Virtual Environment called `git-collaboation`.

``` bash
conda create --name git-collaboration python=3.11
conda activate git-collaboration
```

:::::::::::::::::::::::::



## Linting

::::::::::::::::::::::::::::::::::::::: discussion

We will learn what is code linting and we will use one tool called [pylint](https://www.pylint.org/). You will need to install this tool in order to use it. It is important to install the correct version of the software. For this lecture we will use pylint 3.2.2.

:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: solution

### Using pip

To install pylint with pip

``` bash
pip3 install pylint==3.2.2
```

:::::::::::::::::::::::::



:::::::::::::::: solution

### Using conda

To install pylint with conda

``` bash
conda install pylint=3.2.2
```

:::::::::::::::::::::::::


