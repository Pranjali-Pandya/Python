[README.md](https://github.com/user-attachments/files/33964130/README.md)
# Student Performance & Attendance Tracker

## Project Overview

The **Student Performance & Attendance Tracker** is a MySQL database
project designed to manage student records, departments, faculty,
courses, enrollments, attendance, and grades. It includes sample data
and SQL queries for reporting and analysis.

## Objectives

-   Store and manage student and department information.
-   Maintain faculty and course records.
-   Track student course enrollments.
-   Record attendance as Present, Absent, or Late.
-   Store marks and grades for each student and course.
-   Generate reports on academic performance and attendance.
-   Practise core and advanced SQL concepts using a realistic academic
    database.

## Technologies Used

-   **Database:** MySQL
-   **Language:** SQL

## Database Structure

The database is named `student_tracker_db` and contains seven tables:

  -----------------------------------------------------------------------
  Table                               Purpose
  ----------------------------------- -----------------------------------
  `Departments`                       Stores department names.

  `Students`                          Stores student details and links
                                      each student to a department.

  `Faculty`                           Stores faculty details, department,
                                      and years of experience.

  `Courses`                           Stores course names and their
                                      assigned faculty, if any.

  `Enrollments`                       Records the courses in which
                                      students are enrolled.

  `Attendance`                        Stores attendance records by
                                      student, course, and date.

  `Grades`                            Stores marks and grades for each
                                      student-course pair.
  -----------------------------------------------------------------------

### Relationships and Constraints

-   Students and faculty reference departments through foreign keys.
-   Courses can be assigned to a faculty member; the faculty assignment
    can be `NULL`.
-   Enrollments link students and courses and prevent duplicate
    student-course enrollments.
-   Attendance prevents duplicate records for the same student, course,
    and date.
-   Grades allow one grade record per student-course pair.
-   Marks are constrained to the range 0--100, and faculty experience
    cannot be negative.
-   Foreign-key rules control updates and deletions to preserve
    referential integrity.

## Features and SQL Concepts Demonstrated

The project contains sample records and queries covering:

1.  **Database and table creation** --- creates the database and all
    seven tables.
2.  **Data insertion and retrieval** --- inserts sample departments,
    students, faculty, courses, enrollments, grades, and attendance
    records.
3.  **Filtering and sorting** --- `WHERE`, `ORDER BY`, and `LIMIT`.
4.  **Grouping and filtering groups** --- `GROUP BY` and `HAVING`.
5.  **Logical operators** --- `AND`, `OR`, and `NOT`.
6.  **Aggregate functions** --- `SUM()`, `AVG()`, `MAX()`, `MIN()`, and
    `COUNT()`.
7.  **Joins** --- `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN`, plus a
    `UNION`-based example illustrating a full-outer-join equivalent.
8.  **Subqueries and CTEs** --- used to compare marks, summarize
    attendance, and filter results.
9.  **Date and time functions** --- `YEAR()`, `MONTH()`, `MONTHNAME()`,
    `TIMESTAMPDIFF()`, and `DATE_FORMAT()`.
10. **String and NULL-handling functions** --- `UPPER()`, `TRIM()`, and
    `COALESCE()`.
11. **Window functions** --- `RANK()` and cumulative/running totals.
12. **Conditional logic** --- `CASE` expressions for performance and
    attendance categories.
13. **Reports** --- student performance and attendance summaries.

## Example Reports

The included queries can be used to: - List students by name or student
ID. - Find students in a selected department. - Rank students by average
marks. - Identify students with attendance below 75%. - Calculate
student attendance percentages, counting both `Present` and `Late` as
attended. - Compare course averages and highest/lowest marks. - Count
students in each department. - Find courses without an assigned faculty
member. - Identify students without enrollments or grade records. -
Review monthly attendance trends and enrollment totals. - Create a
combined student performance and attendance overview.

## How to Run the Project

1.  Install and open a MySQL client, such as MySQL Workbench.
2.  Open the project's SQL script.
3.  Review the first statement:
    `DROP DATABASE IF EXISTS student_tracker_db;` **This deletes an
    existing database with that name and its contents.** Remove or
    comment out that statement if you need to preserve an existing
    database.
4.  Execute the SQL script from the beginning so the database, tables,
    sample data, and queries are created and run in order.
5.  Review the result grids for the `SELECT` statements.

> **Compatibility note:** The script uses MySQL syntax, including
> `ENUM`, `AUTO_INCREMENT`, CTEs, and window functions. Use a MySQL
> version that supports CTEs and window functions (MySQL 8.0 or later is
> recommended).

## Attendance Calculation

The queries treat `Present` and `Late` as attended statuses; `Absent` is
not counted as attended. Attendance percentage is calculated as:

`Attendance Percentage = (Present records + Late records) / Total attendance records × 100`

## Sample Data

The script inserts sample data for: - 4 departments - 5 faculty
members - 11 students - 6 courses - Student-course enrollments - Grade
records - Attendance records across multiple dates

These are demonstration records included in the SQL script, not real
institutional data.

## Project Files

-   `README.md` --- project documentation.
-   SQL script --- database schema, sample data, and report queries.

## Learning Outcomes

By completing this project, a learner can practise relational database
design, primary and foreign keys, constraints, data manipulation, joins,
aggregation, subqueries, CTEs, date/string functions, conditional
expressions, and window functions.

## Author

Add your name or team details here if required.
