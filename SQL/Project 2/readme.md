[README.md](https://github.com/user-attachments/files/33662184/README.md)
# DataTransformer – SQL Database Management and Data Analysis Project

## Project Overview

**DataTransformer** is a MySQL project that demonstrates relational database creation, table relationships, joins, subqueries, date and string functions, window functions, and conditional logic. It uses sample customer, order, and employee data to practise data retrieval and transformation.

## Objectives

- Create a database and related tables using MySQL.
- Insert and retrieve customer, order, and employee records.
- Combine related data using `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and a `UNION`-based full outer join.
- Use subqueries to identify customers with above-average orders and employees with above-average salaries.
- Apply date and string functions to format and transform data.
- Use window functions to calculate running totals and rank orders.
- Use `CASE` expressions to categorize discounts and salary levels.

## Technologies Used

- **Database:** MySQL
- **Language:** SQL
- **Suggested tools:** MySQL Workbench or MySQL command-line client

## Database Structure

The project contains three tables.

### 1. Customers

Stores customer details.

| Column | Data Type | Description |
|---|---|---|
| `CustomerID` | INT | Primary key |
| `FirstName` | VARCHAR(50) | Customer first name |
| `LastName` | VARCHAR(50) | Customer last name |
| `Email` | VARCHAR(100) | Email address |
| `RegistrationDate` | DATE | Registration date |

### 2. Orders

Stores customer order information.

| Column | Data Type | Description |
|---|---|---|
| `OrderID` | INT | Primary key |
| `CustomerID` | INT | Foreign key referencing `Customers(CustomerID)` |
| `OrderDate` | DATE | Order date |
| `TotalAmount` | DECIMAL(10,2) | Total order amount |

### 3. Employees

Stores employee information.

| Column | Data Type | Description |
|---|---|---|
| `EmployeeID` | INT | Primary key |
| `FirstName` | VARCHAR(50) | Employee first name |
| `LastName` | VARCHAR(50) | Employee last name |
| `Department` | VARCHAR(50) | Department |
| `HireDate` | DATE | Hire date |
| `Salary` | DECIMAL(10,2) | Salary |

## SQL Concepts Demonstrated

### 1. Database and Table Creation
Creates the `DataTransformer` database and the `Customers`, `Orders`, and `Employees` tables. A foreign key connects orders to their customers.

### 2. Sample Data and Retrieval
Inserts sample records into all three tables and retrieves records using `SELECT`.

### 3. Joins
- `INNER JOIN`: Returns matching customer and order records.
- `LEFT JOIN`: Returns all customers and any matching orders.
- `RIGHT JOIN`: Returns all orders and their matching customers.
- `UNION` of left and right joins: Demonstrates a full outer join pattern in MySQL.

### 4. Subqueries
- Finds customers whose order amounts are above the average order amount.
- Finds employees whose salaries are above the average salary.

### 5. Date Functions
Uses `YEAR()`, `MONTH()`, `CURDATE()`, `DATEDIFF()`, and `DATE_FORMAT()` to extract, compare, and format dates.

### 6. String Functions
Uses `CONCAT()`, `REPLACE()`, `UPPER()`, `LOWER()`, and `TRIM()` to combine names, replace text, change letter case, and remove extra spaces from email values.

### 7. Window Functions
- `SUM() OVER()` calculates a running total of order amounts.
- `RANK() OVER()` ranks orders by total amount.

### 8. Conditional Logic
Uses `CASE` expressions to assign discounts based on order amounts and categorize employee salaries as High, Medium, or Low.

## How to Run the Project

1. Install MySQL Server and open MySQL Workbench or a MySQL command-line client.
2. Open the supplied `Project 2.sql` script.
3. Execute the script on a MySQL server with permission to create databases.
4. Review the `SELECT` queries and run individual sections to inspect the results.

**Note:** The script uses MySQL-specific functions and syntax. MySQL does not directly support `FULL OUTER JOIN`, so the project demonstrates this pattern using `UNION` with left and right joins.

## Learning Outcomes

- Understand primary keys, foreign keys, and relational database design.
- Combine tables and analyze related records.
- Use subqueries and aggregate functions for comparisons.
- Transform dates and text using SQL functions.
- Apply window functions for running totals and ranking.
- Use conditional expressions to create data categories.

## Future Improvements

- Add constraints such as `NOT NULL`, `UNIQUE`, and `CHECK` where appropriate.
- Add more sample data to test edge cases.
- Create views for reusable customer and sales reports.
- Add indexes to columns frequently used in joins or filters.
- Extend the project with monthly sales summaries and department-level salary analysis.

## Author

**Pranjali Pandya**  
Bioinformatics Student | SQL and Data Analysis Learner

## License

This project is intended for educational and learning purposes.
