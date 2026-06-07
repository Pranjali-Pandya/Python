# 🎓 Student Data Organizer

A menu-driven Python application that helps users manage student records efficiently. This project demonstrates the practical use of Python data structures such as Lists, Dictionaries, Sets, and Tuples while performing CRUD (Create, Read, Update, Delete) operations.

---

## 📌 Project Overview

The Student Data Organizer allows users to:

- Add new student records
- Display all students
- Update student information
- Delete student records
- Display all unique subjects offered
- Exit the application safely

The project is designed to strengthen understanding of Python fundamentals and data handling techniques.

---

## ✨ Features

### ➕ Add Student
- Add a new student with:
  - Student ID
  - Name
  - Age
  - Date of Birth
  - Grade
  - Subjects
- Prevents duplicate Student IDs
- Validates Date of Birth format (`DD-MM-YYYY`)

### 📋 Display All Students
- Displays all stored student records
- Shows subjects in a readable format

### ✏️ Update Student Information
Users can update:
- Student Name
- Age
- Grade
- Subjects

### ❌ Delete Student
- Delete a student record using Student ID

### 📚 Display Subjects Offered
- Displays all unique subjects offered by students

### 🚪 Exit Program
- Terminates the application gracefully

---

## 🖥️ Menu Interface

```text
**************** Welcome to Student Data Organizer ********************

1. Add student
2. Display all students
3. Update Student Information
4. Delete Student
5. Display Subject Offered
6. Exit
```

---

## 📖 Sample Student Record

```python
{
    "ID": 101,
    "Name": "Riya",
    "Age": 20,
    "Date Of Birth": "12-05-2004",
    "Grade": "A",
    "Subject": {"Math", "Physics", "Chemistry"}
}
```

---

## 📂 Project Structure

```text
Projects/
└── Pr-3/
    ├── project3.py
    └── README.md
```

---

## 🚀 How to Run

### Step 1: Install Python

Download Python from:

https://www.python.org

### Step 2: Run the Program

Open a terminal in the project folder and execute:

```bash
python project3.py
```

---

## 🧠 Concepts Used

- Python Lists
- Dictionaries
- Sets
- Tuples
- Loops
- Conditional Statements
- Input Validation
- String Manipulation
- CRUD Operations

---

## 🔄 Program Workflow

1. User selects an option from the menu.
2. Student details are stored in a list of dictionaries.
3. Duplicate Student IDs are checked before insertion.
4. Subjects are stored using sets to avoid duplicates.
5. Records can be viewed, updated, or deleted.
6. Unique subjects are collected and displayed.

---

## ⚠️ Limitations

- Data is stored temporarily in memory.
- Data is lost when the program closes.
- Date validation checks only the format, not actual calendar validity.

---

## 🚀 Future Improvements

- Function-based modular structure
- File handling for permanent data storage
- Student search functionality
- Sorting student records
- Database integration (MySQL/SQLite)
- Graphical User Interface (GUI)
- Advanced date validation using the `datetime` module

---

## 📚 Learning Outcomes

Through this project, the following concepts are practiced:

- Data Structures in Python
- CRUD Operations
- User Input Handling
- Data Validation
- Problem Solving
- Menu-Driven Programming

---

## 👨‍💻 Author

**Pranjali Pandya**

Python Mini Project – Student Data Organizer

---

## 📜 License

This project is developed for educational and learning purposes.
