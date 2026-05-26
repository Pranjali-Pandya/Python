# Personal Data Collector 🧾

A simple Python program that collects personal information from the user and displays:

- Name
- Age
- Height
- Favorite Number
- Data Types
- Memory Addresses
- Approximate Birth Year

Good beginner project for learning:

- `input()`
- Type casting
- Variables
- `type()`
- `id()`
- Basic printing in Python

---

## 📌 Features

- Interactive user input
- Integer and float conversion
- Displays variable data types
- Shows memory addresses using `id()`
- Calculates approximate birth year

---

## 🖥️ Example Output

```bash
Welocome to Interactive personal Data Collector

Enter your name: John
Enter your age: 20
Enter your height: 5.9
Enter your favorite number: 7

Thankyou! Here is the information we collected

Name John (Type: <class 'str'> , Memory Address : 140234567890)

Age 20 (Type: <class 'int'> , Memory Address : 140234567891)

Height 5.9 (Type: <class 'float'> , Memory Address : 140234567892)

Favorite Number 7 (Type: <class 'int'> , Memory Address : 140234567893)

Your Birth year is approximately 2006 (based on your age of 20)

Thankyou! for using Personal Data Collector
```

---

## 🚀 How to Run

### 1. Install Python

Download Python from the official website:

https://www.python.org

### 2. Clone Repository

```bash
git clone https://github.com/your-username/personal-data-collector.git
```

### 3. Run the Program

```bash
python main.py
```

---

## 📂 Project Structure

```bash
personal-data-collector/
│
├── main.py
└── README.md
```

---

## ⚠️ Bug Fix

Replace this line:

```python
print("Your Birth year is approximately ",i," f(based on your age of {age} ")
```

With this:

```python
print(f"Your Birth year is approximately {i} (based on your age of {age})")
```

Better version:

```python
birth_year = 2026 - age
print(f"Your Birth year is approximately {birth_year} (based on your age of {age})")
```

---

## 🧠 Concepts Used

- Variables
- User Input
- Type Conversion
- String Formatting
- Python Functions
- Memory Management Basics

---

## 📜 License

This project is open-source and free to use.