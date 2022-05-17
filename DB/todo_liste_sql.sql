create database if not exists TodoListe;
use TodoListe;

create table if not exists TodoItems
(
	item_ID int auto_increment primary key unique key,
    item_name varchar(64),
    item_description text,
    item_link text,
    item_date date,
    item_priority int
);

create table if not exists Projekte
(
    projekt_ID int auto_increment primary key unique key,
    projekt_name varchar(64),
    projekt_beschreibung text
);