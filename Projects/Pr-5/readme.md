# Employee Management System (Python OOP)

## Project Description
This is a console-based Employee Management System developed using Python.  
It uses Object-Oriented Programming concepts to manage Employees, Managers, and Developers with full CRUD operations.

---

## Features
- Add Employee, Manager, Developer
- View all records
- Update existing records
- Delete records
- Prevent duplicate IDs
- Check subclass relationship using `issubclass()`
- Encapsulation using private attributes
- Menu-driven interface

---

## OOP Concepts Used
- Classes and Objects
- Inheritance
- Method Overriding
- Encapsulation (private variables `__empid`, `__salary`)
- Constructors (`__init__`)
- Destructor (`__del__`)
- List of objects

---

## Class Structure

### Employee (Base Class)
Attributes:
- empid (private)
- name
- age
- salary (private)

Methods:
- set_info()
- get_info()
- set_salary()
- get_salary()
- display()

---

### Manager (Child Class of Employee)
Additional Attribute:
- department

Methods:
- display() (overridden)

---

### Developer (Child Class of Employee)
Additional Attribute:
- prog_lang

Methods:
- display() (overridden)

---

## Menu Options

1. Add Employee / Manager / Developer  
2. View Employee / Manager / Developer  
3. Update Employee / Manager / Developer  
4. Delete Employee / Manager / Developer  
5. Check Subclass Relationship  
6. Exit  

---

## How to Run the Project

```bash
python filename.py

Project Logic
Each category stored in separate lists:
emp[]
man[]
dev[]
Duplicate ID check before insertion
Update and delete performed using ID search
Uses issubclass() to verify inheritance

Author
Pranjali Pandya
