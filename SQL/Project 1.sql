-- Project 1
CREATE DATABASE DataDigger;
USE DataDigger;

-- Customer Table

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Address VARCHAR(200)
);

INSERT INTO Customers
(CustomerID, Name, Email, Address)
VALUES
(1, 'Alice', 'alice@gmail.com', 'Rajkot'),
(2, 'Bob', 'bob@gmail.com', 'Ahmedabad'),
(3, 'Charlie', 'charlie@gmail.com', 'Surat'),
(4, 'David', 'david@gmail.com', 'Vadodara'),
(5, 'Emma', 'emma@gmail.com', 'Jamnagar');

-- Order Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)
);

INSERT INTO Orders
(OrderID, CustomerID, OrderDate, TotalAmount)
VALUES
(101, 1, CURDATE() - INTERVAL 2 DAY, 3000.00),
(102, 2, CURDATE() - INTERVAL 5 DAY, 1500.00),
(103, 1, CURDATE() - INTERVAL 10 DAY, 2500.00),
(104, 3, CURDATE() - INTERVAL 40 DAY, 500.00),
(105, 4, CURDATE(), 4000.00);

-- Product Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2),
    Stock INT
);

INSERT INTO Products
(ProductID, ProductName, Price, Stock)
VALUES
(201, 'Headphones', 1500.00, 10),
(202, 'Keyboard', 800.00, 15),
(203, 'Mouse', 500.00, 0),
(204, 'Monitor', 12000.00, 5),
(205, 'Webcam', 2000.00, 8);

-- Order Details Table
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SubTotal DECIMAL(10,2),
    FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID)
);

INSERT INTO OrderDetails
(OrderDetailID, OrderID, ProductID, Quantity, SubTotal)
VALUES
(1, 101, 201, 2, 3000.00),
(2, 102, 202, 1, 800.00),
(3, 103, 201, 1, 1500.00),
(4, 104, 203, 1, 500.00),
(5, 105, 205, 2, 4000.00);

-- Customer
SELECT *FROM Customers;

update customers 
set address = 'Gandhinagar'
where customerid = 2;

SELECT * FROM Customers
WHERE CustomerID = 2;

delete from customers
where customerid = 5;

select *from customers where name = 'Alice';

-- Order table
select *from orders;
SELECT *
FROM Orders
WHERE CustomerID = 1;

-- Update an order's total amount
update orders
set totalamount = 5000
where orderid = 102;

DELETE FROM OrderDetails
WHERE OrderID = 104;

DELETE FROM Orders
WHERE OrderID = 104;

SELECT *
FROM Orders
WHERE OrderDate >= CURDATE() - INTERVAL 30 DAY;

SELECT
    MAX(TotalAmount) AS HighestAmount,
    MIN(TotalAmount) AS LowestAmount,
    AVG(TotalAmount) AS AverageAmount
FROM Orders;

-- Product Table
select *from products;

-- Display all products in descending order of price 
select *from products
order by price desc;

update products
set price = 1600.00
where productid = 201;

DELETE FROM OrderDetails
WHERE ProductID = 203;

DELETE FROM Products
WHERE Stock = 0;

select * from products;

SELECT *
FROM Products
WHERE Price BETWEEN 500 AND 2000;

SELECT *
FROM Products
WHERE Price = (SELECT MAX(Price) FROM Products)
   OR Price = (SELECT MIN(Price) FROM Products);
   
-- Order Details
SELECT *
FROM OrderDetails
WHERE OrderID = 101;

SELECT SUM(SubTotal) AS TotalRevenue
FROM OrderDetails;

select *from OrderDetails;

SELECT
    p.ProductID,
    p.ProductName,
    SUM(od.Quantity) AS TotalQuantityOrdered
FROM OrderDetails od
JOIN Products p
    ON od.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY TotalQuantityOrdered DESC, p.ProductID
LIMIT 3;

SELECT COUNT(*) AS NumberOfSales
FROM OrderDetails
WHERE ProductID = 201;
