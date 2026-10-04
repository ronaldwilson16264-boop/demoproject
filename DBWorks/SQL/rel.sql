create database task_db1;

use task_db1;

create table User(
id int not null primary key,
name varchar(20) not null unique,
email varchar(30) not null unique,
phone varchar(20) not null);

create table Task(id int not null primary key,
title varchar(30),
user_id int,
status enum("pending","finished") default "pending",
date datetime default current_timestamp,
foreign key (user_id) references User(id));




insert into User(id,name,email,phone) values(1,"arun","a@gmail.com","789356677"),(2,"amal","amal@gmail.com","896665677"),
(3,"hari","hari@gmail.com","8456766122");

insert into Task(id,title,user_id)values(1,'pay bill',1),
(2,'buy groceries',1),
(3,'book ticket',3);

-- select * from User;

select * from Task;


select * from User inner join Task
on User.id = Task.user_id;

select name, title, status from User inner join Task on User.id = Task.user_id
where name = "arun";

select * from User left join Task on User.id = Task.user_id; 

select name, title, status from User left join Task on User.id = Task.user_id;