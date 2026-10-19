[README.md](https://github.com/user-attachments/files/33662131/README.md)
# University Course Management System

## Project Overview
This project uses **MySQL 8.0** to create and query a University Course Management System. It demonstrates relational database design and common SQL concepts, including CRUD operations, joins, aggregate functions, subqueries, date and string functions, window functions, and `CASE` expressions.

## Database
- **Database name:** `UniversityDB`
- **SQL file:** `Final Project.sql`
- **DBMS:** MySQL 8.0 or a compatible version

## Tables
The database contains five related tables:

| Table | Purpose |
|---|---|
| `Departments` | Stores academic department names. |
| `Students` | Stores student names, email addresses, birth dates, and enrollment dates. |
| `Courses` | Stores course names, department IDs, and credit values. |
| `Instructors` | Stores instructor details, department IDs, and salary. |
| `Enrollments` | Links students to courses and stores each course enrollment date. |

### Relationships
- A department can offer multiple courses.
- A department can have multiple instructors.
- A student can enroll in multiple courses.
- A course can have multiple students.
- `Enrollments` connects `Students` and `Courses` using foreign keys.
- The `Enrollments` table has a unique constraint on `(StudentID, CourseID)` to prevent duplicate enrollment of the same student in the same course.

## How to Run
1. Open **MySQL Workbench** and connect to your MySQL server.
2. Open `Final Project.sql`.
3. Execute the script from the beginning to create the database, tables, and sample records.
4. Run the queries in sections to view the results.
5. Check the final table contents with the verification queries at the end of the file.

> Run the file against a test database. The script contains `UPDATE` and `DELETE` statements, so executing the entire file repeatedly can change or remove test records.

## SQL Concepts Demonstrated
- **Database and table creation:** `CREATE DATABASE`, `CREATE TABLE`
- **CRUD operations:** `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- **Constraints:** primary keys, foreign keys, `NOT NULL`, `UNIQUE`, `AUTO_INCREMENT`
- **Filtering and sorting:** `WHERE`, `LIKE`, `BETWEEN`, `IN`, `IS NOT NULL`, `ORDER BY`, `LIMIT`
- **Aggregate functions:** `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- **Grouping:** `GROUP BY`, `HAVING`
- **Joins:** `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `CROSS JOIN`, self join
- **Set operations:** `UNION`, `UNION ALL`
- **Subqueries:** single-row, multi-row, correlated, `FROM`, and `SELECT` subqueries; `IN`, `EXISTS`, `NOT EXISTS`
- **Date functions:** `YEAR`, `MONTH`, `DAY`, `CURDATE`, `DATEDIFF`, `DATE_ADD`, `DATE_FORMAT`
- **String functions:** `CONCAT`, `CONCAT_WS`, `UPPER`, `LOWER`, `LENGTH`, `SUBSTRING`, `TRIM`, `REPLACE`, `INSTR`
- **Window functions:** running total, `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PARTITION BY`, `LAG`, `LEAD`
- **Conditional logic:** `CASE`, `IFNULL`
- **Inspection commands:** `SHOW TABLES`, `DESCRIBE`

## Main Assignment Queries
The script includes examples to:
1. Find students enrolled after 2022.
2. List courses offered by the Mathematics department, with a maximum of five results.
3. Count students enrolled in each course and filter courses with more than five students.
4. Calculate the average credits across courses.
5. Find the maximum instructor salary in Computer Science.
6. Count distinct enrolled students in each department.
7. Find students enrolled in both specified courses or either course.
8. Retrieve student-course records using inner and left joins.
9. Find students enrolled in courses with more than ten students.
10. Extract enrollment years and concatenate instructor names.
11. Calculate a running total of enrollments.
12. Label students as `Senior` or `Junior` based on whether their enrollment date is more than four years before the current date.

## Assumptions
- The `Salary` column is included in `Instructors` because the maximum-salary query requires it.
- Student counts by department are based on distinct students enrolled in courses belonging to that department.
- The `Senior`/`Junior` classification is calculated dynamically using `CURDATE()`.
- Sample records are provided for practicing the queries.

## Important Notes
- The sample data currently has no course with more than ten enrollments, so the corresponding subquery may return no rows until more enrollment records are added.
- The sample data currently has no course with more than five enrollments, so the `HAVING COUNT(...) > 5` query may also return no rows.
- The sample script contains an `AVG(Credits)` query twice.
- The demonstration `DELETE` statements use fixed IDs. Check that the target records exist before running them. Foreign-key constraints require dependent enrollment rows to be deleted before deleting referenced students or courses.
- Some CRUD demonstration statements use IDs that may not exist in the sample data at that point. Treat these as examples and adjust IDs to match the current database state.

## Repository Structure
```text
University-Course-Management-System/
├── Final Project.sql
└── README.md
```

## Author
Add your name, course, university, and submission date here before submitting the project.
