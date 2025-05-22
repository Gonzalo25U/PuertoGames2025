CREATE DATABASE PuertoGames2025;
GO

USE PuertoGames2025;
GO

CREATE TABLE Plataforma (
    IDPlataforma INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(50)
);

CREATE TABLE Videojuego (
    IDVideojuego INT PRIMARY KEY IDENTITY(1,1),
    Titulo NVARCHAR(100),
    Precio DECIMAL(10, 2),
	Stock INT,
    IDPlataforma INT,
    FOREIGN KEY (IDPlataforma) REFERENCES Plataforma(IDPlataforma)
);

INSERT INTO Plataforma (Nombre) 
VALUES 
('PlayStation 5 (PS5)'),('Xbox Series X/S'),('Nintendo Switch'),('PC (Windows)'),('PlayStation 4 (PS4)'),
('Xbox One'),('Nintendo 3DS'),('PlayStation Vita'),('Xbox 360'),('Wii U'),('Nintendo Wii'),('PC (MacOS)'),
('Google Stadia'),('Oculus Quest (VR)'),('Sega Genesis'),('PlayStation 2');


INSERT INTO Videojuego (Titulo, Precio, Stock, IDPlataforma) VALUES
('The Last of Us Part II', 59.99, 10, 1),
('Spider-Man: Miles Morales', 49.99, 15, 1),
('Demon’s Souls', 69.99, 20, 1),
('Halo Infinite', 59.99, 12, 2),
('Forza Horizon 5', 59.99, 25, 2),
('Gears 5', 39.99, 30, 2),
('The Legend of Zelda: Breath of the Wild', 59.99, 8, 3),
('Super Mario Odyssey', 49.99, 18, 3),
('Animal Crossing: New Horizons', 49.99, 22, 3),
('Minecraft', 29.99, 50, 4),
('The Witcher 3: Wild Hunt', 39.99, 12, 4),
('Cyberpunk 2077', 59.99, 10, 4),
('Final Fantasy VII Remake', 59.99, 7, 5),
('Gran Turismo 7', 69.99, 20, 5),
('Grand Theft Auto: San Andreas', 29.99, 10, 31),
('Gran Turismo 4', 19.99, 15, 31),
('Metal Gear Solid 3: Snake Eater', 24.99, 12, 31),
('Shadow of the Colossus', 21.99, 8, 31),
('God of War II', 22.99, 14, 31),
('Final Fantasy X', 18.99, 11, 31),
('God of War: Ragnarok', 69.99, 30, 5),
('Minecraft Dungeons', 29.99, 18, 6),
('FIFA 22', 49.99, 28, 6),
('Red Dead Redemption 2', 59.99, 12, 7),
('Pokémon Sword', 49.99, 15, 7),
('Pokémon Shield', 49.99, 10, 7),
('Super Smash Bros. Ultimate', 59.99, 25, 7),
('Luigi’s Mansion 3', 49.99, 9, 7),
('The Elder Scrolls V: Skyrim', 39.99, 5, 8),
('Uncharted 4: A Thief’s End', 59.99, 13, 8),
('LittleBigPlanet 3', 39.99, 12, 8),
('Red Dead Redemption', 39.99, 15, 9),
('Super Mario Bros. U Deluxe', 49.99, 22, 9),
('Donkey Kong Country: Tropical Freeze', 49.99, 18, 9),
('Overwatch', 39.99, 20, 10),
('Super Smash Bros. Ultimate', 59.99, 28, 10),
('Zelda: Link’s Awakening', 49.99, 16, 10),
('The Legend of Zelda: Skyward Sword HD', 59.99, 14, 11),
('Hollow Knight', 19.99, 30, 11),
('Nier: Automata', 49.99, 18, 12),
('Dark Souls III', 49.99, 22, 12),
('Elden Ring', 69.99, 12, 12),
('Call of Duty: Warzone', 0.00, 40, 13),
('Madden NFL 22', 59.99, 30, 13),
('NBA 2K22', 59.99, 35, 13),
('Half-Life: Alyx', 59.99, 8, 14),
('Beat Saber', 29.99, 15, 14),
('The Walking Dead: Saints & Sinners', 39.99, 9, 14),
('Resident Evil Village', 59.99, 20, 15),
('BioShock Infinite', 29.99, 25, 15),
('Borderlands 3', 59.99, 10, 15),
('Horizon Zero Dawn', 59.99, 7, 1),
('Uncharted: The Lost Legacy', 49.99, 13, 5),
('Spider-Man', 59.99, 18, 5),
('The Division 2', 39.99, 15, 2),
('Far Cry 5', 39.99, 20, 9),
('Watch Dogs: Legion', 49.99, 25, 4);
('Resident Evil 4', 20.99, 13, 31),
('Devil May Cry 3: Dante''s Awakening', 17.99, 9, 31),
('Kingdom Hearts', 23.99, 7, 31),
('Pro Evolution Soccer 6', 16.99, 20, 31);

