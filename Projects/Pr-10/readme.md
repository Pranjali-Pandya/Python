[README (1).md](https://github.com/user-attachments/files/32511941/README.1.md)
# Titanic Dataset Analysis

## Project Overview

This project performs **data loading, data cleaning, feature engineering, statistical analysis, and data visualization** on the Titanic dataset using Python.

The analysis is implemented in a Jupyter Notebook and uses **Pandas, NumPy, Matplotlib, and Seaborn**.

## Objectives

- Load the Titanic CSV dataset.
- Explore the structure and contents of the dataset.
- Identify and handle missing values.
- Create new useful features from existing columns.
- Perform statistical analysis.
- Analyze passenger survival.
- Compare survival with gender, passenger class, and age.
- Create visualizations to understand the dataset.

## Technologies Used

- **Python**
- **Jupyter Notebook**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

## Dataset

The project uses the **Titanic Dataset** (`Titanic-Dataset.csv`).

Important columns used in the analysis include:

| Column | Description |
|---|---|
| `PassengerId` | Unique passenger identifier |
| `Survived` | Survival status (0 = Did Not Survive, 1 = Survived) |
| `Pclass` | Passenger class |
| `Name` | Passenger name |
| `Sex` | Passenger gender |
| `Age` | Passenger age |
| `SibSp` | Number of siblings/spouses aboard |
| `Parch` | Number of parents/children aboard |
| `Fare` | Passenger fare |
| `Cabin` | Cabin information |
| `Embarked` | Port of embarkation |

## Project Workflow

### 1. Import Libraries

The project imports:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### 2. Load the Dataset

The Titanic CSV file is loaded using Pandas:

```python
df = pd.read_csv("Titanic-Dataset.csv")
```

The notebook then displays the first and last five rows.

### 3. Dataset Exploration

The notebook examines:

- Number of rows
- Number of columns
- Column names
- Dataset information and data types
- Statistical summary using `describe()`

### 4. Missing Value Analysis and Cleaning

Missing values are identified using:

```python
df.isnull().sum()
```

The percentage of missing values is also calculated.

The following cleaning operations are performed:

- Missing `Age` values are replaced with the **median age**.
- Missing `Embarked` values are replaced with the **mode**.
- A new `CabinKnown` column is created to indicate whether cabin information is available.

```python
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

embarked_mode = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(embarked_mode)

df["CabinKnown"] = df["Cabin"].notnull().astype(int)
```

### 5. Feature Engineering

New features are created from the existing data.

#### FamilySize

```python
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
```

This represents the total family size of a passenger aboard the Titanic.

#### IsAlone

```python
df["IsAlone"] = np.where(df["FamilySize"] == 1, 1, 0)
```

This identifies passengers travelling alone.

#### AgeGroup

Passengers are divided into age groups:

- Child
- Teenager
- Young Adult
- Adult
- Senior

```python
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"]
)
```

#### FamilyCategory

Family size is categorized as:

- Alone
- Small Family
- Large Family

A custom function is used to create this feature.

## Statistical Analysis

The notebook performs analysis of:

- Survival count
- Survival percentage
- Passenger count by gender
- Passenger count by class
- Survival rate by passenger class
- Age statistics
- Survival rate by age group
- Fare statistics

### Survival Analysis

The survival column is analyzed using:

```python
df["Survived"].value_counts()
```

and:

```python
df["Survived"].value_counts(normalize=True) * 100
```

### Survival by Passenger Class

The survival rate for each passenger class is calculated using:

```python
class_survival = df.groupby("Pclass")["Survived"].mean() * 100
```

## Data Visualizations

The project creates several visualizations using Matplotlib and Seaborn.

### Visualizations Included

1. Titanic Survival Count
2. Titanic Survival Percentage
3. Passenger Distribution by Gender
4. Survival by Gender
5. Passenger Distribution by Class
6. Survival by Passenger Class
7. Survival Rate by Passenger Class
8. Age vs Fare Scatter Plot
9. Age Distribution by Survival Status
10. Passenger Survival Distribution
11. Survival Rate by Gender

These visualizations help identify patterns and relationships in the Titanic dataset.

## Key Analysis Areas

The notebook mainly investigates:

- How many passengers survived?
- What percentage of passengers survived?
- How passengers were distributed by gender.
- How survival varied by gender.
- How passengers were distributed among passenger classes.
- How survival varied by passenger class.
- How age was distributed among passengers.
- How survival varied across age groups.
- The relationship between passenger age and fare.

## Project Structure

```text
Titanic-Data-Analysis/
│
├── Titanic-Dataset.csv
├── Titanic_Analysis.ipynb
└── README.md
```

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install Required Libraries

Run:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Step 3: Open Jupyter Notebook

Run:

```bash
jupyter notebook
```

### Step 4: Open the Notebook

Open the project notebook and run the cells from top to bottom.

### Step 5: Keep the Dataset in the Correct Location

Make sure `Titanic-Dataset.csv` is available in the location used by the notebook.

If the CSV file is in the same folder as the notebook, use:

```python
df = pd.read_csv("Titanic-Dataset.csv")
```

## Conclusion

This project demonstrates a complete basic data analysis workflow using the Titanic dataset. It covers **data loading, exploration, cleaning, feature engineering, statistical analysis, and visualization** using Python's popular data analysis libraries.

The project is suitable for practicing practical **Pandas, NumPy, Matplotlib, and Seaborn** concepts in a Jupyter Notebook.
