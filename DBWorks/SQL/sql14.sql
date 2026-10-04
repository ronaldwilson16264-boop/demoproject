--  display the number of books in each category
select category, count(*) from books group by category;

--  display the average price of books in each category
select category, avg(price) from books group by category;

--  display the maximum price of books in each category
select category, max(price) from books group by category;

--  display the minimum price of books in each category
select category, min(price) from books group by category;



--  display the total price of books in each category
select category, sum(price) from books group by category;

--  display the book(s) whose price is greater than the average price of all books
select * from books where price > (select avg(price) from books);

-- display the book(s) having the highest price using a nested query
select * from books where price = (select max(price) from books);

--  display the book(s) having the lowest price using a nested query
select * from books where price = (select min(price) from books);

--  display the book(s) whose price is greater than the price of 'the alchemist' using a nested query
select * from books where price > (select price from books where book_name = 'the alchemist');

--  display the book(s) having the second-highest price using a nested query
select * from books where price = (select max(price) from books where price < (select max(price) from books));