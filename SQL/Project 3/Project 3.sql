-- Project 3
CREATE DATABASE UniversityDB;
USE UniversityDB;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    BirthDate DATE,
    EnrollmentDate DATE NOT NULL
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    DepartmentID INT,
    Credits INT NOT NULL,
    FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    DepartmentID INT,
    Salary DECIMAL(10,2),
    FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    EnrollmentDate DATE NOT NULL,
    FOREIGN KEY (StudentID)
        REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID)
        REFERENCES Courses(CourseID),
    UNIQUE (StudentID, CourseID)
);

INSERT INTO Departments (DepartmentName)
VALUES
('Computer Science'),
('Mathematics'),
('Bioinformatics');

INSERT INTO Students
(FirstName, LastName, Email, BirthDate, EnrollmentDate)
VALUES
('John', 'Doe', 'john.doe@email.com', '2000-01-15', '2022-08-01'),
('Jane', 'Smith', 'jane.smith@email.com', '1999-05-25', '2021-08-01'),
('Rahul', 'Shah', 'rahul.shah@email.com', '2003-04-10', '2023-08-01'),
('Priya', 'Patel', 'priya.patel@email.com', '2002-07-20', '2024-08-01'),
('Amit', 'Verma', 'amit.verma@email.com', '2001-02-11', '2022-07-15'),
('Neha', 'Joshi', 'neha.joshi@email.com', '2004-09-05', '2025-08-01'),
('Arjun', 'Mehta', 'arjun.mehta@email.com', '2003-03-14', '2023-07-10'),
('Riya', 'Desai', 'riya.desai@email.com', '2002-12-22', '2024-07-01'),
('Karan', 'Trivedi', 'karan.trivedi@email.com', '2001-06-18', '2022-08-15'),
('Isha', 'Rao', 'isha.rao@email.com', '2004-11-09', '2025-07-20'),
('Dev', 'Patel', 'dev.patel@email.com', '2003-01-30', '2023-08-05'),
('Mira', 'Shah', 'mira.shah@email.com', '2002-05-16', '2024-08-10');

INSERT INTO Courses
(CourseID, CourseName, DepartmentID, Credits)
VALUES
(101, 'Introduction to SQL', 1, 3),
(102, 'Data Structures', 2, 4),
(103, 'Database Management', 1, 3),
(104, 'Statistics', 2, 4),
(105, 'Genomics', 3, 3),
(106, 'Machine Learning', 1, 4);

INSERT INTO Instructors
(FirstName, LastName, Email, DepartmentID, Salary)
VALUES
('Alice', 'Johnson', 'alice.johnson@univ.com', 1, 75000),
('Bob', 'Lee', 'bob.lee@univ.com', 2, 68000),
('Carol', 'Patel', 'carol.patel@univ.com', 3, 72000),
('David', 'Shah', 'david.shah@univ.com', 1, 82000);

INSERT INTO Enrollments
(StudentID, CourseID, EnrollmentDate)
VALUES
(1, 101, '2022-08-01'),
(1, 102, '2022-08-02'),
(2, 101, '2021-08-01'),
(2, 103, '2021-08-02'),
(3, 101, '2023-08-01'),
(3, 102, '2023-08-02'),
(4, 101, '2024-08-01'),
(4, 103, '2024-08-02'),
(5, 101, '2022-07-15'),
(5, 102, '2022-07-16'),
(6, 101, '2025-08-01'),
(6, 104, '2025-08-02'),
(7, 101, '2023-07-10'),
(7, 102, '2023-07-11'),
(8, 103, '2024-07-01'),
(8, 104, '2024-07-02'),
(9, 104, '2022-08-15'),
(10, 105, '2025-07-20'),
(11, 105, '2023-08-05'),
(12, 106, '2024-08-10');


-- Insert a department
INSERT INTO Departments (DepartmentName)
VALUES ('Physics');

-- Insert a student
INSERT INTO Students
(FirstName, LastName, Email, BirthDate, EnrollmentDate)
VALUES
('Aarav', 'Sharma', 'aarav@email.com', '2003-05-10', '2025-08-01');

-- Insert a course
INSERT INTO Courses
(CourseID, CourseName, DepartmentID, Credits)
VALUES
(107, 'Computer Networks', 1, 3);

-- Insert an instructor
INSERT INTO Instructors
(FirstName, LastName, Email, DepartmentID, Salary)
VALUES
('Meera', 'Joshi', 'meera@univ.com', 1, 70000);

-- Enroll a student in a course
INSERT INTO Enrollments
(StudentID, CourseID, EnrollmentDate)
VALUES
(13, 107, '2025-08-02');

SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Instructors;
SELECT * FROM Enrollments;
SELECT * FROM Departments;


UPDATE Students
SET Email = 'john.updated@email.com'
WHERE StudentID = 1;

UPDATE Courses
SET Credits = 5
WHERE CourseID = 102;

UPDATE Instructors
SET Salary = 80000
WHERE InstructorID = 1;

UPDATE Enrollments
SET EnrollmentDate = '2022-08-05'
WHERE EnrollmentID = 1;

UPDATE Departments
SET DepartmentName = 'Computer Science and Engineering'
WHERE DepartmentID = 1;

DELETE FROM Enrollments
WHERE EnrollmentID = 21;

DELETE FROM Courses
WHERE CourseID = 107;

DELETE FROM Instructors
WHERE InstructorID = 5;

DELETE FROM Students
WHERE StudentID = 13;

DELETE FROM Departments
WHERE DepartmentID = 4;

SELECT *
FROM Students
WHERE EnrollmentDate >= '2023-01-01'
ORDER BY EnrollmentDate;

SELECT c.CourseID, c.CourseName, c.Credits
FROM Courses c
INNER JOIN Departments d
    ON c.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Mathematics'
LIMIT 5;

-- Students with names starting with J
SELECT *
FROM Students
WHERE FirstName LIKE 'J%';

-- Courses with credits between 3 and 4
SELECT *
FROM Courses
WHERE Credits BETWEEN 3 AND 4;

-- Courses from selected departments
SELECT *
FROM Courses
WHERE DepartmentID IN (1, 2);

-- Students whose email is not NULL
SELECT *
FROM Students
WHERE Email IS NOT NULL;

-- Sort students by date of enrollment
SELECT *
FROM Students
ORDER BY EnrollmentDate DESC;

-- Display only the first 5 students
SELECT *
FROM Students
LIMIT 5;

SELECT
    c.CourseID,
    c.CourseName,
    COUNT(e.StudentID) AS TotalStudents
FROM Courses c
INNER JOIN Enrollments e
    ON c.CourseID = e.CourseID
GROUP BY c.CourseID, c.CourseName
HAVING COUNT(e.StudentID) > 5;

SELECT AVG(Credits) AS AverageCredits
FROM Courses;

SELECT AVG(Credits) AS AverageCredits
FROM Courses;

SELECT MAX(i.Salary) AS MaximumSalary
FROM Instructors i
INNER JOIN Departments d
    ON i.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Computer Science';

SELECT
    d.DepartmentName,
    COUNT(DISTINCT e.StudentID) AS TotalStudents
FROM Departments d
LEFT JOIN Courses c
    ON d.DepartmentID = c.DepartmentID
LEFT JOIN Enrollments e
    ON c.CourseID = e.CourseID
GROUP BY d.DepartmentID, d.DepartmentName;


SELECT COUNT(*) AS TotalStudents
FROM Students;

SELECT SUM(Credits) AS TotalCredits
FROM Courses;

SELECT MIN(Credits) AS MinimumCredits
FROM Courses;

SELECT DepartmentID, COUNT(*) AS TotalCourses
FROM Courses
GROUP BY DepartmentID;

SELECT DepartmentID, AVG(Salary) AS AverageSalary
FROM Instructors
GROUP BY DepartmentID
HAVING AVG(Salary) > 70000;

SELECT s.StudentID, s.FirstName, s.LastName
FROM Students s
WHERE s.StudentID IN (
    SELECT e.StudentID
    FROM Enrollments e
    INNER JOIN Courses c
        ON e.CourseID = c.CourseID
    WHERE c.CourseName = 'Introduction to SQL'
)
AND s.StudentID IN (
    SELECT e.StudentID
    FROM Enrollments e
    INNER JOIN Courses c
        ON e.CourseID = c.CourseID
    WHERE c.CourseName = 'Data Structures'
);

SELECT DISTINCT s.StudentID, s.FirstName, s.LastName
FROM Students s
INNER JOIN Enrollments e
    ON s.StudentID = e.StudentID
INNER JOIN Courses c
    ON e.CourseID = c.CourseID
WHERE c.CourseName IN (
    'Introduction to SQL',
    'Data Structures'
);

SELECT
    s.StudentID,
    CONCAT(s.FirstName, ' ', s.LastName) AS StudentName,
    c.CourseName,
    e.EnrollmentDate
FROM Students s
INNER JOIN Enrollments e
    ON s.StudentID = e.StudentID
INNER JOIN Courses c
    ON e.CourseID = c.CourseID;
    
SELECT
    s.StudentID,
    CONCAT(s.FirstName, ' ', s.LastName) AS StudentName,
    c.CourseName
FROM Students s
LEFT JOIN Enrollments e
    ON s.StudentID = e.StudentID
LEFT JOIN Courses c
    ON e.CourseID = c.CourseID;
    
-- RIGHT JOIN: All courses, including courses without enrollments
SELECT
    s.FirstName,
    c.CourseName
FROM Enrollments e
RIGHT JOIN Courses c
    ON e.CourseID = c.CourseID
LEFT JOIN Students s
    ON e.StudentID = s.StudentID;

-- CROSS JOIN: Every possible student-course combination
SELECT
    s.FirstName,
    c.CourseName
FROM Students s
CROSS JOIN Courses c;

-- SELF JOIN: Compare students who enrolled on the same date
SELECT
    s1.FirstName AS Student1,
    s2.FirstName AS Student2,
    s1.EnrollmentDate
FROM Students s1
INNER JOIN Students s2
    ON s1.EnrollmentDate = s2.EnrollmentDate
   AND s1.StudentID < s2.StudentID;
   
SELECT DISTINCT
    s.StudentID,
    s.FirstName,
    s.LastName
FROM Students s
INNER JOIN Enrollments e
    ON s.StudentID = e.StudentID
WHERE e.CourseID IN (
    SELECT CourseID
    FROM Enrollments
    GROUP BY CourseID
    HAVING COUNT(StudentID) > 10
);

-- Single-row subquery: Courses with credits above average
SELECT *
FROM Courses
WHERE Credits > (
    SELECT AVG(Credits)
    FROM Courses
);

-- Multi-row subquery: Students enrolled in any Mathematics course
SELECT *
FROM Students
WHERE StudentID IN (
    SELECT e.StudentID
    FROM Enrollments e
    INNER JOIN Courses c
        ON e.CourseID = c.CourseID
    WHERE c.DepartmentID = (
        SELECT DepartmentID
        FROM Departments
        WHERE DepartmentName = 'Mathematics'
    )
);

-- Correlated subquery: Courses with above-average credits
-- within their own department
SELECT c.CourseID, c.CourseName, c.Credits
FROM Courses c
WHERE c.Credits > (
    SELECT AVG(c2.Credits)
    FROM Courses c2
    WHERE c2.DepartmentID = c.DepartmentID
);

-- EXISTS: Students with at least one enrollment
SELECT s.*
FROM Students s
WHERE EXISTS (
    SELECT 1
    FROM Enrollments e
    WHERE e.StudentID = s.StudentID
);

-- NOT EXISTS: Students with no enrollments
SELECT s.*
FROM Students s
WHERE NOT EXISTS (
    SELECT 1
    FROM Enrollments e
    WHERE e.StudentID = s.StudentID
);

-- Subquery in FROM clause
SELECT DepartmentID, AVG(Credits) AS AverageCredits
FROM (
    SELECT DepartmentID, Credits
    FROM Courses
) AS CourseData
GROUP BY DepartmentID;

-- Subquery in SELECT clause
SELECT
    s.StudentID,
    s.FirstName,
    (
        SELECT COUNT(*)
        FROM Enrollments e
        WHERE e.StudentID = s.StudentID
    ) AS TotalEnrollments
FROM Students s;

SELECT
    StudentID,
    EnrollmentDate,
    YEAR(EnrollmentDate) AS EnrollmentYear
FROM Students;

-- Extract month
SELECT MONTH(EnrollmentDate) AS EnrollmentMonth
FROM Students;

-- Extract day
SELECT DAY(EnrollmentDate) AS EnrollmentDay
FROM Students;

-- Current date
SELECT CURDATE() AS Today;

-- Difference in days between enrollment and today
SELECT
    StudentID,
    DATEDIFF(CURDATE(), EnrollmentDate) AS DaysSinceEnrollment
FROM Students;

-- Add one year to enrollment date
SELECT DATE_ADD(EnrollmentDate, INTERVAL 1 YEAR) AS NextYear
FROM Students;

-- Format the date
SELECT DATE_FORMAT(EnrollmentDate, '%d-%m-%Y') AS FormattedDate
FROM Students;

-- Students enrolled during 2024
SELECT *
FROM Students
WHERE EnrollmentDate >= '2024-01-01'
  AND EnrollmentDate < '2025-01-01';
  
SELECT
    InstructorID,
    CONCAT(FirstName, ' ', LastName) AS InstructorName
FROM Instructors;

-- Convert names to uppercase
SELECT UPPER(FirstName) AS UpperName
FROM Students;

-- Convert names to lowercase
SELECT LOWER(LastName) AS LowerName
FROM Students;

-- Count characters in course names
SELECT CourseName, LENGTH(CourseName) AS NameLength
FROM Courses;

-- Extract first three characters
SELECT SUBSTRING(CourseName, 1, 3) AS ShortName
FROM Courses;

-- Remove extra spaces
SELECT TRIM('  University  ') AS CleanText;

-- Replace a word
SELECT REPLACE(CourseName, 'SQL', 'Database')
FROM Courses;

-- Find the position of a character
SELECT INSTR(CourseName, 'a') AS CharacterPosition
FROM Courses;

-- Combine strings with a separator
SELECT CONCAT_WS(' ', FirstName, LastName) AS FullName
FROM Students;

SELECT
    EnrollmentID,
    StudentID,
    CourseID,
    EnrollmentDate,
    COUNT(*) OVER (
        ORDER BY EnrollmentDate, EnrollmentID
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS RunningTotal
FROM Enrollments;

-- ROW_NUMBER
SELECT
    StudentID,
    FirstName,
    ROW_NUMBER() OVER (
        ORDER BY EnrollmentDate
    ) AS RowNum
FROM Students;

-- RANK
SELECT
    CourseName,
    Credits,
    RANK() OVER (
        ORDER BY Credits DESC
    ) AS CourseRank
FROM Courses;

-- DENSE_RANK
SELECT
    CourseName,
    Credits,
    DENSE_RANK() OVER (
        ORDER BY Credits DESC
    ) AS DenseRank
FROM Courses;

-- PARTITION BY: Rank courses within each department
SELECT
    CourseName,
    DepartmentID,
    Credits,
    RANK() OVER (
        PARTITION BY DepartmentID
        ORDER BY Credits DESC
    ) AS DepartmentRank
FROM Courses;

-- LAG: Previous enrollment date
SELECT
    StudentID,
    EnrollmentDate,
    LAG(EnrollmentDate) OVER (
        ORDER BY EnrollmentDate
    ) AS PreviousEnrollmentDate
FROM Enrollments;

-- LEAD: Next enrollment date
SELECT
    StudentID,
    EnrollmentDate,
    LEAD(EnrollmentDate) OVER (
        ORDER BY EnrollmentDate
    ) AS NextEnrollmentDate
FROM Enrollments;

-- COUNT as a window function
SELECT
    StudentID,
    CourseID,
    COUNT(*) OVER (
        PARTITION BY CourseID
    ) AS StudentsInCourse
FROM Enrollments;

SELECT
    StudentID,
    FirstName,
    LastName,
    EnrollmentDate,
    CASE
        WHEN EnrollmentDate < DATE_SUB(CURDATE(), INTERVAL 4 YEAR)
            THEN 'Senior'
        ELSE 'Junior'
    END AS StudentCategory
FROM Students;

-- Categorize course credits
SELECT
    CourseName,
    Credits,
    CASE
        WHEN Credits >= 4 THEN 'High Credits'
        WHEN Credits = 3 THEN 'Medium Credits'
        ELSE 'Low Credits'
    END AS CreditCategory
FROM Courses;

-- Categorize instructor salaries
SELECT
    FirstName,
    Salary,
    CASE
        WHEN Salary >= 80000 THEN 'High Salary'
        WHEN Salary >= 70000 THEN 'Medium Salary'
        ELSE 'Low Salary'
    END AS SalaryCategory
FROM Instructors;

-- DISTINCT: Unique course department IDs
SELECT DISTINCT DepartmentID
FROM Courses;

-- UNION: Combine student and instructor names
SELECT FirstName, LastName
FROM Students
UNION
SELECT FirstName, LastName
FROM Instructors;

-- UNION ALL: Combine names without removing duplicates
SELECT FirstName, LastName
FROM Students
UNION ALL
SELECT FirstName, LastName
FROM Instructors;

-- IFNULL: Replace missing values
SELECT
    s.FirstName,
    IFNULL(c.CourseName, 'Not Enrolled') AS CourseName
FROM Students s
LEFT JOIN Enrollments e
    ON s.StudentID = e.StudentID
LEFT JOIN Courses c
    ON e.CourseID = c.CourseID;

-- CASE with aggregate counts
SELECT
    c.CourseName,
    COUNT(e.StudentID) AS TotalStudents,
    CASE
        WHEN COUNT(e.StudentID) > 5 THEN 'Popular'
        ELSE 'Regular'
    END AS CourseStatus
FROM Courses c
LEFT JOIN Enrollments e
    ON c.CourseID = e.CourseID
GROUP BY c.CourseID, c.CourseName;

-- Find duplicate enrollment dates
SELECT EnrollmentDate, COUNT(*) AS Total
FROM Enrollments
GROUP BY EnrollmentDate
HAVING COUNT(*) > 1;

SHOW TABLES;

DESCRIBE Students;
DESCRIBE Courses;
DESCRIBE Instructors;
DESCRIBE Enrollments;
DESCRIBE Departments;

SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Instructors;
SELECT * FROM Enrollments;
SELECT * FROM Departments;
