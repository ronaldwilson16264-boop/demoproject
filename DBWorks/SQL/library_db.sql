create database library_db;

use library_db;

create table book (
    id int auto_increment primary key,
    title varchar(100),
    author varchar(100),
    price decimal(10, 2),
    pages int,
    language varchar(50)
);