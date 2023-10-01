-- select name from language

-- select f.title, f.description, l.name 
-- from film as f
-- join language as l on f.language_id = l.language_id;

-- select f.title, f.description, l.name
-- from language as l 
-- left join film as f on l.language_id = f.language_id;

-- create table new_film(
-- 	new_film_id serial primary key,
-- 	name varchar(50)
-- );

-- insert into new_film(name)
-- values
-- ('Ratatouille'),
-- ('Le cinquieme element'),
-- ('Amelie poulain');

-- create table customer_review(
-- 	review_id serial primary key,
--  new_film_id integer,
-- 	language_id integer,
-- 	score integer check(score between 1 and 10),
-- 	review_text text,
-- 	last_update date,
	
--  foreign key (new_film_id) references new_film(new_film_id) on delete cascade,
-- 	foreign key (language_id) references language(language_id) on delete cascade
-- );

-- insert into customer_review(new_film_id, language_id, score, review_text, last_update)
-- values
-- (
-- 	(select new_film_id from new_film where name = 'Ratatouille'),
-- 	(select language_id from language where name = 'French'),
-- 	9,
-- 	'Encore et toujours, Pixar écrase la concurrence, et ce, non seulement enplaçant la barre toujours plus haut, mais aussi en prenant son public au sérieux.
-- 	Avec "Ratatouille", le studio nous offre une fois de plus un chef-doeuvre.
-- 	Epoustoufflant sur le plan visuel, "Ratatouille", ésurpassant tous ses prédécesseurs, nous en met plein la vue avec ses superbes images.
-- 	Ajoutez à cela une originalité constante et un humour savoureux qui plaira à tous; que demander de plus?',
-- 	'2023-09-20'
-- ),
-- (
-- 	(select new_film_id from new_film where name = 'Le cinquieme element'),
-- 	(select language_id from language where name = 'English'),
-- 	8,
-- 	'As irresistible—if occasionally annoying—popcorn-munching escapism, The Fifth Element remains an experience of diversionary entertainment, and almost exclusively about rehashing previously explored surfaces with a new sheen.',
-- 	'2022-08-22'
-- );

-- delete from new_film where name = 'Ratatouille'
-- select * from customer_review

-- update film as f
-- set language_id = 5
-- where f.title = 'Alice Fantasia'

-- drop table customer_review

-- select count(*)
-- from rental
-- where return_date is NULL or return_date > current_date;

-- select f.title, f.rental_rate 
-- from film as f
-- inner join inventory as i on f.film_id = i.film_id
-- left join rental as r on i.inventory_id = r.inventory_id
-- where r.return_date is NULL or r.return_date > current_date
-- order by f.rental_rate desc
-- limit 30

-- select f.title, a.actor_id, a.first_name, a.last_name, f.description
-- from film as f
-- inner join film_actor as fa on f.film_id = fa.film_id
-- inner join actor as a on fa.actor_id = a.actor_id
-- where (a.first_name = 'Penelope' and a.last_name = 'Monroe')
-- 	and lower(f.description) LIKE '%sumo wrestler%';
	
-- select * from film 
-- where length < 60 
-- 	and rating = 'R';

-- select f.title
-- from film as f
-- inner join inventory as i on f.film_id = i.film_id
-- inner join rental as r on i.inventory_id = r.inventory_id
-- inner join customer as c on r.customer_id = c.customer_id
-- where c.first_name = 'Matthew'
--   and c.last_name = 'Mahan'
--   and f.rental_rate > 4.00
--   and r.return_date between '2005-07-28' and '2005-08-01';

-- select f.title, f.description, f.replacement_cost
-- from film as f
-- inner join inventory as i on f.film_id = i.film_id
-- inner join  rental as r on i.inventory_id = r.inventory_id
-- inner join customer as c on r.customer_id = c.customer_id
-- where c.first_name = 'Matthew'
--   and c.last_name = 'Mahan'
--   and (lower(f.title) like '%boat%' or lower(f.description) like '%boat%')
--   and f.replacement_cost > 16;

