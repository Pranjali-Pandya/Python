# Student Data Organizer 🎓

A beginner-friendly Python project that allows users to manage student records through a simple menu-driven interface.

---

## 📋 Features

### Student Management
Perform full CRUD operations on student records:

1. Add a new student
2. Display all students
3. Update student information
4. Delete a student
5. Display all subjects offered
6. Exit

### Data Stored Per Student
- **ID** – Unique student identifier (stored as part of a tuple)
- **Name** – Full name of the student
- **Age** – Student's age
- **Date of Birth** – In `DD-MM-YYYY` format (validated)
- **Grade** – Current grade/class
- **Subjects** – Set of subjects (entered as comma-separated values)

---

## 💻 Example Menu

```
**************** Welcome to Student Data Organizer ********************

1. Add student
2. Display all students
3. Update Student Information
4. Delete Student
5. Display Subject Offered
6. Exit
Enter your choice :
```

---

## 📦 Example Record

```
Id 101 | Name Alice | Age 17 | Date Of Birth 12-05-2007 | Grade 11 | Subject Math,Science,English
```

---

## 🚀 How to Run

### 1. Install Python
Download Python from:
https://www.python.org

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/student-data-organizer.git
```

### 3. Run the Program

```bash
python main.py
```

---

## 📁 Project Structure

```
student-data-organizer/
├── main.py
└── README.md
```

---

## 🧠 Concepts Used

- `while` loops
- `for` loops
- Lists and dictionaries
- Tuples and sets
- Conditional statements (`if`, `elif`, `else`)
- String methods (`.split()`, `.join()`)
- User input handling
- Basic input validation (date format check)

---

## ⚠️ Improvements You Should Make

### 1. Avoid Using `id` as a Variable Name

`id` is a built-in Python function. Using it as a variable name shadows the built-in.

**Current:**
```python
id = int(input("Enter student id: "))
```

**Better:**
```python
student_id = int(input("Enter student id: "))
```

---

### 2. Fix Misleading Comment

The comment on the `split()` call is incorrect — it does the opposite of what is described.

**Current:**
```python
subject2 = subject.split(",")  # converts list to string
```

**Correct:**
```python
subject2 = subject.split(",")  # converts string to list
```

---

### 3. Fix Typo in Grade Update (Choice 3)

In the update section, `g = a = input(...)` is used by mistake. The variable `a` is reassigned unnecessarily.

**Current:**
```python
g = a = input("Enter the grade ")
```

**Better:**
```python
g = input("Enter the grade ")
```

---

### 4. Add Input Validation for Age and ID

Wrap integer inputs in `try-except` to handle non-numeric input gracefully.

**Better:**
```python
try:
    student_id = int(input("Enter student id: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    continue
```

---

## 📄 License

This project is open-source and free to use.
