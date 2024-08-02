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

INI files is structured as (case sensitive) sections in which you can list keyword/values (like for a dictionary) separated by either the `=` or `:` signs. Values can span multiple lines and comments are accepted as long as the extra lines are  indented with respect to the first line. 
 

- JSON: Originally developed for JavaScript, very popular in web applications.  


- YAML Files: are also a popular
