-- Create a table named students to store student information
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(100),
    marks INT,
    city VARCHAR(100)
);

-- Insert sample records into the students table
INSERT INTO students (student_id, name, age, gender, course, marks, city) VALUES
(1, 'Adithya', 20, 'Male', 'Computer Science', 85, 'Kochi'),
(2, 'Fathima', 21, 'Female', 'Electronics', 78, 'Trivandrum'),
(3, 'Abhijith', 19, 'Male', 'Computer Science', 92, 'Kochi'),
(4, 'Sneha', 22, 'Female', 'Mechanical', 45, 'Kollam'),
(5, 'Rahul', 20, 'Male', 'Civil', 32, 'Kochi'),
(6, 'Ananya', 21, 'Female', 'Computer Science', 88, 'Calicut');


--  Display all records from the student’s table.
select * from students;

--  Display name, course, and marks for all students.
select name, course, marks from students;

--  Display names and marks of students who scored more than 80.
select name, marks from students where marks > 80;

--  Display all details of students enrolled in Computer Science.
select * from students where course = 'Computer Science';

-- Display names, ages, and cities of students whose age is between 18 and 22.
select name, age, city from students where age between 18 and 22;

--  Display names, marks, and courses of students from Kochi, sorted by marks in descending order.
select name, marks, course from students where city = 'Kochi' order by marks ;

--  Count the total number of students in each city.
select city, COUNT(*) from students group by city;

--  Display the average marks obtained by students in each course.
select course, AVG(marks) from students group by course;

--  Display details of the student(s) with the highest marks.
select * from students where marks = (select max(marks) from students);

--  Insert a new record into the students table.
insert into students (student_id, name, age, gender, course, marks, city) 
values (7, 'Rahul', 20, 'Male', 'Computer Science', 85, 'Kochi');

--  Update marks of all students who scored below 50 by adding 5 bonus marks.
update students set marks = marks + 5 WHERE marks < 50;

-- Delete all student records where marks are less than 35.
delete from students where marks < 35;