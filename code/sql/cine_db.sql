drop database if exists cine_db;
create database if not exists cine_db;

use cine_db;

create table if not exists Usuario(
	Id_Usuario int not null auto_increment,
    Nombre varchar(75) not null,
    Email varchar(30) not null,
    Num varchar(10) not null,
    password varchar(8) not null,
    primary key (Id_Usuario)
)ENGINE = INNODB;

create table if not exists Administrador(
	Id_Administrador int not null auto_increment,
    Nombre varchar(75) not null,
    Email varchar(30) not null,
    Num varchar(10) not null,
    password varchar(8) not null,
    primary key (Id_Administrador)
)ENGINE = INNODB;

create table if not exists Pelicula(
	Id_Pelicula int not null auto_increment,
	Titulo varchar(30) not null,
    Genero varchar(30) not null,
    Duracion varchar(30) not null,
    Idioma varchar(30) not null,
    primary key(Id_Pelicula)
)ENGINE = INNODB;

create table if not exists Sala(
	Id_Sala int not null auto_increment,
    Asientos int not null,
    Tipo varchar(30) not null,
    primary key (Id_Sala)
) ENGINE = INNODB;

create table if not exists Butaca(
	Id_Butaca int not null UNIQUE,
    Estado bool not null,
    primary key (Id_Butaca)
) ENGINE = INNODB;

create table if not exists Funcion(
	Id_Funcion int not null auto_increment,
    Id_Pelicula int not null,
    Id_Sala int not null,
    fecha DATE not null,
    horario TIME not null,
	primary key(Id_Funcion),
    constraint fk_Funcion_Pelicula foreign key(Id_Pelicula)
		references Pelicula(Id_Pelicula)
        on delete cascade
        on update cascade,
	constraint fk_Funcion_Sala foreign key(Id_Sala)
		references Sala(Id_Sala)
        on delete cascade
        on update cascade
)ENGINE = INNODB;

create table if not exists Ticket(
	Id_Ticket int not null auto_increment,
    Id_Funcion int not null,
    Id_Usuario int not null,
    Id_Butaca int not null,
    primary key(Id_Ticket),
    constraint fk_Ticket_Funcion foreign key(Id_Funcion)
		references Funcion(Id_Funcion)
        on delete cascade
        on update cascade,
	constraint fk_Ticket_Usuario foreign key(Id_Usuario)
		references Usuario(Id_Usuario)
        on delete cascade
        on update cascade,
	constraint fk_Ticket_Butaca foreign key(Id_Butaca)
		references Butaca(Id_Butaca)
        on delete cascade
        on update cascade
)ENGINE = INNODB;

INSERT INTO administrador (`Nombre`, `Email`, `Num`, `password`) VALUES ('admin', 'admin@hotmail.com', '464', '1234');

INSERT INTO usuario (`Nombre`, `Email`, `Num`, `password`) VALUES ('usuario', 'usuario@hotmail.com', '464', '1234');
INSERT INTO usuario (`Nombre`, `Email`, `Num`, `password`) VALUES ('luis', 'luis@hotmail.com', '4641', '1234');
INSERT INTO usuario (`Nombre`, `Email`, `Num`, `password`) VALUES ('juan', 'juan@hotmail.com', '4642', '1234');

INSERT INTO pelicula (`Titulo`, `Genero`, `Duracion`, `Idioma`) VALUES ('Deadpool', 'Accion/Comedia', '1h 10 m', 'Español');
INSERT INTO pelicula (`Titulo`, `Genero`, `Duracion`, `Idioma`) VALUES ('Batman vs. Superman', 'Película de superhéroes', '3h 3 m', 'Español');
INSERT INTO pelicula (`Titulo`, `Genero`, `Duracion`, `Idioma`) VALUES ('Your Name', 'Anime/Drama', '1h 52 m', 'Japones');

INSERT INTO sala (`Asientos`, `Tipo`) VALUES ('100', '3D');
INSERT INTO sala (`Asientos`, `Tipo`) VALUES ('150', 'Normal');
INSERT INTO sala (`Asientos`, `Tipo`) VALUES ('100', 'iMax');

INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (1,1,'2020-05-26','14:30:00');
INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (1,1,'2020-05-26', '16:50:00');
INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (1,1,'2020-05-26', '17:50:00');

INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (2,1,'2020-05-28', '12:00:00');
INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (2,2,'2020-05-28', '12:30:00');
INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (2,3,'2020-05-29', '14:30:00');

INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (3,2,'2020-05-26', '13:30:00');
INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (3,1,'2020-05-26', '15:30:00');
INSERT INTO Funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (3,3,'2020-05-29', '12:30:00');

INSERT INTO  Butaca(`Id_Butaca`,`Estado`) VALUES (1,1);
INSERT INTO  Butaca(`Id_Butaca`,`Estado`) VALUES (2,1);
INSERT INTO  Butaca(`Id_Butaca`,`Estado`) VALUES (3,1);
INSERT INTO  Butaca(`Id_Butaca`,`Estado`) VALUES (4,1);

INSERT INTO Ticket(`Id_Funcion`,`Id_Usuario`,`Id_Butaca`) VALUES (1,1,1);
INSERT INTO Ticket(`Id_Funcion`,`Id_Usuario`,`Id_Butaca`) VALUES (2,2,2);
INSERT INTO Ticket(`Id_Funcion`,`Id_Usuario`,`Id_Butaca`) VALUES (3,3,1);



