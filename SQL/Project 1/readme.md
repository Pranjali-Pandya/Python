# DataDigger – SQL Database Management Project

## 📌 Project Overview

**DataDigger** is a SQL-based database management project developed using MySQL. It manages customer information, orders, products, and order details. The project demonstrates basic to intermediate SQL operations used to store, retrieve, update, and delete data efficiently.

It also uses aggregate functions, joins, subqueries, sorting, filtering, and grouping to analyze order and product information.

## 🎯 Objectives

- Create and manage a relational database using MySQL.
- Store customer details and product information.
- Manage customer orders and order details.
- Perform CRUD operations (Create, Read, Update, and Delete).
- Retrieve data using filtering and sorting.
- Calculate sales statistics using aggregate functions.
- Analyze product sales and quantities ordered.
- Understand primary keys and foreign key relationships.

## 🛠️ Technologies Used

- **Database:** MySQL
- **Language:** SQL
- **Tool:** MySQL Workbench or MySQL Command Line Client

## 🗂️ Database Structure

The project contains four tables:

### 1. Customers

Stores information about customers.

| Column | Data Type | Description |
|---|---|---|
| CustomerID | INT | Primary key |
| Name | VARCHAR(100) | Customer name |
| Email | VARCHAR(100) | Unique email address |
| Address | VARCHAR(200) | Customer address |

### 2. Orders

Stores customer order information.

| Column | Data Type | Description |
|---|---|---|
| OrderID | INT | Primary key |
| CustomerID | INT | Foreign key referencing Customers |
| OrderDate | DATE | Date of the order |
| TotalAmount | DECIMAL(10,2) | Total order amount |

### 3. Products

Stores product information and inventory details.

| Column | Data Type | Description |
|---|---|---|
| ProductID | INT | Primary key |
| ProductName | VARCHAR(100) | Name of the product |
| Price | DECIMAL(10,2) | Product price |
| Stock | INT | Available stock quantity |

### 4. OrderDetails

Stores the products and quantities associated with orders.

| Column | Data Type | Description |
|---|---|---|
| OrderDetailID | INT | Primary key |
| OrderID | INT | Foreign key referencing Orders |
| ProductID | INT | Foreign key referencing Products |
| Quantity | INT | Quantity ordered |
| SubTotal | DECIMAL(10,2) | Subtotal for the order detail |

## 🔗 Database Relationships

- One customer can place multiple orders.
- Each order is associated with a customer through `CustomerID`.
- An order can contain multiple order details.
- Each order detail references a product through `ProductID`.
- Foreign keys maintain referential integrity between related tables.

## ⚙️ SQL Operations Implemented

### 1. Database Creation
- Create the `DataDigger` database.
- Select the database using the `USE` statement.
- Create four relational tables.

### 2. Data Insertion
- Insert sample customer records.
- Insert order records with dynamically calculated dates.
- Insert product and order-detail records.

### 3. CRUD Operations
- **Create:** Create tables and insert records.
- **Read:** Retrieve records using `SELECT`.
- **Update:** Modify customer addresses, order amounts, and product prices.
- **Delete:** Remove selected customers, order details, orders, and products.

### 4. Filtering and Sorting
- Retrieve customer details using `WHERE`.
- Find orders belonging to a particular customer.
- Retrieve orders placed within the last 30 days.
- Filter product prices using `BETWEEN`.
- Display products in descending order of price.

### 5. Aggregate Functions
The project uses:
- `MAX()` – Finds the highest order amount.
- `MIN()` – Finds the lowest order amount.
- `AVG()` – Calculates the average order amount.
- `SUM()` – Calculates total revenue from order details.
- `COUNT()` – Counts sales records for a particular product.

### 6. Joins and Grouping
- Join `OrderDetails` with `Products`.
- Calculate the total quantity ordered for each product.
- Group records using `GROUP BY`.
- Sort results using `ORDER BY`.
- Display the top three products by total quantity ordered using `LIMIT`.

### 7. Subqueries
- Identify the product with the highest price.
- Identify the product with the lowest price.
- Retrieve products matching either price.

## ▶️ How to Run the Project

1. Install MySQL Server and MySQL Workbench, or use the MySQL command-line client.
2. Open your SQL editor.
3. Copy the project SQL code into a new query window.
4. Execute the database creation and table creation statements.
5. Execute the `INSERT` statements to add sample data.
6. Run the remaining SQL queries individually to explore the database and perform the analyses.

**Note:** Run the complete script on a fresh database. Some deletion queries depend on foreign key relationships, so the order of deletion matters.

## 📊 Key Learning Outcomes

- Understanding relational database design.
- Working with primary and foreign keys.
- Performing CRUD operations in SQL.
- Using aggregate functions for data analysis.
- Applying joins, subqueries, and grouping.
- Filtering and sorting database records.
- Understanding referential integrity and deletion dependencies.
- Analyzing product sales and order information.

## 🚀 Future Improvements

- Add a Payments table to manage transactions.
- Add product categories and supplier information.
- Create views for frequently used sales reports.
- Add stored procedures for common database operations.
- Generate monthly sales and customer purchase reports.
- Add constraints to validate prices, stock, and quantities.

## 👩‍💻 Author

**Pranjali Pandya**

Bioinformatics Student | SQL and Data Analysis Learner

## 📄 License

This project is intended for educational and learning purposes.
