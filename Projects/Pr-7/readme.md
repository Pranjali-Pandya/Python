# 📦 Multi-Utility Tool in Python

A menu-driven Python application that combines multiple utilities into a single program using Python's built-in modules. The project demonstrates modular programming, package creation, object-oriented programming, exception handling, file handling, and the use of several standard Python libraries.

---

# 📖 Project Overview

The **Multi-Utility Tool** is a console-based application developed in Python. It provides multiple useful utilities through an interactive menu system. Each utility is implemented as a separate module inside a custom package named **Datetime_package**, making the project modular, reusable, and easy to maintain.

---

# ✨ Features

The application provides the following utilities:

## 🕒 1. Date and Time Operations

Uses Python's `datetime` and `time` modules.

### Functionalities

- Display current date and time
- Display year, month, day, hour, minute and second
- Calculate difference between two dates
- Calculate difference between two times
- Display date in different formats
- Stopwatch
- Countdown timer (minutes or seconds)

---

## 🧮 2. Mathematical Operations

Uses Python's `math` module.

### Functionalities

- Trigonometric calculations
  - Sine
  - Cosine
  - Tangent
  - Inverse Sine
  - Inverse Cosine
  - Inverse Tangent
- Factorial calculation
- Logarithmic calculations
  - Natural Log
  - Base-10 Log
  - Custom Base Log
- Compound Interest Calculator
- Area of Circle Calculator

---

## 🎲 3. Random Data Generation

Uses Python's `random` module.

### Functionalities

- Generate random floating-point numbers
- Generate random integers
- Generate random odd numbers
- Generate random numbers within a specified range
- Generate a random list
- Generate a random secure password

---

## 🆔 4. UUID Generator

Uses Python's `uuid` module.

### Functionality

- Generate a unique UUID (Version 4)

---

## 📁 5. Personal Journal Manager

A file handling application developed using Object-Oriented Programming.

### Functionalities

- Create a journal file
- Add journal entries
- View all journal entries
- Search journal entries using:
  - Date
  - Time
  - Keyword
- Delete all journal entries

### Concepts Used

- File Handling
- Exception Handling
- Classes and Objects
- Custom Exceptions

---

## 🔍 6. Explore Module Attributes

Uses Python's built-in `dir()` function.

### Functionality

- Display all available attributes and functions of the `math` module.

---

# 📂 Project Structure

```
Multi-Utility-Tool/
│
├── main.py
│
├── Datetime_package/
│   ├── __init__.py
│   ├── date_time_utils.py
│   ├── mathmodule.py
│   ├── randomdata.py
│   ├── uuid_module.py
│   ├── file_module.py
│   └── explore_module_attributes.py
│
├── journal.txt          (Created automatically)
└── README.md
```

---

# 🛠 Technologies Used

- Python 3.x
- datetime module
- time module
- math module
- random module
- uuid module
- File Handling
- Object-Oriented Programming (OOP)
- Exception Handling

---

# ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/Multi-Utility-Tool.git
```

### Move into the project folder

```bash
cd Multi-Utility-Tool
```

### Run the application

```bash
python main.py
```

---

# 📋 Main Menu

```
==================================================
Welcome To Multi-Utility Tool
==================================================

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifier (UUID)
5. File Operations (Journal Manager)
6. Explore Module Attributes
7. Exit
```

---

# 💡 Concepts Demonstrated

- Python Packages
- Modular Programming
- Functions
- Loops
- Conditional Statements
- File Handling
- Exception Handling
- Custom Exceptions
- Classes and Objects
- Standard Library Modules
- User Input Validation

---

# 📌 Future Improvements

- Add a graphical user interface (GUI)
- Save user settings
- Add scientific calculator features
- Export journal entries to PDF
- Password-protect journal entries
- Improve input validation
- Add unit testing

---

# 👩‍💻 Author

**Pranjali Pandya**

Python Mini Project

---

# 📜 License

This project is created for educational and learning purposes.
