-- create table students (
-- 	id serial primary key,
-- 	first_name varchar,
-- 	last_name varchar(20),
-- 	birth_date date
-- );

-- insert into students(first_name, last_name, birth_date)
-- values
-- ('Marc', 'Benichou', '1998/11/02/'),
-- ('Yoan', 'Cohen', '2010/12/03'),
-- ('Lea', 'Benichou', '1987/07/27'),
-- ('Amelia', 'Dux', '1996/04/07'),
-- ('David', 'Grez', '2003/06/14'),
-- ('Omer', 'Simpson', '1980/10/03')
-- ;

-- insert into students(first_name, last_name, birth_date)
-- values
-- ('Raquel', 'Boujnah', '2001/08/22')
-- ;

-- select * from students
-- select * from students where first_name = 'Marc' and last_name = 'Benichou'
-- select * from students where first_name = 'Marc' or last_name = 'Benichou'
-- select * from students where first_name like '%a%'
-- select * from students where first_name like 'A%'
-- select * from students where first_name like '%a'
-- select * from students where first_name like '%_a%'
-- select * from students where id = 1 or id = 3
-- select * from students where birth_date = '2000-01-01' or birth_date > '2000-01-01' 

-- exercise-XP-GOLD
-- select * from students where id < 5 order by last_name
-- select * from students where birth_date = (select min(birth_date) from students)
-- select * from students where id > 2 and id < 6