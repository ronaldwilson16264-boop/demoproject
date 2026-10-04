-- create departments table
create table departments (
    id int primary key,
    department_name varchar(50)
);

-- insert values into departments
insert into departments values
(1, 'computer science'),
(2, 'hr'),
(3, 'finance'),
(4, 'marketing');

-- create employee1 table
create table employee1 (
    id int primary key,
    employee_name varchar(50),
    age int,
    salary int,
    joining_year int,
    department_id int,
    city varchar(50),
    foreign key (department_id) references departments(id)
);

-- insert values into employee1
insert into employee1 values
(1, 'arun', 25, 55000, 2021, 1, 'kochi'),
(2, 'anu', 28, 65000, 2022, 1, 'kochi'),
(3, 'rahul', 30, 45000, 2019, 2, 'trivandrum'),
(4, 'amal', 24, 70000, 2023, 3, 'kochi'),
(5, 'meera', 27, 40000, 2020, 2, 'kollam'),
(6, 'arjun', 32, 80000, 2021, 3, 'kochi'),
(7, 'neha', 26, 50000, 2022, 4, 'kollam'),
(8, 'abhay', 29, 60000, 2023, 4, 'trivandrum');

-- retrieve all records from departments
select * from departments;

--  retrieve employee name, age and salary
select employee_name, age, salary from employee1;

--  employees with salary greater than 50,000
select employee_name, salary from employee1 where salary > 50000;

--  employees whose name starts with a
select employee_name, age, city from employee1 where employee_name like 'a%';

--  employees joined after 2020 and salary greater than 60,000
select employee_name, salary from employee1 where joining_year > 2020 and salary > 60000;

--  employees from kochi sorted by salary descending
select employee_name, city, salary from employee1 where city = 'kochi' order by salary desc;

-- number of employees in each department
select department_id, count(*) from employee1 group by department_id;

-- average salary for each city
select city, avg(salary) from employee1 group by city;

--  cities where average salary is greater than 45,000
select city, avg(salary) from employee1 group by city having avg(salary) > 45000;

--  employee name with department name
select employee_name, department_name
from employee1 join departments on employee1.department_id = departments.id;