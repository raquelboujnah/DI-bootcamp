create table menu_items(
id_item serial primary key,
name_item varchar(30) not null,
price_item smallint default 0
);