# Personal Journal Manager

A simple menu-driven Personal Journal Manager built using Python and file handling concepts.

## Features

* Create a journal file
* Add new journal entries with date and time
* View all saved journal entries
* Search entries using date, time, or keywords
* Delete all journal entries with confirmation
* Exception handling for invalid inputs and file-related errors

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* File Handling
* Custom Exceptions
* Exception Handling

## Project Structure

```
Personal-Journal-Manager/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/Personal-Journal-Manager.git
```

2. Open the project folder.

```bash
cd Personal-Journal-Manager
```

3. Run the program.

```bash
python journal_manager.py
```

## Menu Options

```
1. Create a Journal File
2. Add a New Entry
3. View all Entry
4. Search for an Entry
5. Delete All Entries
6. Exit
```

## Input Validation

### Date Validation

The program accepts dates only in the following format:

```
DD/MM/YYYY
```

Example:

```
23/08/2025
```

### Time Validation

The program accepts time only in 24-hour format:

```
HH:MM
```

Example:

```
14:30
```

## Concepts Demonstrated

* Classes and Objects
* Custom User-Defined Exceptions
* File Creation
* File Reading and Writing
* Search Operations
* Data Validation
* Menu-Driven Programming

## Sample Output

```
******************* Welcome to a Personal Journal Manager *********************

1. Create a Journal File
2. Add a New Entry
3. View all Entry
4. Search for an Entry
5. Delete All Entries
6. To exit
```

## Future Improvements

* Delete a specific journal entry
* Edit existing entries
* Password protection
* Automatic date and time retrieval
* Export entries to PDF

## Author

Pranjali Pandya

B.Tech Bioinformatics Student
