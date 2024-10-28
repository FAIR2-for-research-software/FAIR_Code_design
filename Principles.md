---
title: "Principles of Code design"
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions 

- How to write maintainable, readable, resusable and scalable code?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Be familiar with standard principles of code design
- Understand what they mean and how to apply them

::::::::::::::::::::::::::::::::::::::::::::::::

## Don't repeat yourself (DRY) - Rule of three

#### Introduction

The DRY Principle states: **“Don’t Repeat Yourself.”** It encourages you to minimize duplication by centralizing similar code patterns. This leads to more readable, maintainable, and scalable code.

Why DRY is it important:
- Improves Readability: Code is clearer when it's not cluttered with repeated logic.
- Reduces Bugs: If you need to make changes, you only do it in one place, reducing the chance of errors.
- Saves Time: Updating and testing code is faster when code is organized with minimal duplication.


#### Using functions to avoid repeting code

Instead of writing the same code in multiple places in your script, create a function. This makes updates easier and avoids errors. For example consider the following code:

```Python
price1 = 100 * 1.2
price2 = 150 * 1.2
price3 = 200 * 1.2
print(price1, price2, price3)
```

The same operation is repeated three times with a different value. If you create a function that makes this operation you can refactor your code:

```Python
# With DRY Principle
def calculate_price(base_price):
    return base_price * 1.2

price1 = calculate_price(100)
price2 = calculate_price(150)
price3 = calculate_price(200)
print(price1, price2, price3)
```

#### Using loops instead of manual repetition

In the previous examples we still call the function three time which is not optimal. In general, If you’re applying the same operation to multiple elements, use a loop to avoid repeated code blocks:

```Python
prices = [100, 150, 200]
for price in prices:
    print(calculate_price(price))
```


#### Using constants for common values

When a value is repeated in multiple places, declare it as a constant variable. This way, you only need to change it once if necessary. Consider the following code:

```Python
total = (100 * 0.1) + (200 * 0.1) + (300 * 0.1)
```

The value `0.1` is repeated three times. If you want to change it, you will need to do it three times. To save time and to add some clarity to your code, you may want to declare the value `0.1`, as follows:

```Python
TAX_RATE = 0.1
total = (100 * TAX_RATE) + (200 * TAX_RATE) + (300 * TAX_RATE)
```

Now if you want to change `0.1` to `0.2` you need to do it only once. In addition, now you have a better idea of what that constant is! The code is already clearer.



::::::::::::::::::::::::::::::::::::: challenge

Write a code, without repetition, that produces the following output:

```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

::::::::::::::::::::::::::::::::::::::::::::::::


#### Summary

**DRY helps you write clear, efficient, and error-resistant code**. Use functions, loops, and constants to reduce repetition. A DRY approach **saves time and effort in the long run**, especially when scaling or debugging code.

It is important to note that prematurly refactoring a code might lead to the unecessary complexity. This is why **DRY** is often associated to the **Rule of Three**. The latter is a guideline suggesting that you should wait until a piece of code is repeated three times before refactoring it. It ensures that you only refactor when a pattern is stable and repeated enough time.




## Keep it simple, Stupid (KISS) & Curly's Law - Do one Thing


## You aren't gonna need it (YAGNI)


## Principle of least astonishment (POLA)


## Code for the maintainer

