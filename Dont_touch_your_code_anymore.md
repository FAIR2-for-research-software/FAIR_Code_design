---
title: "Don't touch your code anymore!"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can you modify your code configuration without touching it?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Learn how to set up configuration files using a simple INI file
- Be able to create simple command line interfaces with argparse

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Research software is often based on a trial-error or trial-trial loops. You will often find yourself trying to rerun a code with different parameters to try different configuration of your code. So far what we have seen deals with the design of the code itself and how to make it cleaner, more readable and maintainable. BUT! what is you need to try something new by changing few parameters of your code? You will need to go and change the code itself! And it is very likely that you will do this a few times (or a lot!). Along the way, and unless you are able to track very well all your trials, you will probably loose track of some of them. In addition, modifying endlessly the code increase greatly the risk of introducing errors...

In order to avoid such problems we are going to see a couple of options that are easily available and implementable:
- Configuration files
- Command line interface 


## Configuration files

### Advantages of using configuration files

Using configuration files in a research context offers several specific benefits that can greatly enhance the efficiency, reproducibility, and manageability of research projects. Here are the key reasons why configuration files are beneficial in a research setting:


- Reproducibility: Configuration files ensure that experiments can be easily replicated by maintaining consistent settings across different runs. This is critical for verifying results and peer review.

- Parameter Management: Research often involves experimenting with various parameters. Configuration files allow researchers to manage and tweak these parameters without altering the core codebase, enabling easier experimentation and optimization.

- Collaboration: Research projects often involve collaboration between multiple researchers. Configuration files provide a clear and centralized way to share settings, making it easier for team members to understand and modify the setup as needed.

- Documentation: Well-structured configuration files serve as documentation for the experimental setup. They provide a clear and organized record of the settings used, which is crucial for understanding and interpreting results.

- Version Control: Configuration files can be versioned alongside the code using version control systems like Git. This makes it easy to track changes in experimental setups over time and understand the impact of these changes on the results.

### How to build configuration files? What library should I use?

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

INI files are structured as (case sensitive) sections in which you can list keyword/value pairs (like for a dictionary) separated by either the `=` or `:` signs. Values can span multiple lines and comments are accepted as long as the extra lines are  indented with respect to the first line. 
 

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

JSON files are also structured as section and keyword/value pairs. JSON files start with an opening brace `{` and end with a closing brace `}`. Then each section comes with its name followed by `:`. Then key/value pairs are listed within braces (one for each section). Nevertheless, comments are not allowed.


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




### Configparser: loading and writing config files

In the following we will be using INI files. We will start by a simple exercice on writing a configuration file manually. 

 
::::::::::::::::::::::::::::::::::::: challenge

Using the text editor of your choice, create an INI file with three sections: simulation, environment and initial conditions. 
In the first section, to parameters are given: `time_step` set at 0.01s and `total_time` set at 100.0s. The environment section also has two parameters with `gravity` at 9.81 and `air_resistance` at 0.02. Finally the initial conditions are: `velocity` at 10.0 km/s, `angle` at 45 degrees and `height` at 1 m

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




#### Reading configuration files


#### Writing configuration files


#### Exercice: 

::::::::::::::::::::::::::::::::::::: challenge

Create a Python script that reads from, writes to, and modifies the following configuration files using the configparser module. This script will simulate managing settings for a simple application.


```
[simulation]
time_step = 0.01
total_time = 100.0

[environment]
gravity = 9.81
air_resistance = 0.02

[initial_conditions]
initial_velocity = 10.0
initial_angle = 45.0
initial_height = 0.0
```
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

```
# Step 2: Read the Configuration File
config = configparser.ConfigParser()
config.read('config.ini')

# Step 3: Print the Configuration
print("Sections:", config.sections())

print("\n[simulation]")
for key in config['simulation']:
    print(f"{key} = {config['simulation'][key]}")

print("\n[environment]")
for key in config['environment']:
    print(f"{key} = {config['environment'][key]}")

print("\n[initial_conditions]")
for key in config['initial_conditions']:
    print(f"{key} = {config['initial_conditions'][key]}")

# Step 4: Modify the Configuration
config['simulation']['time_step'] = '0.005'
config['environment']['air_resistance'] = '0.03'
config['initial_conditions']['initial_velocity'] = '12.0'

# Step 5: Write the Updated Configuration Back to the File
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Step 6: Verify the Changes
config.read('config.ini')

print("\nUpdated [simulation]")
for key in config['simulation']:
    print(f"{key} = {config['simulation'][key]}")

print("\nUpdated [environment]")
for key in config['environment']:
    print(f"{key} = {config['environment'][key]}")

print("\nUpdated [initial_conditions]")
for key in config['initial_conditions']:
    print(f"{key} = {config['initial_conditions'][key]}")
```

:::::::::::::::::::::::::::::::::






