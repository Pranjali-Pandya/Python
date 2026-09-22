[README.md](https://github.com/user-attachments/files/32512157/README.md)
# Pandas Analyzer & Data Visualization

## Project Overview

**Pandas Analyzer & Data Visualization** is a Python-based, menu-driven application developed to perform sales data analysis, data cleaning, data manipulation, statistical analysis, and data visualization.

The project uses **Pandas, NumPy, Matplotlib, and Seaborn** and demonstrates **Object-Oriented Programming (OOP)** concepts through a `SalesDataAnalyzer` class.

---

## Objectives

- Load and explore a sales dataset
- Clean missing and duplicate data
- Perform NumPy array operations
- Perform mathematical operations
- Combine and split DataFrames
- Search, sort, and filter data
- Calculate aggregate functions
- Perform statistical analysis
- Create pivot tables
- Perform GroupBy and Transform operations
- Create different types of visualizations
- Save processed data as a CSV file
- Apply Python OOP concepts

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Manipulation and Analysis |
| NumPy | Numerical and Array Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |

---

## Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

The main libraries are imported as:

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

---

## Project Structure

    Pr-9/
    │
    ├── sales_data_analyzer.py
    ├── sales_data.csv
    ├── README.md
    └── requirements.txt

---

## Dataset

The project uses a CSV file named:

`sales_data.csv`

The dataset contains sales-related information used for data analysis and visualization.

---

# Features

## 1. Load Dataset

The program loads the sales dataset using Pandas.

    pd.read_csv("sales_data.csv")

The dataset is stored in a Pandas DataFrame for further analysis.

---

## 2. Explore Data

The program allows the user to:

- Display first 5 rows
- Display last 5 rows
- Display column names
- Display data types
- Display dataset shape
- Display dataset information
- Display descriptive statistics

### Pandas Functions Used

    head()
    tail()
    columns
    dtypes
    shape
    info()
    describe()

---

## 3. Clean Data

The program performs different data cleaning operations:

- Missing value handling
- Numerical missing value replacement using mean
- Categorical missing value replacement using mode
- Date conversion
- Duplicate removal

### Example

    self.data.drop_duplicates()

---

## 4. NumPy Array Operations

Numerical columns are converted into NumPy arrays.

The program performs:

- Indexing
- Slicing
- Shape checking
- Data type checking

### Example

    array = self.data[column].to_numpy()

---

## 5. Mathematical Operations

The program performs:

- Addition
- Subtraction
- Multiplication
- Division
- Square
- Square Root

### NumPy Functions Used

    np.square()
    np.sqrt()

---

## 6. Combine DataFrames

The program demonstrates different methods for combining DataFrames:

- Concatenation
- Merge
- Join

### Functions Used

    pd.concat()
    pd.merge()
    DataFrame.join()

---

## 7. Split Data

The dataset can be split according to:

- Region
- Product Category
- Sales Representative

---

## 8. Search, Sort and Filter

The program allows users to:

- Search for values
- Sort data in ascending order
- Sort data in descending order
- Filter records based on selected values

---

## 9. Aggregate Functions

The following aggregate functions are performed:

- Sum
- Mean
- Count
- Minimum
- Maximum
- Median

### Example

    self.data[column].sum()
    self.data[column].mean()
    self.data[column].count()
    self.data[column].min()
    self.data[column].max()
    self.data[column].median()

---

## 10. Statistical Analysis

The project performs:

- Descriptive statistics
- Mean
- Standard deviation
- Variance
- Percentiles
- Correlation analysis

### Example

    numeric_data.corr()

---

## 11. Pivot Table

The project creates pivot tables using Pandas.

### Example

    pd.pivot_table(
        self.data,
        index=index_column,
        values=value_column,
        aggfunc="sum"
    )

---

## 12. GroupBy and Transform

The project performs grouped analysis using Pandas `groupby()`.

### Calculations

- Sum
- Mean
- Count

### Example

    self.data.groupby(group_column)[value_column].agg(
        ["sum", "mean", "count"]
    )

The project also demonstrates `transform()`.

### Example

    self.data.groupby(group_column)[value_column].transform("mean")

A new `Group_Mean` column is added to the DataFrame.

---

# Data Visualization

The project provides multiple visualization options using **Matplotlib** and **Seaborn**.

## 1. Bar Plot

Used to compare values across different categories.

    plt.bar()

---

## 2. Line Plot

Used to show trends between variables.

    plt.plot()

---

## 3. Scatter Plot

Used to show the relationship between two numerical variables.

    plt.scatter()

---

## 4. Pie Chart

Used to display categorical distributions.

    plt.pie()

---

## 5. Histogram

Used to display the frequency distribution of numerical data.

    plt.hist()

---

## 6. Stack Plot

Used to display multiple numerical values together.

    plt.stackplot()

---

## 7. Subplots

Used to display multiple plots in a single figure.

    plt.subplots()

---

## 8. Seaborn Heatmap

Used to display a correlation matrix.

    sns.heatmap()

---

## 9. Seaborn Box Plot

Used to display the distribution of numerical data.

    sns.boxplot()

---

# Main Menu

The program provides the following options:

    ========== Main Menu ==========

    1. Load Dataset
    2. Explore Data
    3. Clean Data
    4. NumPy Array Operations
    5. Mathematical Operations
    6. Combine Data
    7. Split Data
    8. Search, Sort, or Filter Data
    9. Compute Aggregates
    10. Statistical Analysis
    11. Create Pivot Table
    12. GroupBy and Transform
    13. Data Visualization
    14. Save Data
    15. Exit

---

# Object-Oriented Programming

The project is implemented using a class named:

    class SalesDataAnalyzer:

The class contains separate methods for performing different data analysis operations.

## Constructor

The constructor initializes the dataset.

    def __init__(self, data=None):
        self.data = data

## Destructor

The project also demonstrates the destructor method.

    def __del__(self):
        pass

---

# Error Handling

The project uses `try-except` blocks to handle common errors such as:

- Invalid user input
- Invalid menu choices
- File not found
- Invalid column names
- File saving errors

### Example

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")

---

# Installation

Install the required Python libraries using:

    pip install pandas numpy matplotlib seaborn

---

# How to Run

## Step 1: Download or Clone the Repository

Download or clone the GitHub repository.

## Step 2: Check the Project Files

Make sure the following files are present:

    sales_data_analyzer.py
    sales_data.csv
    README.md
    requirements.txt

## Step 3: Install Required Libraries

    pip install pandas numpy matplotlib seaborn

## Step 4: Run the Program

    python sales_data_analyzer.py

## Step 5: Select an Option

Enter the number corresponding to the required operation from the main menu.

---

# Data Analysis Workflow

    Load Dataset
          ↓
    Explore Data
          ↓
    Clean Data
          ↓
    NumPy Array Operations
          ↓
    Mathematical Operations
          ↓
    Search / Sort / Filter
          ↓
    Aggregate Functions
          ↓
    Statistical Analysis
          ↓
    Pivot Table
          ↓
    GroupBy and Transform
          ↓
    Data Visualization
          ↓
    Save Data

---

# Important Note for GitHub

The CSV file should be loaded using a relative path:

    pd.read_csv("sales_data.csv")

Avoid using a computer-specific path such as:

    pd.read_csv("P:/Data Science/Jupyter Notebook 2/sales_data.csv")

Using a relative path allows the project to work correctly when the repository is downloaded or cloned on another computer.

---

# Learning Outcomes

Through this project, the following concepts are practiced:

- Python Programming
- Object-Oriented Programming
- Classes and Objects
- Constructor and Destructor
- Exception Handling
- Pandas DataFrames
- Data Cleaning
- Missing Value Handling
- Duplicate Removal
- NumPy Arrays
- Mathematical Operations
- DataFrame Concatenation
- Merge
- Join
- Data Splitting
- Searching
- Sorting
- Filtering
- Aggregate Functions
- Statistical Analysis
- Pivot Tables
- GroupBy
- Transform
- Matplotlib
- Seaborn
- CSV File Handling

---

# Conclusion

The **Pandas Analyzer & Data Visualization** project demonstrates a complete workflow for analyzing and visualizing sales data using Python.

The application combines data loading, cleaning, manipulation, statistical analysis, and visualization into a single menu-driven program using **Pandas, NumPy, Matplotlib, and Seaborn**.

---

# Author

**Pranjali Pandya**

**B.Tech Bioinformatics**

**Marwadi University**

---

*This project is developed for educational and academic purposes.*
