-- exercise-1
-- select rating, count(*) as film_count
-- from film
-- group by rating
-- order by rating

-- select * from film 
-- where (rating = 'G' or rating = 'PG-13')
-- and length < 120 
-- and rental_rate < 3.00
-- order by title

-- update customer
-- set first_name = 'Raquel',
-- 	last_name = 'Boujnah',
-- 	email = 'raquelboujnah@gmail.com'
-- where first_name = 'Mary'

-- exercise -2
-- create table students (
--     id SERIAL PRIMARY KEY,
--     last_name VARCHAR(50),
--     first_name VARCHAR(50),
--     birth_date DATE
-- );
-- insert into students (first_name, last_name, birth_date)
-- values
--     ('Marc', 'Benichou', '02/11/1998'),
--     ('Yoan', 'Cohen', '03/12/2010'),
--     ('Lea', 'Benichou', '27/07/1987'),
--     ('Amelia', 'Dux', '  07/04/1996'),
--     ('David', 'Grez', '14/06/2003'),
--     ('Omer', 'Simpson', '03/10/1980');

-- update students
-- set birth_date = '1998-11-02'
-- where last_name = 'Benichou'

--  update students
--  set last_name = 'Guez'
--  where last_name = 'Grez'
 
--  delete from students
--  where first_name = 'Lea'
 
-- select count(*) from students

-- select count(*) from students where birth_date > '2000-01-01'

-- alter table students
-- add column math_grade integer

-- update students
-- set math_grade = 80
-- where id = 1;

-- update students
-- set math_grade = 90
-- where id = 2 or id = 4

-- select * from students

-- update students
-- set math_grade = 40
-- where id = 6;

-- select count(*) from students where math_grade < 83

-- insert into students(first_name, last_name, birth_date, math_grade)
-- values
-- ('Omer', 'Simpson', '1980-10-03', 70)

-- select sum(math_grade) from students


 