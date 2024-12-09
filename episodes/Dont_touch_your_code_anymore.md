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

Until now, what we have seen deals with the design of the code itself and how to make it cleaner, more readable and maintainable. Now we are going to see how to reduce the amount of time you change the code while still modify parameters. 
Research is often based on a trial-error or trial-trial loops. You will often find yourself trying to rerun a code with different parameters to try different configuration. Hard coding this values can lead to inflexibility and error-prone results because it means that you will need to go change the code itself to change the configuration. In addition, and unless you are able to track very well all your trials, you will probably loose track of some of them. 

## Configuration files

### Why would need them?

Configuration files will allow you to adjust some parameters of the code (it can be filenames, directories, values, etc) while actually leaving the code untouched. 

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


- TOML files are a bit more recent than the other ones but start to be widely use in Python (a simple example is the setup.py file for installation that became a pyproject.toml file in the last years). They allow structure and data formats. They are quite similar to INI files for the syntax. It is worth mentioning that the library [tomllib](https://docs.python.org/3/library/tomllib.html) is part of the Python standard library from python versoin 3.11. 

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

``` Python
#Let's import the ConfigParser object directly
import ConfigParser 

# And create a config object
config = ConfigParser()
```

Creating a configuration is equivalent to creating a dictionaries:

``` Python
config['simulation'] = {'time_step': 1.0, 'total_time': 200.0}
config['environment'] = {'gravity': 9.81, 'air_resistance': 0.02}
config['initial_conditions'] = {'velocity': 5.0, 'angle': 30.0, 'height': 0.5}
```

And finally you will have to save it:

``` Python
with open('config_file_program.ini', 'w') as configfile: ##This open the config_file_program.ini in write mode
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

Consider the following INI file:

```
[fruits]
oranges = 3
lemons = 6
apples = 5

[vegetables]
onions = 1
asparagus = 2
beetroots = 4
```

Read it using the configparser library. Then you will change the number of beetroot to 2 and the number of oranges to 5 and a section 'pastries' with 5 croissants. Then save it back on disk in a different file.



:::::::::::::::::::::::: solution


```Python
##Import the package
import configparser

###create the object
config = configparser.ConfigParser()

##read the file
config.read('conf_fruit.ini')


###Change the values
config['fruits']['oranges'] = str(5)
config['vegetables']['beetroots'] = str(2)

###Add a section with a new key/pair value
config['pastries'] = {'croissants': '5'}


##save it back
with open('new_conf_fruits', 'w') as openconfig:
    config.write(openconfig)
```

:::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::::::::::::::

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
parser = argparse.ArgumentParser(description='This program is an example of command line interface in Python',
 				                         epilog='Author: R. Thomas, 2024, UoS')

```

Once this is written, you need to tell the program to analyse (parse) the arguments passed to program. This is done with the `parse_args()` method:

```
args = parser.parse_args()
```

If you save everything in a python file (e.g. `cli_course.py`) and run `python cli_course.py --help` you will see the following on the terminal:

```
usage: cli_course.py [-h]

This program is an example of command line interface in Python

optional arguments:
  -h, --help  show this help message and exit

Author: R. Thomas, 2024, UoS
``` 


You can see that the only option that was implemented is the `help`. It is done by constructing the command line interface and you do not need to implement it yourself. Now let's add extra arguments!


#### Define command line arguments

The `argparse` modules implements the `add_argument` method to add argument. Based on the code we prepared before, you would use if this way:

``` Python
parser.add_argument(SOMETHING TO ADD HERE)
```

Two main types of arguments are possible:
* Optional arguments: their name start by `-` or `--` and are called in the terminal by their name. They can be ignored by the user.
* Positional arguments: Their name DO NOT start by `-` or `--`, the user cannot ignore them and they are not to be called by their name (just the value need to be passed).

For example, you can add this three lines before the `args = parser.parse.args()` in the file `commandline.py` that you created before:

``` Python
parser.add_argument('file')               # positional argument (mandatory)
parser.add_argument('file2')              # positional argument (mandatory)
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-n')                 # option that takes a value
parser.add_argument('--max')              # option that takes a value
```

If once again you want to print the help in the terminal `python commandline.py --help` you will see the following being displayed:


```
usage: cli_course.py [-h] [-c COUNT] [-n N] [--max MAX] file file2

This program is an example of command line interface in Python

positional arguments:
  file
  file2

optional arguments:
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

- `action`: this options allows you to do store boolean values.

- `default`: This allows you to define a default value for the argument. In the case thr argument will not be used by the user, the default value will be selected: `parser.add_argument('--color', default='blue')`.

- `type`: By default, the argument will be extracted as strings. Nevertheless, it is possible to have them interpreted as other types using the `type` argument: `parser.add_argument('-i', type=int)`. It the user passes a value that cannot be converted to the expected type an error will be returned.

- `choices`: If you want to restrict the values an argument can take, you can use the `choice` option to add this contraints: `parser.add_argument('--color', choices=['blue', 'red', 'green'])`. If the user pass 'purple' as value, an error will be raised. 

Finally you must be able to retrieve all the argument values:

#### How to get values from the CLI?

To get values from the command line interface you need to look into the `args` variable that you defined with the line `args = parser.parse_args()`. Each argument can be called via the structure 'arge.' + argument name:

```
args = parser.parse_args()
print(args) # Gives the namespace content
print(args.file) #direct access to the 1st positional argument
print(args.max) #direct access to the max optional argument
```

Below we give a couple of examples of calls to the program with different configurations:
```
[user@user]$ python cli_course.py file1path/file.py -c 3 --max 5
usage: cli_course.py [-h] [-c COUNT] [-n N] [--max MAX] file file2
cli_course.py: error: too few arguments  ####<---One positional argument is missing.

[user@user]$ python cli_course.py file1path/file.py file2path/file2.py -c 3
Namespace(count='3', file='file1path/file.py', file2='file2path/file2.py', max=None, n=None)
file1path/file.py
None
```

::::::::::::::::::::::::::::::::::::: challenge

Create a Python script called `basic_cli.py` that:

Accepts two arguments: `--input_file` (path to the data file) and `--output_dir` (directory for saving results). Prints out the values of these arguments.


Expected output:

```
Input file: /data/input.txt
Output directory: /results/
```


::::::::::::::::::::::::::::::::::::::::::::::::

## Final exercice: Mixing everything

For this last part of the final lecture we will combine a bit of everything we have seen during the module (you should plan for an hour for this exercice).


::::::::::::::::::::::::::::::::::::: challenge

It all start with a configuration [file](https://github.com/FAIR2-for-research-software/FAIR_Code_design/blob/main/Conf_cli_codes/final/conffile.ini) that you should download.

You will create four python files in a directory called 'final':
* a main.py: it will contain the main code of the program
* a cli.py: that will contain the command line interface
* a conf.py: that will handle configuration file
* a simulation.py that will handle the simulation that we are going to fake.
* a __init__.py that will stay empty.

You will start by creating the command line interface in the cli.py file with the following optional arguments:
* --config: that will take a string value and the user will use it to pass the configuration file.
* --timestamp: that will take a float as value
* --save: an action argument. If used it should be true, false otherwise.
You should wrap this up in a function called 'command_line'.

In the main.py, you will import the file cli.py and call the command_line function and start analysing the arguments. If the argument --config is empty (=None), you will close the program with a message printed in terminal ('No config file passed...exit'). 

If something is passed the code wil continue and you will read the configuration file. This will be done by calling the conf.py file where you will create a function call 'read_conf' that takes the file as argument. This function will return a dictionary with the complete configuration. In the main.py, you must retrieve this complete configuration.

Once you are there, check the timestamp option from the command line interface. If something has been given, you should replace, in the configuration, the value under Parameters/time_step by the value given by the user.


With this final configuration (updated or not, depending on the user's request) you will create a simulation. This will be done in the simulation.py. In that file you will create a 'Simulation' class, that takes the three parameters L, M and H from the configuration file as parameters. These parameters will become properties of that class. You will create a method (function inside that class) called 'get_total()' and that makes the addition L+M. 

In the main.py, you will create a Simulation object and then print the result of the 'get_total()' method.

Finally, if the user called the '--save' argument, you will use a function 'write_conf()' that you will create in the conf.py file that will write the final configuration to a file called 'final_conf.ini'.

::::::::::::::::::::::::::::::::::::::::::::::::
