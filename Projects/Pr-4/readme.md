# Data Analyzer and Transformer Program

## Overview

The **Data Analyzer and Transformer Program** is a Python menu-driven application that allows users to input, analyze, transform, and display datasets. The program supports both **1D arrays** and **2D arrays** and demonstrates the use of various Python concepts such as:

* Functions
* Recursion
* Lambda Functions
* Filter Function
* Variable Length Arguments (`*args`)
* Built-in Functions
* List Operations

---

## Features

### 1. Input Data

Users can:

* Create a 1D array manually
* Create a 2D array manually
* Use predefined sample data for testing

### 2. Display Data Summary

For 1D arrays, the program displays:

* Length of array
* Sum of elements
* Minimum value
* Maximum value
* Unique values

For 2D arrays, all rows are displayed.

### 3. Calculate Factorial

Uses a recursive function to calculate the factorial of a number.

Example:

Factorial of 5 = 120

### 4. Filter Data by Threshold

Uses a lambda expression with the filter() function to display values greater than a user-defined threshold.

Example:

Array: [23, 43, 12, 56, 78]

Threshold: 40

Output: [43, 56, 78]

### 5. Sort Data

For 1D arrays:

* Ascending order sorting
* Descending order sorting

For 2D arrays:

* Uses sorted() function to sort rows.

### 6. Display Dataset Statistics

Returns multiple values:

* Minimum value
* Average value
* Maximum value
* Total sum

### 7. Display Dataset

Uses variable length arguments (*args) to display all elements of the dataset.

### 8. Exit Program

Terminates the application.

---

## Python Concepts Demonstrated

| Concept            | Usage                         |
| ------------------ | ----------------------------- |
| Functions          | Modular program design        |
| Recursion          | Factorial calculation         |
| Lambda Function    | Threshold filtering           |
| Filter Function    | Data filtering                |
| Built-in Functions | len(), sum(), min(), max()    |
| Variable Arguments | *args                         |
| List Operations    | Input, sorting, unique values |
| Global Variables   | Shared dataset storage        |

---

## Sample 1D Dataset

```python
[23, 43, 12, 56, 78, 78, 90]
```

## Sample 2D Dataset

```python
[
    [1, 3, 4],
    [23, 67, 34],
    [76, 12, 34],
    [90, 23, 12]
]
```

---

## Program Flow

1. Input dataset
2. Choose desired operation
3. View results
4. Continue using other features
5. Exit program

---

## How to Run

### Requirements

* Python 3.x

### Execute

```bash
python filename.py
```

Replace `filename.py` with the name of your Python source file.

---

## Learning Outcomes

By completing this project, students can understand:

* Menu-driven programming
* Data analysis using Python
* Recursive functions
* Lambda expressions
* Filtering and sorting techniques
* Handling 1D and 2D arrays
* Returning multiple values from functions
* Variable length arguments

---

## Author

Data Analyzer and Transformer Program

Developed as a Python practice project to demonstrate data processing and analysis techniques.
