---
title: "Introduction"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can code design make your code more FAIR?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the definition of software in research.
- Understand the FAIR principles as applied to research software.
- Understand how code design is related to the FAIR principles.

::::::::::::::::::::::::::::::::::::::::::::::::

## What is a software in academia?

It is not always easy to define what constitutes software in a research setting. The size of projects can vary from a
small script of a few dozens of lines to a massive project with millions of lines. If you are interested in a discussion
around a research software definition a good starting point is [_Defining Research Software: a controversial
discussion_][defressoft]. An abbreviated summary of this paper and a pragmatic definition we use
as a basis for this course is...

::::::::::::::::::::::::::::::::::::: keypoints

Research Software includes source code files, algorithms, scripts, computational workflows and executables that were
created during the research process or for a research purpose. Software components (e.g., operating systems, libraries,
dependencies, packages, scripts,etc.) that are used for research but were not created during or with a clear research
intent should be considered software in research and not Research Software. This differentiation may vary between
disciplines.

::::::::::::::::::::::::::::::::::::::::::::::::

## Reminder: The FAIR principles applied to research software

The FAIR principles (Findable, Accessible, Interoperable and Reusable) were originally designed for research data in
order to "enhance their re-usability" (see [Wilkinson _et al_ (2016)][fair]). In this seminal paper it was made clear
that while data was a central aspect of research, the principles should also apply to algorithms, tools and workflows
that led to the production of that data. Few years later, in 2022, a set of recommendation was published ([Chue Hon _et
al._ (2022)][fair4rswg]; [Barker _et al._ (2022)][fair4rs]) in order to apply these FAIR principle to research
software. An overview of the FAIR principles adapted to research software are that...

::::::::::::::::::::::::::::::::::::: keypoints

- Findable: Software, and its associated metadata, is easy for both humans and machines to find.

- Accessible: Software, and its metadata, is retrievable via standardised protocols.

- Interoperable: Software interoperates with other software by exchanging data and/or metadata, and/or through
  interaction via Application Programming Interfaces (APIs), described through standards.

- Reusable: Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or
  incorporated into other software).

::::::::::::::::::::::::::::::::::::::::::::::::


## How can Code Design help the FAIR principles?

By designing your code efficiently you will make it FAIRer. Code design is about making your code easy to read, adapt, maintain and share. Here's how some of the principles benefit from good design:

- **Interoperability**: Writing code in a modular way and using standard data format allows other systems to communicate with it.  

- **Reusability**: Documented code, use of docstrings and comments makes it easier for others to understand, use, and modify your code. Using modular design with single-task blocks also increases reusability. Indeed, small simple pieces can be more easily transferred to other projects or extended without significant refactoring.

The goal of this lecture is to dive into these practices and learn a little bit more about how the way you code will greatly enhance how maintainable, adaptable, and sustainable your software is in the long run.


[defressoft]: https://doi.org/10.5281/zenodo.5504016
[fair]: https://doi.org/10.1038/sdata.2016.18
[fair4rs]: https://doi.org/10.1038/s41597-022-01710-x
[fair4rswg]: https://10.5281/zenodo.5504015.
