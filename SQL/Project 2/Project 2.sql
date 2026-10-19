-- Project 2
CREATE DATABASE DataTransformer;
USE DataTransformer;

-- 1. Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    RegistrationDate DATE
);

-- 2. Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- 3. Employees Table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    HireDate DATE,
    Salary DECIMAL(10,2)
);

-- Customers
INSERT INTO Customers VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '2022-03-15'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '2021-11-02'),
(3, 'David', 'Brown', 'david.brown@email.com', '2023-01-10'),
(4, 'Priya', 'Patel', '  priya.patel@email.com  ', '2024-05-20');

-- Orders
INSERT INTO Orders VALUES
(101, 1, '2023-07-01', 150.50),
(102, 2, '2023-07-03', 200.75),
(103, 1, '2023-07-05', 650.00),
(104, 3, '2023-08-10', 1200.00);

-- Employees
INSERT INTO Employees VALUES
(1, 'Mark', 'Johnson', 'Sales', '2020-01-15', 50000.00),
(2, 'Susan', 'Lee', 'HR', '2021-03-20', 55000.00),
(3, 'Rahul', 'Shah', 'IT', '2019-06-10', 80000.00),
(4, 'Neha', 'Patel', 'Sales', '2022-09-01', 35000.00); 	

select * from Customers;
select * from Orders;
select * from Employees;

-- Retrieve orders with their matching customer details.
SELECT c.CustomerID, c.FirstName, c.LastName,
       o.OrderID, o.OrderDate, o.TotalAmount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID;

SELECT c.CustomerID, c.FirstName, c.LastName,
       o.OrderID, o.OrderDate, o.TotalAmount
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID;

-- Retrieve all orders and their corresponding customers.
SELECT c.CustomerID, c.FirstName, c.LastName,
       o.OrderID, o.OrderDate, o.TotalAmount
FROM Customers c
RIGHT JOIN Orders o
ON c.CustomerID = o.CustomerID;


-- Full Outer Join
SELECT c.CustomerID, c.FirstName, c.LastName,
       o.OrderID, o.OrderDate, o.TotalAmount
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID

UNION

SELECT c.CustomerID, c.FirstName, c.LastName,
       o.OrderID, o.OrderDate, o.TotalAmount
FROM Customers c
RIGHT JOIN Orders o
ON c.CustomerID = o.CustomerID;

-- Subquery: Customers with orders above the average order amount
SELECT DISTINCT c.CustomerID, c.FirstName, c.LastName
FROM Customers c
JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE o.TotalAmount > (
    SELECT AVG(TotalAmount)
    FROM Orders
);

-- Subquery: Employees with above-average salaries
SELECT EmployeeID, FirstName, LastName,
       Department, Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);

-- Extract the year and month from OrderDate
SELECT OrderID, OrderDate,
       YEAR(OrderDate) AS OrderYear,
       MONTH(OrderDate) AS OrderMonth
FROM Orders;

-- Calculate the difference in days between OrderDate and today
SELECT OrderID, OrderDate,
       CURDATE() AS CurrentDate,
       DATEDIFF(CURDATE(), OrderDate) AS DaysDifference
FROM Orders;

-- Format OrderDate as DD-MMM-YYYY
SELECT OrderID, OrderDate,
       DATE_FORMAT(OrderDate, '%d-%b-%Y') AS FormattedDate
FROM Orders;

-- Concatenate FirstName and LastName
SELECT EmployeeID,
       CONCAT(FirstName, ' ', LastName) AS FullName
FROM Employees;

-- Replace John with Jonathan
select * from Customers;
SELECT CustomerID, FirstName,
       REPLACE(FirstName, 'John', 'Jonathan') AS UpdatedFirstName
FROM Customers;

-- Convert FirstName to uppercase and LastName to lowercase
SELECT EmployeeID,
       UPPER(FirstName) AS UpperFirstName,
       LOWER(LastName) AS LowerLastName
FROM Employees;

-- Trim extra spaces from Emai
SELECT CustomerID, Email,
       TRIM(Email) AS CleanEmail
FROM Customers;

-- Calculate the running total of TotalAmount
SELECT OrderID, OrderDate, TotalAmount,
       SUM(TotalAmount) OVER (
           ORDER BY OrderDate, OrderID
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS RunningTotal
FROM Orders;

-- Rank orders by TotalAmount using RANK()
SELECT OrderID, TotalAmount,
       RANK() OVER (
           ORDER BY TotalAmount DESC
       ) AS OrderRank
FROM Orders;

-- Assign discounts based on TotalAmount
SELECT OrderID, TotalAmount,
       CASE
           WHEN TotalAmount > 1000 THEN '10% Discount'
           WHEN TotalAmount > 500 THEN '5% Discount'
           ELSE 'No Discount'
       END AS Discount
FROM Orders;

-- Categorize employees' salaries as High, Medium, or Low
SELECT EmployeeID, FirstName, LastName, Salary,
       CASE
           WHEN Salary > 60000 THEN 'High'
           WHEN Salary > 40000 THEN 'Medium'
           ELSE 'Low'
       END AS SalaryCategory
FROM Employees;
