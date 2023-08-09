create table Books(
id int identity(1,1) not null,
name varchar(150) not null,
author varchar(150) not null,
constraint PK_Books primary key (id) 
)


insert into [Books] values
('Fox', 'Antonio'),
('Rose', 'Toninho'),
('Prince', 'Tonhão')