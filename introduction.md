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

## Scalability

### Definition and key aspects
**Scalability in software refers to the ability of a system, application, or process to handle increased loads or demands without compromising performance, reliability, or efficiency**. This involves the capacity of the software to grow and manage higher demands by adding resources or optimizing the existing ones. Scalability is a critical consideration in software design and architecture, ensuring that the system can accommodate growth in users, transactions, data volume, or other metrics over time.


Multiple types of scalability can be considered, here are a few examples:

- Data scalability: The ability to efficiently store, retrieve, and process large volumes of data.
- User scalability: Supporting an increasing number of simultaneous users without degradation of performance
- Functional scalability: The ability to add new features of functionalities to the software without affecting existing performance


### Benefits
- **Improved Performance**: Scalable systems maintain or improve performance levels as the load increases.

- **Cost Efficiency**: Scalability allows for gradual investment in additional resources as needed, rather than over-provisioning from the start.

- **Reliability and Availability**: Scalable systems often include redundancy and failover mechanisms, improving overall system reliability and uptime.

- **User Satisfaction**: Providing consistent and reliable performance even as user demand grows ensures a better user experience.

- **Future-Proofing**: Designing for scalability ensures that the system can grow and adapt to future requirements without significant overhauls.


## Maintainability

### Definition and key aspects
Maintainability in software refers to the ease with which a software system can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment. Highly maintainable software is designed to be easily understood, tested, and updated by developers, ensuring that the software can evolve over time with minimal effort and cost.

Key aspects:

- Core readibility: your code should be organized logically with meaningful names for variables, functions and classes.  

- Modularity: If you divide your software into distinct modules or components, each responsible for a specific functionality, you will greatly reduce dependencies.

- Documentation: The documentation of the code should be continuously updated to reflect the latest state of the sotware.

- Automated testing: Testing your software is important to make sure that modification and implementatio of new functionalities do not break it. 



### Benefits

- **Reduce technical debt**: Maintainable code is easier to refacto ad improve over time, reducing the accumulation of technical debt. The cost and effort to maintain the software will be significantly reduced

- **Faster development**: If you code is maintainable, it will be easier to understand, modify and extend. It will also be easier to identfy and fix bugs.

- **Increase collaboration**: Having a maintainable code will make it easier for people to join you!

- **Adaptability to new requirements**: if your code is maintainable it will be easier to adapt it to changing (or new) requirements, as it is often the case in research.



## Quizz

Results of the Quiz in mentimeter slides. The question for each code is 'Is this code readable, reusable, maintainable, scalable'?

::::::::::::::::::::::::::::::::: challenge

Code #1: 

```
import numpy
def process_list(data):
    return [numpy.sqrt(x) * 2 + 3 for x in data if x * 1.5 < 5]

#Example usage
input_data = [1, 2, 3, 4, 5, 6]
result = process_list(input_data)
print("processed list:", result)

```

::::::::::::::::: solution

- **Readable**: The code is readable because it uses a list comprehension that is relatively straightforward to understand for someone familiar with Python.
- **Reusable**: The function can be used with any list of integers to filter and transform the data.
- **Scalable**: The function uses a list comprehension, which is efficient for processing lists.

However, the code will be difficult to maintain because:

- There are no comments explaining what the function is doing or why it’s doing it.
- Constraints are not explained.
- The logic includes "magic numbers" (2 and 3) without any explanation or named constants.
- There is no error handling, which makes it harder to maintain when unexpected inputs occur.

::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::



::::::::::::::::::::::::::::::::: challenge

Code #2: 

```
def b(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return b(m - 1, 1)
    else:
        return b(m - 1, b(m, n - 1))

# Example usage
result = b(3, 2)
print("Result:", result)
```

::::::::::::::::: solution

This code implements the Ackermann function, a classic example of a computationally intensive function.

- **Maintainable**: The code is structured and easy to update. 
- **Reusable**: You can call the b function with different arguments to compute the Ackermann function for different inputs. 
- **Scalable**: It is a recursive function that computes the Ackermann function efficiently.

Nevertheless, the code is difficult to read:

The code may not be very readable to someone unfamiliar with the Ackermann function or the specific implementation details. The function name *b* and the lack of comments or descriptive variable names may make it difficult to understand at first glance.
::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::: challenge

Code #3: 

```
def calculate_statistics():
    data = [23, 45, 12, 67, 34, 89, 23, 45, 23, 34]
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count
    
    data_sorted = sorted(data)
    if count % 2 == 0:
        median = (data_sorted[count // 2 - 1] + data_sorted[count // 2]) / 2
    else:
        median = data_sorted[count // 2]

    occurrences = {}
    for num in data:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    mode = max(occurrences, key=occurrences.get)

    print("Sum:", total_sum)
    print("Average:", average)
    print("Median:", median)
    print("Mode:", mode)

# Calculate statistics for the specific data set
calculate_statistics()

```

::::::::::::::::: solution

- **Maintainable**: The code is well-structured, with clear variable names and straightforward logic. It's easy to understand and modify if needed.
- **Readable**: The code uses descriptive variable names and simple constructs, making it easy to follow.
- **Scalable**: The code efficiently handles the data processing tasks (sum, average, median, mode) for a list of numbers.


However, the code is not reusable because the function calculate_statistics is hardcoded to work with a specific dataset defined within the function. It cannot be easily reused with different datasets without modifying the function itself.

::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::: challenge

Code #4: 

```
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: The factorial of the given number n.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")
```

::::::::::::::::: solution

- **Maintainable**: The code is well-structured with a clear base case and recursive case. The function is documented, explaining what it does and the parameters it takes.
- **Readable**: The variable names are descriptive, and the function logic is simple and easy to follow. The use of comments and a docstring further enhances readability.
- **Reusable**: The factorial function can be reused to calculate the factorial of any non-negative integer.

However, the recursive approach to calculating factorial is not scalable for large values of n due to the risk of stack overflow and the inefficiency of repeated function calls. For large inputs, this implementation will not perform well and can cause a maximum recursion depth exceeded error in Python.

::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::


