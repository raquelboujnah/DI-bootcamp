-- create table customer(
-- 	id serial primary key,
-- 	first_name varchar(50),
-- 	last_name varchar(50) not null
-- );

-- create table customer_profile(
-- 	id serial primary key,
-- 	isLoggedIn boolean default false,
-- 	customer_id int unique,
	
-- 	foreign key (customer_id) references customer(id)
-- );

-- insert into customer(first_name, last_name)
-- values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')

-- insert into customer_profile(isLoggedIn, customer_id)
-- values
-- (true, (select id from customer where first_name = 'John')),
-- (false, (select id from customer where first_name = 'Jerome'))

-- select c.first_name
-- from customer as c
-- inner join customer_profile as cp on c.id = cp.customer_id
-- where cp.isLoggedIn = true;

-- create table book(
-- 	book_id serial primary key,
-- 	title varchar(50) not null,
-- 	author varchar(50) not null 
-- );

-- insert into book(title, author)
-- values
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student(
-- 	student_id serial primary key,
-- 	name varchar(50) not null unique,
-- 	age integer check(age <= 15)
-- );

-- insert into student(name, age)
-- values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table book_library(
-- 	book_fk_id integer,
-- 	student_id integer,
-- 	borrowed_date date,
	
-- 	foreign key (book_fk_id) references book(book_id) on delete cascade on update cascade,
-- 	foreign key (student_id) references student(student_id) on delete cascade on update cascade
-- );

-- insert into book_library (book_fk_id, student_id, borrowed_date)
-- values 
-- (
-- 	(select book_id from book where title = 'Alice In Wonderland'),
-- 	(select student_id from student where name = 'John'),
-- 	'2022-02-15'
-- ),
-- (
-- 	(select book_id from book where title = 'To kill a mockingbird'),
-- 	(select student_id from student where name = 'Bob'),
-- 	'2021-03-03'
-- ),
-- (
-- 	(select book_id from book where title = 'Alice In Wonderland'),
-- 	(select student_id from student where name = 'Lera'),
-- 	'2021-05-23'
-- ),
-- (
--     (select book_id from book where title = 'Harry Potter'),
--     (select student_id from student where name = 'Bob'),
--     '2021-08-12'
-- );

-- select * from book_library

-- select s.name, b.title 
-- from book_library as l
-- join student as s on l.student_id = s.student_id
-- join book as b on l.book_fk_id = b.book_id

-- select avg(s.age)
-- from book_library as l
-- join student as s on l.student_id = s.student_id
-- join book as b on l.book_fk_id = b.book_id
-- where b.title = 'Alice In Wonderland'

delete from Student as s
where s.name = 'John' 




