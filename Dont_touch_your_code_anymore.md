---
title: "Don't touch your code anymore!"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can you modify your code configuration without touching it?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the purpose and usage of configuration files and command line interfaces.
- Create, read, and write configuration files in different formats (INI, JSON, YAML)
- Learn to design and implement command-line interfaces (CLI) using argparse
- Integrate configuration files with CLI arguments for dynamic applications.

::::::::::::::::::::::::::::::::::::::::::::::::

## Configuration files

### Why would need them?

Until now, what we have seen deals with the design of the code itself and how to make it cleaner, more readable and maintainable. Now we are going to see how to actually stop touching while still modifying it. 
Research is often based on a trial-error or trial-trial loops. You will often find yourself trying to rerun a code with different parameters to try different configuration. Hard coding this values can lead to inflexibility and error-prone results because it means that you will need to go change the code itself to change the configuration. In addition, and unless you are able to track very well all your trials, you will probably loose track of some of them. 

Configuration files will allow you to adjust these parameters outside the code, improving reproducibility and making the code usable across different contexts.

Benefits:

- **Easier Reproducibility**: By simply changing configuration files, you can reproduce the same results or adjust parameters for new experiments.
- **Collaboration**: Configuration files allow collaborators to use the same script but adjust settings for their own environment. It is also easier to share configurations between collaborators.
- **Minimizing Code Modifications**: Parameters are externalized, making the core code cleaner and more maintainable.
- **Documentation**: Well-structured configuration files serve as documentation for your run. They provide a clear and organized record of the settings used, which is crucial for understanding and interpreting results.
- **Version Control**: Configuration files can be versioned alongside the code using version control systems like Git. 

### Types of configuration files 

As it is often the case in Python, multiple options are available:

- [INI](https://en.wikipedia.org/wiki/INI_file) Files are easy to read and parse. The module used to load these files is [configparser](https://docs.python.org/3/library/configparser.html) and part of the [Python standard Library](https://docs.python.org/3/library/index.html).   

```
[section1]
key1 = value1
key2 = value2

#Comments

[section2]
key1 = value1


[Section3]
key = value3
    multiline
```

INI files are structured as (case sensitive) sections in which you can list keyword/value pairs (like for a dictionary) separated by either the `=` or `:` signs. Values can span multiple lines and comments are accepted as long as the extra lines are indented with respect to the first line. All data are parsed as strings.  
 
- JSON: Originally developed for JavaScript, they are very popular in web applications. The module to read these files is [json](https://docs.python.org/3/library/json.html#module-json) and also part of the standard library.  

```
{
  "section1": {
    "key1": "value1",
    "key2": "value2"
  },
  "section2": {
    "key1": "value1"
  }
}
```

JSON files are also structured as section and keyword/value pairs. JSON files start with an opening brace `{` and end with a closing brace `}`. Then each section comes with its name followed by `:`. Then key/value pairs are listed within braces (one for each section). Nevertheless, comments are not allowed and they might be a little bit more complex to write.


- YAML Files: are also a popular format (used for github action for example). In order to read (and write) YAML files, you will need to install a third party package called [PyYAML](https://pyyaml.org/).

```
section1:
  key1: value1
  key2: value2

section2:
  key1: value1

# Comments
```

YAML files work also with sections and keyword/value pairs.  


- TOML files are a bit more recent than the other ones but start to be widely use in Python (a simple example is the setup.py file for installation that became a pyproject.toml file in the last years). They allow structure and data formats. They are quite similar to INI files for the syntax. It is worth mentioning that the library [tomllib]() is part of the Python standard library from python versoin 3.11. 

```
[section1]
key1 = value1 
key2 = value2

[section2]
key1 = value1
```


### Loading and writing INI files: Configparser

In the following we will be using INI files. We will start by a simple exercice on writing a configuration file, manually. 

 
::::::::::::::::::::::::::::::::::::: challenge

Using the text editor of your choice, create an INI file with three sections: simulation, environment and initial conditions. 
In the first section, two parameters are given: `time_step` set at 0.01s and `total_time` set at 100.0s. The environment section also has two parameters with `gravity` at 9.81 and `air_resistance` at 0.02. Finally the initial conditions are: `velocity` at 10.0 km/s, `angle` at 45 degrees and `height` at 1m.

Do the same for a TOML file.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

Creating a file `'config.ini'` with the following content.

```
[simulation]
time_step = 0.01
total_time = 100.0

[environment]
gravity = 9.81
air_resistance = 0.02

[initial_conditions]
velocity = 10.0
angle = 45.0
height = 0.0
```

:::::::::::::::::::::::::::::::::

#### Reading configuration files: INI

Reading an INI file is very easy. It requires the use of the [Configparser](https://docs.python.org/3/library/configparser.html) library. You do not need to install it because it comes as part of the standard library. When you want to read a config file you will need to import it and create a parser object which will then be used to read the file we created just above, as follows:

``` Python
##Import the library
import configparser 

##Create the parser object
parser = configparser.ConfigParser()

##Read the configuration file
parser.read('config.ini')
```

From there you can access everything that is in the configuration file. Firstly you can access the section names and check if sections are there or not (useful to check that the config file is compliant with what you would expect):

``` Python
>>> print(parser.sections())
['simulation', 'environment', 'initial_conditions'] 


>>>print(parser.has_section('simulation'))
True

>>>print(parser.has_section('Finalstate'))
False
```

Eventually, you will need to extract the values in the configuration file. You can get all the keys inside a section at once:


``` Python
>>> options = parser.options('simulation')
['time_step', 'total_time']
```

You can also extract everything at once, in that caseeach couple key/value will be called an *item*:

``` Python
>>> items_in_simulation = parser.items('simulation')
>>> print(items_in_simulation)
[('time_step', '0.01'), ('total_time', '100.0')]
``` 

That method will return a *list* of *tuples*, each *tuple* will contain the couple key/value. Values will always be of type string. 

Finally, you can access directly values of keys inside a given section like this:

``` Python
>>> time_step = parser['simulation']['time_step']
>>> print(time_step)
0.01
```
By default, *ALL* values will be a *string*. Another option is to use the method `.get()`:

``` Python
>>> time_step_with_get = parser.get('simulation', 'time_step')
>>> print(time_step_with_get)
0.01
```

It will also be giving a string...And that can be annoying when you have some other types because you will have to convert everything to the right type. Fortunately, other methods are available:

- `.getint()` will extract the keyword and convert it to integer
- `.getfloat()` will extract the keyword and convert it to a float 
- `.getboolean()` will extract the keyword and convert it to a boolean. Interestingly, you it return `True` is the value is `1`, `yes`, `true` or `on`, while it will return False if the value is `0`, `no`, `false`, or `off`.


#### Writing configuration files

In some occasions it might also be interesting to be able to write configuration file programatically. **Configparser** allows the user to write INI files as well.
As for reading them, everything starts by importing the module and creating an object:

```
#Let's import the ConfigParser object directly
from configparser import ConfigParser 

# And create a config object
config = ConfigParser()
```

Creating a configuration is equivalent to creating a dictionaries:

```
config['simulation'] = {'time_step': 1.0, 'total_time': 200.0}
config['environment'] = {'gravity': 9.81, 'air_resistance': 0.02}
config['initial_conditions'] = {'velocity': 5.0, 'angle': 30.0, 'height': 0.5}
```

And finally you will have to save it:

```
with open('config_file_program.ini', 'w') as configfile: ##This open the condif_file_program.ini in write mode
    config.write(configfile)
```

After running that piece of code, you will end with a new file called `config_file_program.ini` with the following content:

```
[simulation]
time_step = 1.0
total_time = 200.0

[environment]
gravity = 9.81
air_resistance = 0.02

[initial_conditions]
velocity = 5.0
angle = 30.0
height = 0.5
```

::::::::::::::::::::::::::::::::::::: challenge

Using the [tomllib](https://docs.python.org/3/library/tomllib.html) (json[])docmumentation, write a toml file (withthe same element as the previous exercise and read it back).

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

:::::::::::::::::::::::::::::::::




## Using command line interfaces

### Definition & advantages

A Command Line Interface (CLI) is a text-based interface used to interact with software and operating systems. It allows users to type commands into a terminal or command prompt to perform specific tasks, ranging from file manipulation to running scripts or programs.

When writing research software CLIs are particularly suitable:

- **Configuration**: Using CLI it is easy to modify the configuration of a software without having to touch the source code.

- **Batch Processing**: Researchers often need to process large datasets or run simulations multiple times. CLI commands can be easily scripted to automate these tasks, saving time and reducing the potential for human error.

- **Quick Execution**: Experienced users can perform complex tasks more quickly with a CLI compared to navigating through a GUI.

- **Adding New Features**: Adding new arguments and options is straightforward, making it easy to extend the functionality of your software as requirements evolve.

- **Documentation**: CLI helps document the functionality of your script through the `help` command, making it clearer how different options and parameters affect the outcome.

- **Use in HPCs**: HPCs are often accessible through terminal making command line interfaces particularly useful to start codes from HPCs.

### Creating a command line interface in Python

In Python, there is a very nice module called [argparse](https://docs.python.org/3/library/argparse.html). It allows to write, in a very limited amount of lines, a command line interface. Again, that module is part of the standard library so you do not need to install anything.

As for the configuration files, we must start by importing the module and creating a parser object. The parser object can take a few arguments, the main ones are:

- `prog`: The name of the program
- `description`: A short description of the program.
- `epilog`: Text displayed at the bottom of the help

We would proceed as follows:

``` Python
###import the library
import argparse


###create the parser object
parser = argparse.ArgumentParser(prog='My program',
                                 description='This program is an example of command line interface in Python',
 				 epilog='Author: R. Thomas, 2024, UoS')


```

Once this is written, you need to tell the program to analyse (parse) the arguments passed to program. This is done with the `parse_args()` method:

```
args = parser.parse.args()
```

if you save everything in a python file (e.g. `commandline.py`) and run `python commandline.py --help` you will see the following on the terminal:

```
usage: My program [-h]

This program is an example of command line interface in Python

options:
  -h, --help  show this help message and exit

Author: R. Thomas, 2024, UoS
``` 


You can see that the only option that was implemented is the `help`. It is done by constructing the command line interface and you do not need to implement it yourself. Now let's add extra arguments!


#### Define command line arguments

The `argparse` modules implements the `add_argument` method to add argument. Based on the code we prepared before, you would use if this way:

```
parser.add_argument(SOMETHING TO ADD HERE)
```

Two main types of arguments are possible:
- Optional arguments: their name start by `-` or `--` and are called in the terminal by their name. They can be ignored by the user.
- Positional arguments: Their name DO NOT start by `-` or `--`, the user cannot ignore them and they are not to be called by their name (just the value need to be passed).

For example, you can add this three lines before the `args = parser.parse.args()` in the file `commandline.py` that you created before:

``` Python
parser.add_argument('file')               # positional argument (mandatory)
parser.add_argument('file2')              # positional argument (mandatory)
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-n')                 # option that takes a value
parser.add_argument('--max')                 # option that takes a value
```

If once again you want to print the help in the terminal `python commandline.py --help` you will see the following being displayed:


```
usage: My program [-h] [-c COUNT] [-n N] [--max MAX] file file2

This program is an example of command line interface in Python

positional arguments:
  file
  file2

options:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
  -n N
  --max MAX

Author: R. Thomas, 2024, UoS
```

The help tells you that `file` and `file2` are positional arguments. THe user have to provide the values for each of them (in the right order!). In the next section named 'options', we find the help, that was already there before, and the `count`, `n` and `max` options: 
- The count option can be called by using `-c` OR `--count` and a value `COUNT` that the user will need to provide.
- The `n` option is called using '-n' plus a value
- The `max` option is called using '--max' plus a value


Now that we have defined a few argument, we can tune them a little bit. The first thing you will want to do is to provide the user of your program with a small help. As is stands now, displaying the help tells you what are the arguments to be used but nothing tell you what they actually are. To prevent any confusion, add a one-liner help to your argument:

``` Python
parser.add_argument('file', help='input data file to the program')          # position argument
parser.add_argument('file2', help='Configuration file to the program')      # position argument
parser.add_argument('-c', '--count', help='Number of counts per iteration') # option that takes a value
parser.add_argument('-n', help='Number of iteration')                       # option that takes a value
parser.add_argument('--max', help='Maximum population per iteration')       # option that takes a value
```

These short descriptions will be displayed when using the help:


```
usage: My program [-h] [-c COUNT] [-n N] [--max MAX] file file2

This program is an example of command line interface in Python

positional arguments:
  file                  input data file to the program
  file2                 Configuration file to the program

options:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Number of counts per iteration
  -n N                  Number of iteration
  --max MAX             Maximum population per iteration

Author: R. Thomas, 2024, UoS
```



It is possible to use extra options to define arguments, we list a few here:

- `actions`: this options allows you to do 

- `default`: This allows you to define a default value for the argument. In the case thr argument will not be used by the user, the default value will be selected: `parser.add_argument('--color', default='blue')`.

- `type`: By default, the argument will be extracted as strings. Nevertheless, it is possible to have them interpreted as other types using the `type` argument: `parser.add_argument('-i', type=int)`. It the user passes a value that cannot be converted to the expected type an error will be returned.

- `choices`: If you want to restrict the values an argument can take, you can use the `choice` option to add this contraints: `parser.add_argument('--color', choiced=['blue', 'red', 'green'])`. If the user pass 'purple' as value, an error will be raised. 

- `help`: finally, and it is probably the most important option, you can provide a short description of the argument: `parser.add_argument('--color', help='Color of the curve displayed in the plot')` 

Finally you must be able to retrieve all the argument values:

```
###retrieve all arguments 
args = parser.parse_args()
print(args.start, args.e, args.color)
```


## Final exercice: Mixing command line interface and configuration file 

For this last part of the final lecture we will combine both package we just reviewed: `argparse` and `configparser`. Find the instructions below:


::::::::::::::::::::::::::::::::::::: challenge

The program that you will create will take an optional configuration file. If not configuration file is given, the program will load an internal one that you can find [here](https://github.com/Romain-Thomas-Shef/FAIR_Code_design/blob/main/final_exercice/config_default.conf) (you need to put this next to your code). To do this you will create an optional argument `--file`. 

 arguments:

- `--name`: This argument requires a name. If it is used, the value given will replace the default name in the configuration file.
- `--save`: This argument require a directory as value. If used, the configuration is saved into that directory under the name `X_config.ini` where `X` is the name of the user found in the configuration file OR the one given by the `--name` argument.
 
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution


AHAHAHAHA you really though it would be that easy.... :)

:::::::::::::::::::::::::::::::::
