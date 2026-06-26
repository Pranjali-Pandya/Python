# 🛒 E-Commerce Order System using Python UUID

A simple command-line based E-Commerce Order Management System developed in Python. This project demonstrates the use of Python's built-in `uuid` module to generate unique Order IDs for every product ordered.

---

## 📌 Features

* Place a new order
* Generate a unique Order ID using the `uuid` module
* View all placed orders
* Store orders using a Python dictionary
* Simple menu-driven interface

---

## 🛠️ Technologies Used

* Python 3
* UUID Module

---

## 📂 Project Structure

```
ecommerce-order-system-python/
│
├── main.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/ecommerce-order-system-python.git
```

2. Navigate to the project folder.

```bash
cd ecommerce-order-system-python
```

3. Run the program.

```bash
python main.py
```

---

## 📖 How It Works

When the program starts, a menu is displayed.

```
1. To Place Order
2. To View Orders
3. To Exit
```

### Place Order

* Enter the product name.
* The program generates a unique Order ID using `uuid.uuid4()`.
* The order is stored in a dictionary.

### View Orders

Displays all previously placed orders along with their unique Order IDs.

### Exit

Terminates the program.

---

## 💻 Sample Output

```
1. To Place Order
2. To View Orders
3. To Exit

Enter your choice: 1

Enter the product name: Laptop

Order Placed Successfully!

Product Name : Laptop
Order ID     : 7f4b7c8d-a5b2-4d81-9d89-c4c4e6d8e45f
```

---

## 📚 Concepts Used

* Python Dictionary
* While Loop
* Conditional Statements (`if`, `elif`, `else`)
* UUID Module
* User Input
* Menu-Driven Programming

---

## 🎯 Learning Outcome

This project helps in understanding:

* How to generate universally unique identifiers (UUIDs)
* How to store and retrieve data using dictionaries
* Building menu-driven console applications
* Basic CRUD-style operations in Python

---

## 👩‍💻 Author

**Pranjali Pandya**

B.Tech Bioinformatics Student

Learning Python, Data Analytics, and Software Development.
