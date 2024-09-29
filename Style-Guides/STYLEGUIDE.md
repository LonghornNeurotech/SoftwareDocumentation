---
title: Welcome to the LHNT Software Style Guide!

---


---

# Welcome to the LHNT Software Style Guide!

> “*It is not enough for code to work.*” — Robert C. Martin

This document outlines coding standards and best practices for Longhorn Neurotech’s Software Team. It provides a set of rules and guidelines to ensure that all code written for our projects is consistent, readable, and maintainable. As a large organization, it’s crucial to uphold these standards across the team.

This document is intended as a reference rather than a manual to be memorized in a single sitting. Use it to look up specific rules and examples as needed.

*Please note that this guide is not exhaustive.* Covering every potential scenario would result in a 1000-pound LHNT Software Style Tome. For any issues not addressed here for which you have questions, consult your leads for guidance.

> “*Of course bad code can be cleaned up. But it’s very expensive.*”  — Also Robert C. Martin

---

## Table of Contents

1. [Code Layout](#1-code-layout)
   - [1.1 Indentation](#11-indentation)
   - [1.2 Line Length](#12-line-length)
   - [1.3 Blank Lines](#13-blank-lines)
   - [1.4 One Statement Per Line](#14-one-statement-per-line)
2. [Naming Conventions](#2-naming-conventions)
   - [2.1 Variables and Functions: `snake_case`](#21-variables-and-functions-snake_case)
   - [2.2 Constants: `SCREAMING_SNAKE_CASE`](#22-constants-screaming_snake_case)
   - [2.3 Class Names: `PascalCase`](#23-class-names-pascalcase)
   - [2.4 Descriptive Variable Names](#24-descriptive-variable-names)
3. [Variables and Constants](#3-variables-and-constants)
   - [3.1 Avoid Magic Numbers: Use Constants](#31-avoid-magic-numbers-use-constants)
4. [Code Organization](#4-code-organization)
   - [4.1 Functions Should Be Short](#41-functions-should-be-short)
   - [4.2 Use Classes When Appropriate](#42-use-classes-when-appropriate)
5. [Comments and Documentation](#5-comments-and-documentation)
   - [5.1 Docstrings](#51-docstrings)
   - [5.2 Commenting Complex or Confusing Code](#52-commenting-complex-or-confusing-code)
   - [5.3 Comment Judiciously](#53-comment-judiciously)
6. [Imports](#6-imports)
   - [6.1 One Import Per Line](#61-one-import-per-line)
   - [6.2 Import Only What You Need](#62-import-only-what-you-need)
7. [Error Handling](#7-error-handling)
8. [Multithreading Safety](#8-multithreading-safety)

---

## 1. Code Layout

### 1.1 Indentation

#### 1.1.1 4-Space Indentation

**Description:**

Use 4 spaces per indentation level for consistency and readability.

**Correct Implementation:**

```python
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

**Incorrect Implementation:**

```python
def check_even(number):
 if number % 2 == 0:
  return True
 else:
  return False
```

**Explanation:**

The correct code uses 4 spaces for each indentation level. The incorrect code uses inconsistent spacing, which can lead to confusion and errors.

---

### 1.2 Line Length

#### 1.2.1 Limit Lines to 79 Characters

**Description:**

Limit lines to a maximum of 79 characters to enhance readability.

**Correct Implementation:**

```python
def long_function_name(var_one, var_two, var_three, var_four):
    pass  # Function body goes here
```

**Incorrect Implementation:**

```python
def long_function_name(var_one, var_two, var_three, var_four, var_five, var_six):
    pass  # This line exceeds the 79-character limit
```

**Explanation:**

The correct example keeps line length within the limit. The incorrect one has a function definition that is too long and should be broken into multiple lines.

---

#### 1.2.2 Indent Continuation Lines

**Description:**

Indent continuation lines to align with the opening delimiter or to a level that improves readability.

**Correct Implementation:**

```python
total = (first_variable
         + second_variable
         - third_variable)
```

**Incorrect Implementation:**

```python
total = (first_variable +
second_variable - third_variable)
```

**Explanation:**

The correct code aligns the continued lines under the opening parenthesis. The incorrect code breaks the line improperly, reducing readability.

---

### 1.3 Blank Lines

**Description:**

Use blank lines to separate code into logical sections.

**Correct Implementation:**

```python
class MyClass:
    pass


def my_function():
    pass
```

**Incorrect Implementation:**

```python
class MyClass:
    pass
def my_function():
    pass
```

**Explanation:**

The correct code uses a blank line to separate the class and function definitions, enhancing readability.

---

### 1.4 One Statement Per Line

**Description:**

Write only one statement per line to enhance code clarity.

**Correct Implementation:**

```python
is_valid = True
count += 1
```

**Incorrect Implementation:**

```python
is_valid = True; count += 1
```

**Explanation:**

The correct code separates statements onto different lines. The incorrect one combines them with a semicolon, which can be harder to read.

---

## 2. Naming Conventions

> "*You should name a variable using the same care with which you name a first-born child.*" — Also Robert C. Martin

### 2.1 Variables and Functions: `snake_case`

**Description:**

Use lowercase letters with underscores for variable and function names.

**Correct Implementation:**

```python
user_name = "JohnDoe"

def calculate_area(radius):
    pass
```

**Incorrect Implementation:**

```python
UserName = "JohnDoe"

def CalculateArea(radius):
    pass
```

**Explanation:**

The correct names follow the `snake_case` convention. The incorrect ones use `PascalCase`, which is reserved for class names.

---

### 2.2 Constants: `SCREAMING_SNAKE_CASE`

**Description:**

Use uppercase letters with underscores for constants.

**Correct Implementation:**

```python
PI_VALUE = 3.14159
```

**Incorrect Implementation:**

```python
piValue = 3.14159
```

**Explanation:**

The correct constant name uses `SCREAMING_SNAKE_CASE`. The incorrect one does not, making it less clear that the value is intended to be constant.

---

### 2.3 Class Names: `PascalCase`

**Description:**

Use `PascalCase` for class names, capitalizing the first letter of each word without underscores.

**Correct Implementation:**

```python
class DataProcessor:
    pass
```

**Incorrect Implementation:**

```python
class data_processor:
    pass
```

**Explanation:**

The correct class name uses `PascalCase`, while the incorrect one uses `snake_case`, which should be reserved for variable and function names.

---

### 2.4 Descriptive Variable Names

**Description:**

Choose variable names that clearly indicate their purpose.

**Correct Implementation:**

```python
average_score = total_score / number_of_tests
```

**Incorrect Implementation:**

```python
a = b / c
```

**Explanation:**

The correct code uses descriptive names, making the calculation clear. The incorrect code uses ambiguous single-letter variables.

---

## 3. Variables and Constants

### 3.1 Avoid Magic Numbers: Use Constants

**Description:**

Avoid using unexplained numbers in code; define them as constants with meaningful names.

**Correct Implementation:**

```python
MAX_USERS = 100

if current_user_count > MAX_USERS:
    print("User limit reached.")
```

**Incorrect Implementation:**

```python
if current_user_count > 100:
    print("User limit reached.")
```

**Explanation:**

The correct code uses a named constant, making the purpose of `100` clear. The incorrect code uses a magic number, which can be confusing.

---

## 4. Code Organization

> "*Functions should do one thing. They should do it well. They should do it only.*" — Also Robert C. Martin

### 4.1 Functions Should Be Short

**Description:**

Keep functions concise (under 25 lines) to ensure they are easy to understand and maintain.

**Correct Implementation:**

```python
def authenticate_user(username, password):
    # Code to authenticate user
    pass
```

**Incorrect Implementation:**

```python
def authenticate_user(username, password):
    # Overly long function with multiple responsibilities
    # Code to authenticate user
    # Code to log login attempt
    # Code to update user statistics
    # ...
    pass
```

**Explanation:**

The correct function focuses on a single task. The incorrect one tries to handle multiple tasks, making it too long and complex.

---

### 4.2 Use Classes When Appropriate

**Description:**

Use classes when they provide a clear advantage, such as encapsulating data and behavior.

**Correct Implementation:**

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
```

**Incorrect Implementation:**

```python
class Utility:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b
```

**Explanation:**

The correct example uses a class to represent an object with attributes. The incorrect one uses a class unnecessarily for standalone functions.

---

## 5. Comments and Documentation

### 5.1 Docstrings

**Description:**

Use docstrings to document modules, classes, functions, and methods. They should explain what the code does, its parameters, return values, and any exceptions.

**Correct Implementation:**

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return 3.14159 * radius ** 2
```

**Incorrect Implementation:**

```python
def calculate_area(radius):
    # Calculate area
    return 3.14159 * radius ** 2
```

**Explanation:**

The correct example uses a docstring that provides detailed information about the function, while the incorrect one uses a simple comment that lacks depth and doesn't follow the docstring convention.

**NOTE:** *In this document, we're breaking our own docstring rule! This is so that we don't distract from our examples.*

---

### 5.2 Comment Judiciously

**Description:**

Use comments judiciously to add value without stating the obvious. Avoid cluttering code with unnecessary comments. Add comments to complex or non-obvious code segments.

**Correct Implementation:**

```python
def convert_temperature(celsius):
    # Convert Celsius to Fahrenheit
    return (celsius * 9 / 5) + 32
```

**Incorrect Implementation:**

```python
def convert_temperature(celsius):
    # Multiply celsius by 9
    # Divide the result by 5
    # Add 32 to the result
    return (celsius * 9 / 5) + 32
```

**Explanation:**

The correct example provides a concise comment explaining the overall purpose. The incorrect one includes redundant step-by-step comments that mirror the code.

---

## 6. Imports

### 6.1 One Import Per Line

**Description:**

Write one import statement per line to keep imports clear and manageable.

**Correct Implementation:**

```python
import os
import sys
```

**Incorrect Implementation:**

```python
import sys, os
```

**Explanation:**

The correct example separates imports, making them easier to read and manage. The incorrect one combines imports, which can be less clear.

---

### 6.2 Import Only What You Need

**Description:**

Import only the modules or functions you need to avoid namespace pollution.

**Correct Implementation:**

```python
from math import sqrt
```

**Incorrect Implementation:**

```python
from math import *
```

**Explanation:**

The correct code imports only the `sqrt` function. The incorrect code imports everything from `math`, which can lead to conflicts and unnecessary memory usage.

---

## 7. Error Handling

**Description:**

Include error handling to manage exceptions and provide feedback to the user.

**Correct Implementation:**

```python
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
```

**Incorrect Implementation:**

```python
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
```

**Explanation:**

The correct code uses a try-except block to handle potential file not found errors gracefully. The incorrect code does not handle exceptions, which can cause the program to crash.

---

## 8. Multithreading Safety

### 8.1 Use `if __name__ == "__main__":`

**Description:**

Use this idiom to ensure that certain code runs only when the script is executed directly, not when imported. This is important for multithreading safety.

**Correct Implementation:**

```python
def main():
    start_application()

if __name__ == "__main__":
    main()
```

**Incorrect Implementation:**

```python
def main():
    start_application()

main()
```

**Explanation:**

The correct code checks the `__name__` variable before running `main()`, which prevents unintended code execution when importing and is essential for multithreading safety.

---

If you have any questions, please reach out to your team lead!