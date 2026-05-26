# Pattern Generator and Number Analyzer 🔢

A beginner-friendly Python project that allows users to:

- Generate different number patterns
- Analyze numbers in a range
- Check odd/even numbers
- Calculate the sum of numbers in a range

This project helps practice:

- Loops
- Nested loops
- Match-case statements
- Conditions
- User input handling
- Pattern printing

---

## 📌 Features

### Pattern Generator
Generate different patterns:

1. Right-angled triangle
2. Inverted right-angled triangle
3. Same number triangle
4. Reverse incrementing number triangle

### Number Analyzer
- Detects odd and even numbers
- Calculates total sum in a range

---

## 🖥️ Example Menu

```bash
Welcome to the Pattern Generator and Number Analyzer

Select an option from below
1. To Generate a Pattern
2. To analyze a Range of Numbers
3. To Exit
```

---

## 📖 Example Patterns

### Right-Angled Triangle

```bash
1
12
123
1234
```

### Inverted Right-Angled Triangle

```bash
1234
123
12
1
```

### Same Number Triangle

```bash
1
22
333
4444
```

### Reverse Incrementing Number Triangle

```bash
54321
5432
543
54
5
```

---

## 🚀 How to Run

### 1. Install Python

Download Python from:

https://www.python.org

### 2. Clone Repository

```bash
git clone https://github.com/your-username/pattern-generator-number-analyzer.git
```

### 3. Run the Program

```bash
python main.py
```

---

## 📂 Project Structure

```bash
pattern-generator-number-analyzer/
│
├── main.py
└── README.md
```

---

## 🧠 Concepts Used

- `while` loops
- `for` loops
- Nested loops
- `match-case`
- Conditional statements
- Range handling
- Pattern printing
- User input

---

## ⚠️ Improvements You Should Make

### 1. Typo Fixes

Current:

```python
print("Welcome to the Pattern Generator and Nimber Analyzer")
```

Correct:

```python
print("Welcome to the Pattern Generator and Number Analyzer")
```

---

### 2. Avoid Using `sum` as Variable Name

You used:

```python
sum = 0
```

`sum` is already a built-in Python function.

Better:

```python
total = 0
```

---

### 3. Reverse Pattern Logic Has Indentation Issue

This line:

```python
print()
```

should be inside the outer loop for proper formatting.

Correct version:

```python
for i in range(r+1,0,-1):
    for j in range(r+1,i-1,-1):
        print(j, end="")
    print()
```

---

## 📜 License

This project is open-source and free to use.