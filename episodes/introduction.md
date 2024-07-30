---
title: "Introduction"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- Why should you know about code design?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the 4 main concepts developed in this course: Maintainability, readability, reusability and scalibility

::::::::::::::::::::::::::::::::::::::::::::::::

## Why should you care?

### Reproducibility and Reliability
Good code practices ensure that research results are reproducible and reliable. Research findings are often scrutinized and validated by others in the field, and well-written code facilitates this process. Clean, well-documented, and well-tested code allows other researchers to replicate experiments, verify results, and build upon existing work, thus advancing scientific knowledge.

### Efficiency and Maintainability
Writing good code enhances efficiency and maintainability. Research projects can span several years and involve multiple collaborators. Readable and well-structured code makes it easier for current and future researchers to understand, modify, and extend the software. This reduces the time and effort required to troubleshoot issues, implement new features, or adapt the code for different datasets or experiments.

### Collaboration and Community Contribution
Good coding practices facilitate collaboration and contribution from the wider research community. Open-source research software, written with clear, standardized coding practices, attracts contributions from other researchers and developers. This collaborative environment can lead to improvements in the software, innovative uses, and more robust and versatile tools, ultimately benefiting the entire research community.



## Designing your code is a continuous process

Research software development is inherently a continuous process driven by the need to adapt to evolving scientific requirements, maintain and enhance quality, and integrate new technologies. This ongoing cycle is fueled by feedback from researchers, advancements in scientific methodologies, and technological progress, all of which necessitate regular updates and improvements.

Maintaining and supporting research software involves continuous tasks such as implementation of new fetures, bug fixing and performance optimization. As research needs and computational loads change, software must be regularly updated to optimize performance. A scalable architecture and modular design allow for independent development, deployment, and scaling of individual components, fostering ongoing enhancements. Regular usability testing, peer reviews, and iterative design improvements ensure that research software remains user-friendly and meets evolving scientific needs.

The benefits of continuous research software development are significant, including enhanced responsiveness to researcher feedback and advancements in the field, higher quality through ongoing testing and improvements, and fostering innovation by incorporating new scientific methods and technologies. However, this approach also presents challenges, such as managing resources effectively, ensuring team coordination, and addressing technical debt. Overall, a continuous development process ensures that research software remains relevant, secure, and valuable to the scientific community over time.

![Designing loop](fig/Loop.png)


## Readability

### Definition and key aspects
Readability in software refers to **how easily a human reader can understand the purpose, control flow, and operation of the code**. High readability means that the code is clear, easy to follow, and well-organized, which greatly enhances maintainability, collaboration, and reduces the likelihood of bugs.

Key aspects:

- Descriptve Naming: Use meaningful and descriptive names that convey the purpose of the variable.

- Consistent Formatting: Consistent indentation improves the visual structure of the code. Keeping lines of code within a reasonable length (usually 80-100 characters) prevents horizontal scrolling and improves readability.

- Comments and documentation: Brief comments within the code explaining non-obvious parts. Detailed documentation at the beginning of modules, classes, and functions explaining their purpose, parameters, and return values.

- Code structure: Breaking down code into functions, classes, and modules that each handle a specific task. Group related pieces of code together, and separate different functionalities clearly.

### Benefits:

1 - **Maintainability**: Your code will be easier to understand and modify the code. It will also greatly reduce the risk of errors when introducing changes.

2 - **Collaboration**: writing readable code will enhance teamwork and make it easy for others to contribute. Code reviews will be easy!

3 - **Efficiency**: You are going to save a LOT of time. You will waste less time deciphering your code. That saved time will be used to develop the code.

4 - **Quality**: Reduces the likelihood of bugs and errors, leading to more reliable code


## Reusability

### Definition and Key aspects

Reusability in software refers to the ability to use existing software components (such as functions, classes, modules, or libraries) across multiple projects or in different parts of the same project without significant modification. Reusable code is designed to be generic and flexible, promoting efficiency, reducing redundancy, and enhancing maintainability.

Key aspects:

- Modularity: Encapsulate functionality within well-defined modules or classes that can be independently reused.

- Abstraction: Provide simple interfaces while hiding the complex implementation details.

- Parametrization: Design functions and methods that accept parameters to make them adaptable to different situations.

- Generic and Reusable Components: Develop generic libraries and utility functions that can be reused across multiple projects.

- Documentation and Naming: Provide comprehensive documentation for modules, classes, and functions to explain their usage. 

- Avoid hardcoding values:  Instead, use constants or configuration files.


### Benefits:

- **Time saving**: Reusable components save development time. You don't need to rewrite from sratch! Avoids duplication of effort by using existing solutions for common tasks.

- **Consistency**: Using the same code components across projects ensures consistency in functionality and behavior. 

- **Maintainability**: Reusable components can be maintained and updated independently, making it easier to manage large codebases.

- **Quality**: Reusable components are often well-tested, leading to more reliable and bug-free software

## Maintainability

### Definition
Maintainability in software refers to the ease with which a software system can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment. Highly maintainable software is designed to be easily understood, tested, and updated by developers, ensuring that the software can evolve over time with minimal effort and cost.

Key aspects:

- Core readibility:  

- Modularity:

- Documentation: 

- Consistent formating:

- Automated testing:

- Version Control:

- Refactoring: 


###Benefits

## Scalability

### Definition and key aspects
**Scalability in software refers to the ability of a system, application, or process to handle increased loads or demands without compromising performance, reliability, or efficiency**. This involves the capacity of the software to grow and manage higher demands by adding resources or optimizing the existing ones. Scalability is a critical consideration in software design and architecture, ensuring that the system can accommodate growth in users, transactions, data volume, or other metrics over time.


Multiple types of scalability can be considered, here are a few examples:

- Data scalability: The ability to efficiently store, retrieve, and process large volumes of data.
- User scalability: Supporting an increasing number of simultaneous users without degradation of performance
- Functional scalability: The ability to add new features of functionalities to the software without affecting existing performance


### Benefits
- Improved Performance: Scalable systems maintain or improve performance levels as the load increases.

- Cost Efficiency: Scalability allows for gradual investment in additional resources as needed, rather than over-provisioning from the start.

- Reliability and Availability: Scalable systems often include redundancy and failover mechanisms, improving overall system reliability and uptime.

- User Satisfaction: Providing consistent and reliable performance even as user demand grows ensures a better user experience.

- Future-Proofing: Designing for scalability ensures that the system can grow and adapt to future requirements without significant overhauls.



## Quizz

---> Got to [this website](https://www.mentimeter.com/) and enter the following code:


::::::::::::::::::::::::::::::::::::: challenge 

## Challenge 1: Can you do it?

What is the output of this command?

```r
paste("This", "new", "lesson", "looks", "good")
```

:::::::::::::::::::::::: solution 

## Output
 
```output
[1] "This new lesson looks good"
```

:::::::::::::::::::::::::::::::::

