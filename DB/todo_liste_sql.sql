create database if not exists TodoListe;
use TodoListe;

create table if not exists TodoItems
(
	item_ID int auto_increment primary key unique key,
    item_name varchar(64),
    item_description text,
    item_link text,
    item_datum date,
    item_priority int,
    item_ort text, 
    item_ziel text,
    item_field1 text,
    item_field2 text
);

create table if not exists Projekte
(
    projekt_ID int auto_increment primary key unique key,
    projekt_name varchar (64),
    projekt_beschreibung text,
    projekt_ziel text
);

create table if not exists Hausaufgaben
(
    aufgabe_ID int auto_increment primary key unique key,
    aufgabe_name varchar(64),
    aufgabe_fach varchar(32),
    aufgabe_angabe text,
    aufgabe_abgabeDatum date
);