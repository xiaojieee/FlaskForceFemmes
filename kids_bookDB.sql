CREATE DATABASE Kids_booksDB;

use Kids_booksDB;

CREATE TABLE Books_list (
    BookID INT PRIMARY KEY,
    Title TEXT,
    Author TEXT,
    Genre TEXT,
    Pages INT,
    ReadingLevel TEXT
);
INSERT INTO Books (BookID, Title, Author, Genre, Pages, ReadingLevel)
VALUES
(1, 'Thorfinn and the putrid potion', 'David MacPhail', 'Adventure', 256, 'Book Band Lime'),
(2, 'The pearl in the ice', 'Cathryn Constable', 'Adventure', 240, 'Book Band Lime'),
(3, 'Max and the Midknights', 'Lincoln Peirce', 'Adventure', 288, 'Book Band Gold'),
(4, 'Bloom', 'Nicola Skinner', 'Fantasy', 288, 'Book Band Orange'),
(5, 'Evie and the animals', 'Matt Haig', 'Fantasy', 256, 'Book Band Gold'),
(6, 'The rusty rescue', 'Shane Hegarty', 'Fantasy', 288, 'Book Band Gold'),
(7, 'From the Ashes', 'Tom Palmer', 'Sport', 320, 'Book Band Lime'),
(8, 'Berlin Olympics', 'Vince Cross', 'Sport', 240, 'Book Band Gold'),
(9, 'The Unlucky Eleven', 'Phil Earle', 'Sport', 224, 'Book Band Gold'),
(10, 'Sam Wu is not afraid of zombies', 'Katie. & Kevin Tsang', 'Horror', 240, 'Book Band Lime'),
(11, 'The Bigwoof conspiracy', 'Dashe Roberts', 'Horror', 288, 'Book Band Gold'),
(12, 'Whoa! I spy a werewolf', 'Justin Davies', 'Horror', 288, 'Book Band Lime'),
(13, 'The Highland Falcon thief', 'MG Leonard & Sam Sedgman', 'Mystery', 352, 'Book Band Gold'),
(14, 'The catnap caper', 'Sarah Todd Taylor', 'Mystery', 160, 'Book Band Gold'),
(15, 'Mickey and the animal spies', 'Anne Miller', 'Mystery', 192, 'Book Band Gold'),
(16, 'How to be extraordinary', 'Rashmi Sirdeshpande', 'Non-Fiction', 320, 'Book Band Gold'),
(17, 'The big book of the UK', 'Imogen Russell Williams', 'Non-Fiction', 192, 'Book Band Gold'),
(18, 'Unusual pets', 'Pat Jacobs', 'Non-Fiction', 208, 'Book Band Gold'),
(19, 'Winging it', 'Laura Ellen Anderson', 'Graphic', 304, 'Book Band Gold'),
(20, 'Brawl of the wild', 'Dav Pilkey', 'Graphic', 256, 'Book Band Gold'),
(21, 'The mightiest chef in the universe!', 'James Stayte', 'Graphic', 288, 'Book Band Lime'),
(22, 'Be the change', 'Various', 'Poetry', 176, 'Book Band Gold'),
(23, 'How many points for a panda?', 'Hilda Offen', 'Poetry', 40, 'Book Band Gold'),
(24, 'A Caribbean dozen', 'Various', 'Poetry', 128, 'Book Band Gold'),
(25, 'Freckle Juice', 'Judy Blume', 'Classics', 64, 'Book Band Orange'),
(26, 'Hacker', 'Malorie Blackman', 'Classics', 400, 'Book Band Gold'),
(27, 'Worzel Gummidge', 'Barbara Eurphan Todd', 'Classics', 176, 'Book Band Gold'),
(28, 'Agent Weasel and the abominable Dr Snow', 'Nick East', 'Humour', 192, 'Book Band Gold'),
(29, 'The Taylor Turbochaser', 'David Baddiel', 'Humour', 400, 'Book Band Gold'),
(30, 'Trouble!', 'Alan MacDonald', 'Humour', 400, 'Book Band Gold');

SELECT * FROM Books_list;

CREATE TABLE Reading_progress (
    ChildID INT PRIMARY KEY AUTO_INCREMENT,
    AnimalAlias TEXT,
    BookID INT,
    Title TEXT,
    ReadingLevel TEXT,
    Genre TEXT,
    NumberOfPages INT,
    StartDate DATE,
    PagesReadToday INT,
    CompletedDate DATE
);

INSERT INTO Reading_progress (AnimalAlias, BookID, Title, ReadingLevel, Genre, NumberOfPages, StartDate, PagesReadToday, CompletedDate)
VALUES
('Ziggy the Zebra', 1, 'Thorfinn and the putrid potion', 'Book Band Lime', 'Adventure', 256, '2024-03-01', 13, '2024-03-20'),
('Leo the Lion', 4, 'Bloom', 'Book Band Orange', 'Fantasy', 288, '2024-03-05', 36, NULL),
('Polly the Penguin', 7, 'From the Ashes', 'Book Band Lime', 'Sport', 320, '2024-03-04', 56, '2024-03-30'),
('Benny the Bunny', 10, 'Sam Wu is not afraid of zombies', 'Book Band Lime', 'Horror', 240, '2024-03-07', 0, NULL),
('Sammy the Sloth', 13, 'The Highland Falcon thief', 'Book Band Gold', 'Mystery', 352, '2024-03-01', 34, NULL),
('Coco the Chameleon', 16, 'How to be extraordinary', 'Book Band Gold', 'Non-Fiction', 320, '2024-03-01', 5, '2024-04-01'),
('Gigi the Giraffe', 19, 'Winging it', 'Book Band Gold', 'Graphic', 304, '2024-03-07', 22, NULL),
('Rocky the Raccoon', 22, 'Be the change', 'Book Band Gold', 'Poetry', 176, '2024-03-05', 48, '2024-04-02'),
('Lily the Llama', 25, 'Freckle Juice', 'Book Band Orange', 'Classics', 64, '2024-03-01', 0, '2024-04-03'),
('Freddie the Fox', 28, 'Agent Weasel and the abominable Dr Snow', 'Book Band Gold', 'Humour', 192, '2024-03-04', 45, '2024-04-03');

SELECT * FROM Reading_progress;

CREATE TABLE Completed_reading (
    ChildID INT,
    AnimalAlias TEXT,
    BookID INT,
    Title TEXT,
    ReadingLevel TEXT,
    CompletedDate DATE
);
INSERT INTO Completed_reading (ChildID, AnimalAlias, BookID, Title, ReadingLevel, CompletedDate)
VALUES
(1, 'Ziggy the Zebra', 6, 'The rusty rescue', 'Book Band Gold', '2024-03-01'),
(1, 'Ziggy the Zebra', 2, 'The pearl in the ice', 'Book Band Lime', '2024-03-03'),
(1, 'Ziggy the Zebra', 3, 'Max and the Midknights', 'Book Band Gold', '2024-03-06'),
(2, 'Leo the Lion', 5, 'Evie and the animals', 'Book Band Gold', '2024-03-09'),
(2, 'Leo the Lion', 3, 'Max and the Midknights', 'Book Band Gold', '2024-03-11'),
(2, 'Leo the Lion', 6, 'The rusty rescue', 'Book Band Gold', '2024-03-13'),
(3, 'Polly the Penguin', 15, 'Mickey and the animal spies', 'Book Band Gold', '2024-03-15'),
(3, 'Polly the Penguin', 20, 'Brawl of the wild', 'Book Band Gold', '2024-03-18'),
(3, 'Polly the Penguin', 30, 'Trouble!', 'Book Band Gold', '2024-03-20'),
(4, 'Benny the Bunny', 4, 'Bloom', 'Book Band Orange', '2024-03-22'),
(4, 'Benny the Bunny', 16, 'How to be extraordinary', 'Book Band Gold', '2024-03-25'),
(5, 'Sammy the Sloth', 30, 'Trouble!', 'Book Band Gold', '2024-03-27'),
(5, 'Sammy the Sloth', 24, 'A Caribbean dozen', 'Book Band Gold', '2024-03-30'),
(6, 'Coco the Chameleon', 23, 'How many points for a panda?', 'Book Band Gold', '2024-02-02'),
(6, 'Coco the Chameleon', 14, 'The catnap caper', 'Book Band Gold', '2024-02-04'),
(7, 'Gigi the Giraffe', 3, 'Max and the Midknights', 'Book Band Gold', '2024-02-07'),
(8, 'Rocky the Raccoon', 27, 'Worzel Gummidge', 'Book Band Gold', '2024-02-10'),
(8, 'Rocky the Raccoon', 13, 'The Highland Falcon thief', 'Book Band Gold', '2024-02-12'),
(9, 'Lily the Llama', 28, 'Agent Weasel and the abominable Dr Snow', 'Book Band Gold', '2024-02-14'),
(10, 'Freddie the Fox', 12, 'Whoa! I spy a werewolf', 'Book Band Lime', '2024-02-17'),
(10, 'Freddie the Fox', 6, 'The rusty rescue', 'Book Band Gold', '2024-02-19'),
(10, 'Freddie the Fox', 30, 'Trouble!', 'Book Band Gold', '2024-02-21');

SELECT * FROM Completed_reading;