[README_Project8.md](https://github.com/user-attachments/files/32512594/README_Project8.md)
# NumPy Analyzer

## Project Overview

**NumPy Analyzer** is a Python-based, menu-driven application developed using **NumPy**. The project allows users to create and analyze **1D, 2D, and 3D NumPy arrays** through an interactive console menu.

The project demonstrates NumPy array creation, indexing, slicing, mathematical operations, combining and splitting arrays, searching, sorting, filtering, and statistical analysis. It also applies Python Object-Oriented Programming concepts such as classes, constructors, class methods, static methods, private attributes, and private helper methods.

## Objective

The main objectives of this project are:

- To understand NumPy arrays and their dimensions.
- To create 1D, 2D, and 3D arrays using user input.
- To perform indexing and slicing operations.
- To perform mathematical and matrix operations.
- To combine and split arrays.
- To search, sort, and filter array elements.
- To calculate statistical values from arrays.
- To implement NumPy functionality using a Python class.
- To build a simple menu-driven analytical application.

## Technologies Used

- **Python**
- **NumPy**
- **Jupyter Notebook**

## Project Structure

```text
NumPy Analyzer
│
├── Import NumPy
│
├── DataAnalyst Class
│   ├── Constructor
│   ├── 1D Array Creation
│   ├── 2D Array Creation
│   ├── 3D Array Creation
│   ├── Display Array
│   ├── Indexing
│   ├── Slicing
│   ├── Mathematical Operations
│   ├── Search, Sort and Filter
│   ├── Aggregates and Statistics
│   └── Combine and Split
│
└── Main Menu
    ├── Create a NumPy Array
    ├── Perform Mathematical Operations
    ├── Combine or Split Arrays
    ├── Search, Sort, or Filter Arrays
    ├── Compute Aggregates and Statistics
    └── Exit
```

## Features

### 1. Create a NumPy Array

The application supports three types of arrays:

- 1D Array
- 2D Array
- 3D Array

For a 2D array, the user enters the number of rows, columns, and elements.

For a 3D array, the user enters the number of layers, rows, columns, and elements.

Example:

```text
Choose an option:
1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

### 2. Indexing

The application allows users to access individual elements.

For example:

- 1D array → index
- 2D array → row and column index
- 3D array → layer, row, and column index

### 3. Slicing

The application supports slicing for all three array dimensions.

Examples include:

```python
array[start:end]
```

For a 2D array:

```python
array[row_start:row_end, column_start:column_end]
```

For a 3D array:

```python
array[layer_start:layer_end,
      row_start:row_end,
      column_start:column_end]
```

### 4. Mathematical Operations

The project provides:

- Addition
- Subtraction
- Multiplication
- Division
- Dot Product
- Matrix Multiplication

The program also checks for conditions such as division by zero and compatible matrix dimensions.

### 5. Combine and Split Arrays

Arrays can be combined or split according to their dimensions.

For 1D arrays:

- Concatenation

For 2D arrays:

- Vertical combination
- Horizontal combination

For 3D arrays:

- Combination along Axis 0
- Combination along Axis 1
- Combination along Axis 2

The application also supports splitting arrays into multiple parts.

### 6. Search, Sort and Filter

The project provides:

#### Search

Searches for a specified value using NumPy.

```python
np.where()
```

#### Sort

Sorting options depend on the array dimension.

For 1D arrays:

- Ascending
- Descending

For 2D arrays:

- Column-wise ascending
- Column-wise descending
- Row-wise ascending
- Row-wise descending

For 3D arrays:

- Axis 0 ascending/descending
- Axis 1 ascending/descending
- Axis 2 ascending/descending

#### Filter

The application can filter elements greater than a user-specified value.

```python
array[array > value]
```

### 7. Aggregates and Statistics

The project calculates:

- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum
- Maximum
- Percentile
- Correlation

Important NumPy functions used include:

```python
np.sum()
np.mean()
np.median()
np.std()
np.var()
np.min()
np.max()
np.percentile()
np.corrcoef()
```

## Object-Oriented Programming Concepts

The project uses a `DataAnalyst` class to organize the NumPy operations.

### Constructor

```python
def __init__(self, array=None):
    self.__array = array
```

The constructor initializes the array.

### Private Attribute

```python
self.__array
```

The double underscore makes the array attribute private within the class.

### Class Methods

The project uses class methods to create arrays:

```python
@classmethod
def create_1D(cls):
```

```python
@classmethod
def create_2d(cls):
```

```python
@classmethod
def create_3d(cls):
```

These methods create objects containing the required NumPy arrays.

### Static Method

The class also contains:

```python
@staticmethod
def show_title():
```

A static method does not require the class instance or class itself to access instance data.

### Private Helper Methods

The project uses private methods to create secondary arrays or matrices:

```python
__get_second_array()
```

```python
__get_second_matrix()
```

These methods are used internally by other operations.

## Program Flow

```text
Start
  ↓
Import NumPy
  ↓
Create DataAnalyst class
  ↓
Display Main Menu
  ↓
Create 1D / 2D / 3D Array
  ↓
Store Array in DataAnalyst Object
  ↓
Perform Selected Operation
  ↓
Display Result
  ↓
Return to Main Menu
  ↓
Exit
```

## Main Menu Options

| Option | Operation |
|---|---|
| 1 | Create a NumPy Array |
| 2 | Perform Mathematical Operations |
| 3 | Combine or Split Arrays |
| 4 | Search, Sort, or Filter Arrays |
| 5 | Compute Aggregates and Statistics |
| 6 | Exit |

## Installation

Make sure Python is installed on your system.

Install NumPy using:

```bash
pip install numpy
```

In Jupyter Notebook, you can also run:

```python
!pip install numpy
```

## How to Run

1. Open the Jupyter Notebook containing the project.
2. Run the NumPy installation cell if required.
3. Run the import cell.
4. Run the `DataAnalyst` class cell.
5. Run the main program cell.
6. Select an option from the displayed menu.
7. Enter the required array values.
8. Perform the required operation.
9. Select **6** to exit the application.

## Example

```text
Welcome to the NumPy Analyzer !
=================================

Choose an option:
1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit

Enter your choice: 1
```

For a 1D array:

```text
Create a NumPy Array

Select the type of array you want to create
1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 1

Write the elements to be filled in 1D Array
12 23 45 67

Array created successfully!

Current Array

[12. 23. 45. 67.]
```

## Error Handling and Validation

The project includes input validation for several operations, including:

- Invalid menu choices
- Incorrect number of array elements
- Division by zero
- Invalid percentile values
- Invalid number of split parts
- Incompatible matrix dimensions
- Invalid array axis selection

## Learning Outcomes

After completing this project, the following concepts are practiced:

- NumPy arrays
- Array dimensions and shapes
- Array indexing
- Array slicing
- Array reshaping
- Mathematical operations
- Matrix operations
- Searching and filtering
- Sorting
- Array concatenation
- Array splitting
- Statistical calculations
- Correlation
- Python classes and objects
- Constructors
- Class methods
- Static methods
- Private attributes
- Private helper methods
- Menu-driven programming

## Conclusion

The **NumPy Analyzer** project provides an interactive way to practice NumPy and Python Object-Oriented Programming. It combines multiple array-analysis operations into one menu-driven application and demonstrates how NumPy can be integrated into a structured Python class.

## Author

**Pranjali Pandya**

B.Tech Bioinformatics  
Marwadi University
