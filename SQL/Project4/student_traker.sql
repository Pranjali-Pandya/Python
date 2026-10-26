DROP DATABASE IF EXISTS student_tracker_db;
CREATE DATABASE student_tracker_db;
USE student_tracker_db;


CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE,
    gender VARCHAR(20),
    email VARCHAR(150) UNIQUE,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    admission_date DATE NOT NULL,
    department_id INT NOT NULL,
    CONSTRAINT fk_students_department
        FOREIGN KEY (department_id) REFERENCES Departments(department_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE Faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    phone_number VARCHAR(20),
    department_id INT NOT NULL,
    experience_years INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_faculty_experience CHECK (experience_years >= 0),
    CONSTRAINT fk_faculty_department
        FOREIGN KEY (department_id) REFERENCES Departments(department_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(120) NOT NULL,
    faculty_id INT NULL,
    CONSTRAINT fk_courses_faculty
        FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    CONSTRAINT uq_student_course_enrollment UNIQUE (student_id, course_id),
    CONSTRAINT fk_enrollments_student
        FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_enrollments_course
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late') NOT NULL,
    CONSTRAINT uq_attendance_student_course_date
        UNIQUE (student_id, course_id, attendance_date),
    CONSTRAINT fk_attendance_student
        FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_attendance_course
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    marks_obtained DECIMAL(5,2) NOT NULL,
    grade VARCHAR(5),
    CONSTRAINT chk_marks_range CHECK (marks_obtained BETWEEN 0 AND 100),
    CONSTRAINT uq_grade_student_course UNIQUE (student_id, course_id),
    CONSTRAINT fk_grades_student
        FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_grades_course
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);


INSERT INTO Departments (department_id, department_name) VALUES
(1, 'Computer Science'),
(2, 'Bioinformatics'),
(3, 'Information Technology'),
(4, 'Business Administration');

INSERT INTO Faculty
(faculty_id, name, email, phone_number, department_id, experience_years) VALUES
(1, 'Aarav Shah', 'aarav.shah@example.com', '9000000001', 1, 8),
(2, 'Meera Patel', 'meera.patel@example.com', '9000000002', 2, 6),
(3, 'Rohan Desai', 'rohan.desai@example.com', '9000000003', 3, 4),
(4, 'Nisha Joshi', 'nisha.joshi@example.com', '9000000004', 1, 10),
(5, 'Kunal Trivedi', 'kunal.trivedi@example.com', '9000000005', 4, 3);

INSERT INTO Students
(student_id, name, dob, gender, email, phone_number, address, admission_date, department_id) VALUES
(1, 'Anaya Mehta', '2005-02-14', 'Female', 'anaya.mehta@example.com', '9100000001', 'Rajkot', '2024-07-01', 1),
(2, 'Dev Patel', '2004-11-20', 'Male', 'dev.patel@example.com', '9100000002', 'Ahmedabad', '2024-07-03', 1),
(3, 'Isha Shah', '2005-06-09', 'Female', 'isha.shah@example.com', '9100000003', 'Jamnagar', '2024-07-05', 2),
(4, 'Krish Joshi', '2004-08-17', 'Male', 'krish.joshi@example.com', '9100000004', 'Rajkot', '2024-07-07', 3),
(5, 'Mira Desai', '2005-12-01', 'Female', NULL, '9100000005', 'Surat', '2024-07-09', 2),
(6, 'Neel Shah', '2004-04-25', 'Male', 'neel.shah@example.com', '9100000006', 'Vadodara', '2024-07-11', 1),
(7, 'Pari Trivedi', '2005-09-12', 'Female', 'pari.trivedi@example.com', '9100000007', 'Bhavnagar', '2024-07-13', 3),
(8, 'Rudra Parmar', '2004-03-30', 'Male', 'rudra.parmar@example.com', '9100000008', 'Morbi', '2024-07-15', 4),
(9, 'Sana Khan', '2005-01-05', 'Female', 'sana.khan@example.com', '9100000009', 'Rajkot', '2025-01-10', 1),
(10, 'Vivaan Rao', '2004-07-19', 'Male', 'vivaan.rao@example.com', '9100000010', 'Gandhinagar', '2025-01-12', 4),
(11, 'Zoya Sheikh', '2005-10-22', 'Female', 'zoya.sheikh@example.com', '9100000011', 'Ahmedabad', '2025-01-14', 2);

INSERT INTO Courses (course_id, course_name, faculty_id) VALUES
(1, 'Database Management Systems', 1),
(2, 'Python Programming', 4),
(3, 'Bioinformatics Fundamentals', 2),
(4, 'Data Analytics', 3),
(5, 'Business Communication', 5),
(6, 'Computer Networks', NULL);

INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES
(1,1,1,'2024-07-10'), (2,1,2,'2024-07-10'), (3,2,1,'2024-07-10'),
(4,2,2,'2024-07-10'), (5,3,3,'2024-07-10'), (6,3,1,'2024-07-11'),
(7,4,4,'2024-07-11'), (8,5,3,'2024-07-12'), (9,6,1,'2024-07-12'),
(10,6,2,'2024-07-12'), (11,7,4,'2024-07-13'), (12,8,5,'2024-07-14'),
(13,9,1,'2025-01-15'), (14,10,5,'2025-01-15');

INSERT INTO Grades (grade_id, student_id, course_id, marks_obtained, grade) VALUES
(1,1,1,96,'A+'), (2,1,2,91,'A+'), (3,2,1,68,'C'),
(4,2,2,72,'B'), (5,3,3,88,'A'), (6,3,1,79,'B+'),
(7,4,4,93,'A+'), (8,5,3,59,'D'), (9,6,1,84,'A'),
(10,6,2,90,'A'), (11,7,4,76,'B+'), (12,8,5,81,'A'),
(13,9,1,45,'F'), (14,10,5,67,'C');

-- Attendance sample data: 10 dates per student-course pair.
-- Status 'Present' and 'Late' count as attended; 'Absent' does not.
INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES
(1,1,'2025-01-06','Present'),(1,1,'2025-01-07','Present'),(1,1,'2025-01-08','Present'),(1,1,'2025-01-09','Present'),(1,1,'2025-01-10','Present'),
(1,1,'2025-01-13','Present'),(1,1,'2025-01-14','Present'),(1,1,'2025-01-15','Present'),(1,1,'2025-01-16','Late'),(1,1,'2025-01-17','Present'),
(2,1,'2025-01-06','Present'),(2,1,'2025-01-07','Absent'),(2,1,'2025-01-08','Absent'),(2,1,'2025-01-09','Present'),(2,1,'2025-01-10','Absent'),
(2,1,'2025-01-13','Absent'),(2,1,'2025-01-14','Present'),(2,1,'2025-01-15','Absent'),(2,1,'2025-01-16','Absent'),(2,1,'2025-01-17','Absent'),
(3,3,'2025-01-06','Present'),(3,3,'2025-01-07','Present'),(3,3,'2025-01-08','Present'),(3,3,'2025-01-09','Present'),(3,3,'2025-01-10','Absent'),
(3,3,'2025-01-13','Present'),(3,3,'2025-01-14','Present'),(3,3,'2025-01-15','Present'),(3,3,'2025-01-16','Present'),(3,3,'2025-01-17','Present'),
(4,4,'2025-01-06','Present'),(4,4,'2025-01-07','Present'),(4,4,'2025-01-08','Absent'),(4,4,'2025-01-09','Present'),(4,4,'2025-01-10','Present'),
(4,4,'2025-01-13','Present'),(4,4,'2025-01-14','Present'),(4,4,'2025-01-15','Absent'),(4,4,'2025-01-16','Present'),(4,4,'2025-01-17','Present'),
(5,3,'2025-01-06','Absent'),(5,3,'2025-01-07','Absent'),(5,3,'2025-01-08','Present'),(5,3,'2025-01-09','Absent'),(5,3,'2025-01-10','Absent'),
(5,3,'2025-01-13','Absent'),(5,3,'2025-01-14','Absent'),(5,3,'2025-01-15','Present'),(5,3,'2025-01-16','Absent'),(5,3,'2025-01-17','Absent'),
(6,1,'2025-01-06','Present'),(6,1,'2025-01-07','Present'),(6,1,'2025-01-08','Present'),(6,1,'2025-01-09','Present'),(6,1,'2025-01-10','Present'),
(6,1,'2025-01-13','Present'),(6,1,'2025-01-14','Present'),(6,1,'2025-01-15','Present'),(6,1,'2025-01-16','Present'),(6,1,'2025-01-17','Present'),
(7,4,'2025-01-06','Present'),(7,4,'2025-01-07','Absent'),(7,4,'2025-01-08','Present'),(7,4,'2025-01-09','Absent'),(7,4,'2025-01-10','Present'),
(7,4,'2025-01-13','Absent'),(7,4,'2025-01-14','Present'),(7,4,'2025-01-15','Absent'),(7,4,'2025-01-16','Present'),(7,4,'2025-01-17','Absent');



SELECT * FROM Students ORDER BY student_id;

-- 4. WHERE, HAVING, LIMIT
-- Students in the Computer Science department
SELECT s.student_id, s.name, d.department_name
FROM Students AS s
INNER JOIN Departments AS d ON d.department_id = s.department_id
WHERE d.department_name = 'Computer Science'
ORDER BY s.name;

-- Top 10 highest-scoring students by overall average marks
SELECT s.student_id, s.name, ROUND(AVG(g.marks_obtained), 2) AS average_marks
FROM Students AS s
JOIN Grades AS g ON g.student_id = s.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks DESC
LIMIT 10;

-- Students whose overall attendance is below 75%
SELECT s.student_id, s.name,
       ROUND(100.0 * SUM(a.status IN ('Present','Late')) / COUNT(*), 2) AS attendance_percentage
FROM Students AS s
JOIN Attendance AS a ON a.student_id = s.student_id
GROUP BY s.student_id, s.name
HAVING attendance_percentage < 75
ORDER BY attendance_percentage;


-- 5. AND, OR, NOT OPERATORS

-- Attendance below 50% AND failing (average marks below 50)
WITH attendance_summary AS (
    SELECT student_id,
           100.0 * SUM(status IN ('Present','Late')) / COUNT(*) AS attendance_percentage
    FROM Attendance
    GROUP BY student_id
),
grade_summary AS (
    SELECT student_id, AVG(marks_obtained) AS average_marks
    FROM Grades
    GROUP BY student_id
)
SELECT s.student_id, s.name, a.attendance_percentage, g.average_marks
FROM Students s
JOIN attendance_summary a ON a.student_id = s.student_id
JOIN grade_summary g ON g.student_id = s.student_id
WHERE a.attendance_percentage < 50 AND g.average_marks < 50;

-- Students who scored above 90 OR have perfect attendance (100%)
WITH attendance_summary AS (
    SELECT student_id,
           100.0 * SUM(status IN ('Present','Late')) / COUNT(*) AS attendance_percentage
    FROM Attendance
    GROUP BY student_id
),
grade_summary AS (
    SELECT student_id, MAX(marks_obtained) AS highest_mark
    FROM Grades GROUP BY student_id
)
SELECT DISTINCT s.student_id, s.name, g.highest_mark, a.attendance_percentage
FROM Students s
LEFT JOIN grade_summary g ON g.student_id = s.student_id
LEFT JOIN attendance_summary a ON a.student_id = s.student_id
WHERE g.highest_mark > 90 OR a.attendance_percentage = 100;

-- Faculty members NOT assigned to any course
SELECT f.faculty_id, f.name
FROM Faculty f
WHERE NOT EXISTS (
    SELECT 1 FROM Courses c WHERE c.faculty_id = f.faculty_id
);

-- 6. ORDER BY AND GROUP BY

-- Alphabetical student list
SELECT student_id, name FROM Students ORDER BY name ASC;

-- Number of students in each department (including departments with zero)
SELECT d.department_id, d.department_name, COUNT(s.student_id) AS student_count
FROM Departments d
LEFT JOIN Students s ON s.department_id = d.department_id
GROUP BY d.department_id, d.department_name
ORDER BY student_count DESC, d.department_name;

-- Average marks per course
SELECT c.course_id, c.course_name, ROUND(AVG(g.marks_obtained), 2) AS average_marks
FROM Courses c
LEFT JOIN Grades g ON g.course_id = c.course_id
GROUP BY c.course_id, c.course_name
ORDER BY average_marks DESC;

-- 7. AGGREGATE FUNCTIONS: SUM, AVG, MAX, MIN, COUNT

-- Average attendance percentage per student, then average across students
WITH per_student_attendance AS (
    SELECT student_id,
           100.0 * SUM(status IN ('Present','Late')) / COUNT(*) AS attendance_percentage
    FROM Attendance
    GROUP BY student_id
)
SELECT ROUND(AVG(attendance_percentage), 2) AS average_student_attendance_percentage
FROM per_student_attendance;

-- Highest and lowest marks in each course
SELECT c.course_id, c.course_name,
       MAX(g.marks_obtained) AS highest_marks,
       MIN(g.marks_obtained) AS lowest_marks
FROM Courses c
LEFT JOIN Grades g ON g.course_id = c.course_id
GROUP BY c.course_id, c.course_name;

-- Total number of students per department
SELECT d.department_name, COUNT(s.student_id) AS total_students
FROM Departments d
LEFT JOIN Students s ON s.department_id = d.department_id
GROUP BY d.department_id, d.department_name;

-- Additional examples for SUM and COUNT
SELECT course_id, SUM(marks_obtained) AS total_marks, COUNT(*) AS graded_student_count
FROM Grades
GROUP BY course_id;

-- 8. PRIMARY / FOREIGN KEY RELATIONSHIPS

-- Check for duplicate student-course enrollments (should return no rows)
SELECT student_id, course_id, COUNT(*) AS duplicate_count
FROM Enrollments
GROUP BY student_id, course_id
HAVING COUNT(*) > 1;

-- Courses and the faculty member who teaches each course
SELECT c.course_id, c.course_name, f.faculty_id, f.name AS faculty_name
FROM Courses c
LEFT JOIN Faculty f ON f.faculty_id = c.faculty_id
ORDER BY c.course_id;

-- 9. JOINS: INNER, LEFT, RIGHT, FULL OUTER JOIN EQUIVALENT

-- INNER JOIN: student details with department
SELECT s.student_id, s.name, s.email, d.department_name
FROM Students s
INNER JOIN Departments d ON d.department_id = s.department_id
ORDER BY s.student_id;

-- LEFT JOIN: students who have not enrolled in any course
SELECT s.student_id, s.name
FROM Students s
LEFT JOIN Enrollments e ON e.student_id = s.student_id
WHERE e.enrollment_id IS NULL;

-- RIGHT JOIN: courses that have no faculty assigned
SELECT c.course_id, c.course_name, f.faculty_id, f.name AS faculty_name
FROM Faculty f
RIGHT JOIN Courses c ON c.faculty_id = f.faculty_id
WHERE f.faculty_id IS NULL;

-- FULL OUTER JOIN equivalent in MySQL:
-- MySQL has no FULL OUTER JOIN keyword. This UNION combines unmatched
-- students (no grade) and unmatched grade records (normally prevented by FK).
SELECT s.student_id, s.name, g.course_id, g.marks_obtained
FROM Students s
LEFT JOIN Grades g ON g.student_id = s.student_id
WHERE g.grade_id IS NULL
UNION
SELECT s.student_id, s.name, g.course_id, g.marks_obtained
FROM Students s
RIGHT JOIN Grades g ON g.student_id = s.student_id
WHERE s.student_id IS NULL;

-- More direct version: students who do not have any grade
SELECT s.student_id, s.name
FROM Students s
LEFT JOIN Grades g ON g.student_id = s.student_id
WHERE g.grade_id IS NULL;

-- ============================================================
-- 10. SUBQUERIES
-- ============================================================

-- Students with marks above the average score across all grade records
SELECT DISTINCT s.student_id, s.name, g.marks_obtained
FROM Students s
JOIN Grades g ON g.student_id = s.student_id
WHERE g.marks_obtained > (SELECT AVG(marks_obtained) FROM Grades)
ORDER BY g.marks_obtained DESC;

-- Courses taught by faculty members with at least 5 years of experience
SELECT c.course_id, c.course_name, f.name AS faculty_name, f.experience_years
FROM Courses c
JOIN Faculty f ON f.faculty_id = c.faculty_id
WHERE f.experience_years >= 5;

-- Students who have missed more than 10 classes
SELECT s.student_id, s.name, COUNT(*) AS classes_missed
FROM Students s
JOIN Attendance a ON a.student_id = s.student_id
WHERE a.status = 'Absent'
GROUP BY s.student_id, s.name
HAVING COUNT(*) > 10;


-- 11. DATE AND TIME FUNCTIONS
-- Attendance trends by month
SELECT YEAR(attendance_date) AS attendance_year,
       MONTH(attendance_date) AS attendance_month,
       MONTHNAME(attendance_date) AS month_name,
       COUNT(*) AS attendance_records,
       SUM(status IN ('Present','Late')) AS attended_records
FROM Attendance
GROUP BY YEAR(attendance_date), MONTH(attendance_date), MONTHNAME(attendance_date)
ORDER BY attendance_year, attendance_month;

-- Number of years since each student's admission
SELECT student_id, name, admission_date,
       TIMESTAMPDIFF(YEAR, admission_date, CURRENT_DATE()) AS years_since_admission
FROM Students
ORDER BY student_id;

-- Format attendance date as DD-MM-YYYY
SELECT attendance_id, student_id, course_id,
       DATE_FORMAT(attendance_date, '%d-%m-%Y') AS formatted_attendance_date,
       status
FROM Attendance
ORDER BY attendance_date, student_id;


-- 12. STRING MANIPULATION FUNCTIONS


-- Faculty names in uppercase
SELECT faculty_id, UPPER(name) AS faculty_name_uppercase
FROM Faculty;

-- Trim leading/trailing spaces from student names
SELECT student_id, name, TRIM(name) AS trimmed_name
FROM Students;

-- Replace NULL faculty email fields with a readable message
SELECT faculty_id, name,
       COALESCE(email, 'Email Not Provided') AS email_display
FROM Faculty;

-- Same NULL-handling requirement demonstrated for student email fields
SELECT student_id, name,
       COALESCE(email, 'Email Not Provided') AS email_display
FROM Students;

-- 13. WINDOW FUNCTIONS 

-- Rank students by overall average marks
WITH student_average AS (
    SELECT s.student_id, s.name, AVG(g.marks_obtained) AS average_marks
    FROM Students s
    JOIN Grades g ON g.student_id = s.student_id
    GROUP BY s.student_id, s.name
)
SELECT student_id, name, ROUND(average_marks, 2) AS average_marks,
       RANK() OVER (ORDER BY average_marks DESC) AS performance_rank
FROM student_average
ORDER BY performance_rank, name;

-- Cumulative attendance percentage per course, ordered by date.
-- Present and Late count as attended. This is a running rate, not a final rate.
WITH daily_course AS (
    SELECT course_id, attendance_date,
           COUNT(*) AS records_on_date,
           SUM(status IN ('Present','Late')) AS attended_on_date
    FROM Attendance
    GROUP BY course_id, attendance_date
),
running_course AS (
    SELECT course_id, attendance_date,
           SUM(records_on_date) OVER (
               PARTITION BY course_id ORDER BY attendance_date
               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
           ) AS cumulative_records,
           SUM(attended_on_date) OVER (
               PARTITION BY course_id ORDER BY attendance_date
               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
           ) AS cumulative_attended
    FROM daily_course
)
SELECT course_id, attendance_date, cumulative_records, cumulative_attended,
       ROUND(100.0 * cumulative_attended / NULLIF(cumulative_records, 0), 2)
           AS cumulative_attendance_percentage
FROM running_course
ORDER BY course_id, attendance_date;

-- Running total of students enrolled per month
WITH monthly_enrollments AS (
    SELECT DATE_FORMAT(enrollment_date, '%Y-%m-01') AS enrollment_month,
           COUNT(*) AS new_enrollments
    FROM Enrollments
    GROUP BY DATE_FORMAT(enrollment_date, '%Y-%m-01')
)
SELECT enrollment_month, new_enrollments,
       SUM(new_enrollments) OVER (
           ORDER BY enrollment_month
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total_enrollments
FROM monthly_enrollments
ORDER BY enrollment_month;

-- ============================================================
-- 14. CASE EXPRESSIONS
-- ============================================================

-- Performance categories by marks
SELECT student_id, course_id, marks_obtained,
       CASE
           WHEN marks_obtained > 90 THEN 'Excellent'
           WHEN marks_obtained BETWEEN 75 AND 90 THEN 'Good'
           ELSE 'Needs Improvement'
       END AS performance_level
FROM Grades
ORDER BY student_id, course_id;

-- Attendance categories by each student's overall attendance rate
WITH student_attendance AS (
    SELECT student_id,
           100.0 * SUM(status IN ('Present','Late')) / COUNT(*) AS attendance_percentage
    FROM Attendance
    GROUP BY student_id
)
SELECT s.student_id, s.name, ROUND(a.attendance_percentage, 2) AS attendance_percentage,
       CASE
           WHEN a.attendance_percentage > 80 THEN 'Regular'
           WHEN a.attendance_percentage BETWEEN 50 AND 80 THEN 'Irregular'
           ELSE 'Defaulter'
       END AS attendance_category
FROM student_attendance a
JOIN Students s ON s.student_id = a.student_id
ORDER BY a.attendance_percentage DESC;

-- Categorize individual attendance records as well, using the overall rate
-- for the student. The assignment's categories refer to percentages, not a
-- single Present/Absent/Late value.
WITH student_attendance AS (
    SELECT student_id,
           100.0 * SUM(status IN ('Present','Late')) / COUNT(*) AS attendance_percentage
    FROM Attendance
    GROUP BY student_id
)
SELECT a.attendance_id, s.name, c.course_name, a.attendance_date, a.status,
       ROUND(sa.attendance_percentage, 2) AS student_attendance_percentage,
       CASE
           WHEN sa.attendance_percentage > 80 THEN 'Regular'
           WHEN sa.attendance_percentage BETWEEN 50 AND 80 THEN 'Irregular'
           ELSE 'Defaulter'
       END AS attendance_category
FROM Attendance a
JOIN Students s ON s.student_id = a.student_id
JOIN Courses c ON c.course_id = a.course_id
JOIN student_attendance sa ON sa.student_id = a.student_id
ORDER BY a.attendance_date, s.name;
-- 15. OPTIONAL REPORT QUERIES

-- Student performance and attendance overview
WITH marks_summary AS (
    SELECT student_id, AVG(marks_obtained) AS average_marks
    FROM Grades GROUP BY student_id
),
attendance_summary AS (
    SELECT student_id,
           100.0 * SUM(status IN ('Present','Late')) / COUNT(*) AS attendance_percentage
    FROM Attendance GROUP BY student_id
)
SELECT s.student_id, s.name, d.department_name,
       ROUND(ms.average_marks, 2) AS average_marks,
       ROUND(att.attendance_percentage, 2) AS attendance_percentage
FROM Students s
JOIN Departments d ON d.department_id = s.department_id
LEFT JOIN marks_summary ms ON ms.student_id = s.student_id
LEFT JOIN attendance_summary att ON att.student_id = s.student_id
ORDER BY ms.average_marks DESC, s.name;


