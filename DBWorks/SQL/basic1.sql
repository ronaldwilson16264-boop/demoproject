-- Query for displaying all database files

show databases;

-- Query for creating a new db file
-- Create db dbname
create database company;


-- Switch to current db file
-- use dbname

use company;

-- Query for creating a db table
create table employee(
    empid int unique not null primary key,
    name varchar(20),
    age int,
    place varchar(20),
    gender enum("male","female"),
    designation varchar(20),
    salary int
);


-- inserting values
insert into employee(empid, name, age, place, gender, salary, designation)
values 
    (101, 'Arun', 23, 'ekm', 'male', 25000, 'developer'),
    (102, 'Amal', 24, 'tvm', 'male', 30000, 'developer'),
    (103, 'vipin', 27, 'ekm', 'male', 45000, 'developer'),
    (104, 'Anu', 24, 'tcr', 'female', 37000, 'tester'),
    (105, 'neenu', 29, 'tvm', 'female', 50000, 'HR'),
    (106, 'manu', 28, 'ekm', 'male', 48000, 'tester');
    


-- Query for reading all employee records (with all attributes)
SELECT * FROM employee;

-- Query for reading name, age attribute of all employees
SELECT name, age FROM employee;

-- Query for reading employee records whose place="ekm"
SELECT * FROM employee WHERE place = "ekm";

-- Query for reading employee records whose age<25
SELECT * FROM employee WHERE age < 25;

-- Query for reading employee records from ekm whose age is below 30
SELECT * FROM employee WHERE place = "ekm" AND age < 30;

-- Query for reading empid, name, salary of all employees
SELECT empid, name, salary FROM employee;  


-- employee records having place other than ekm
SELECT * FROM employee WHERE NOT (place = "ekm");
SELECT * FROM employee WHERE place != "ekm"; 


-- employee records whose name starts with letter 'A'
SELECT * FROM employee WHERE name LIKE 'A%';

-- employees having 3 letter name starting letter 'A'
SELECT * FROM employee WHERE name LIKE 'A__'; 

-- employees having 4 letter name ends with letter 'n'
SELECT * FROM employee WHERE name LIKE '___n';

-- employees whose place ends with letter 'm'
SELECT * FROM employee WHERE place LIKE '%m';

-- employee having 5 letter name
SELECT * FROM employee WHERE name LIKE '_____';


-- employees having salary between 30000 and 50000
SELECT * FROM employee WHERE salary BETWEEN 30000 AND 50000;

-- employees having age between 28 and 30
SELECT * FROM employee WHERE age BETWEEN 28 AND 30; 


-- employees having salary 30000 or salary 50000
-- in
SELECT * FROM employee WHERE salary IN (30000, 50000);

-- employees having age=23 or age=25
SELECT * FROM employee WHERE age IN (23, 25);
SELECT * FROM employee WHERE age = 23 OR age = 25; 



-- Display all employee details
SELECT * FROM employee;

-- Display all employee details in ascending order of salary
-- order by
SELECT * FROM employee ORDER BY salary;

-- Display all employee details in descending order of salary
SELECT * FROM employee ORDER BY salary DESC; 


-- Display all employee details in ascending order of age
SELECT * FROM employee ORDER BY age;

-- Display all employee details in descending order of name
SELECT * FROM employee ORDER BY name DESC; 

-- display place details of all employees
SELECT place FROM employee; 


-- display unique place details
-- distinct
SELECT DISTINCT(place) FROM employee;  


-- read first 3 rows
SELECT * FROM employee LIMIT 3;

-- read 2 rows after skipping first 3 rows
SELECT * FROM employee LIMIT 2 OFFSET 3;
-- or alternatively:
-- SELECT * FROM employee LIMIT 3, 2;

-- read 1 row after skipping first row
SELECT * FROM employee LIMIT 1 OFFSET 1;
--  alternative
-- SELECT * FROM employee LIMIT 1 OFFSET 1; 


-- update
SELECT * FROM employee;

UPDATE employee SET age = 28 WHERE empid = 103;

-- delete
DELETE FROM employee WHERE empid = 103; 


use company;

-- sum of salary of all employees
select sum(salary) from employee;

-- average salary of all employees
select avg(salary) from employee;

-- count of salary records
select count(salary) from employee;

-- minimum age among employees
select min(age) from employee;

-- maximum age among employees
select max(age) from employee;   



-- group by -having ---

select * from employee;

-- count of employees in each city
select place, count(*) from employee group by place;

-- count of employees in each gender
select gender, count(*) from employee group by gender;

-- count of employees in developer role
select designation, count(*) from employee group by designation having designation = 'developer'; 


-- max(salary) in each place
select place, max(salary) from employee group by place;

-- max(salary) in ekm
select place, max(salary) from employee group by place having place = 'ekm';

-- avg(salary) in male gender
select gender, avg(salary) from employee group by gender having gender = 'male';

-- avg(salary) in developer role
select designation, avg(salary) from employee group by designation having designation = 'developer';