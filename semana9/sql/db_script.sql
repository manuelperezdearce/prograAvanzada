CREATE database gameshark;
USE gameshark;

CREATE TABLE videojuego(
     id INT PRIMARY KEY auto_increment,
	 titulo VARCHAR(100),
	 genero VARCHAR(50),
	 clasificacion VARCHAR(20),
	 plataforma VARCHAR(50)
);

INSERT INTO videojuego (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES
 (1,'The Legend of Zelda: Breath of the Wild', 'Aventura', 'E10+', 'Nintendo Switch'),
 (2,'FIFA 22', 'Deportes', 'E', 'Multiplataforma'),
 (3,'Cyberpunk 2077', 'RPG', 'Mature', 'PC');
 
 select * from videojuego;