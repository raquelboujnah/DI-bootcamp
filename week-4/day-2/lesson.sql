-- create table countries (
-- 	id serial primary key,
-- 	name_country varchar(50)
-- );

-- insert into countries(name_country)
-- values
-- ('USA'),
-- ('France');

create table movies(
	movie_id serial primary key,
	movie_title varchar(50) not null,
	movie_story text,
	
	country_id integer,
	
	foreign key(country_id) references countries(id)
);