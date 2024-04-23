CREATE DATABASE BOOK_TRACKER;


USE BOOK_TRACKER;


CREATE TABLE Author (
    Author_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100)
);

CREATE TABLE Genre (
    Genre_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100)
);

CREATE TABLE Reading_Level (
    Reading_Level_ID INT PRIMARY KEY AUTO_INCREMENT,
    Level VARCHAR(100)
);

-- Create Book_List table
CREATE TABLE Book_List (
    Book_ID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100),
    Author_ID INT, FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID),
    Genre_ID INT, FOREIGN KEY (Genre_ID) REFERENCES Genre(Genre_ID),
    Pages INT,
    Reading_Level_ID INT, FOREIGN KEY (Reading_Level_ID) REFERENCES Reading_Level(Reading_Level_ID),
    Book_image VARCHAR(255),
    Blurb VARCHAR(1000),
    Recommended Boolean NULL
);

CREATE TABLE Book_Author (
    Book_ID INT, FOREIGN KEY (Book_ID) REFERENCES Book_List(Book_ID),
    Author_ID INT, FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID)
);

select * FROM Book_list;

-- Create account_type table
CREATE TABLE Account_type (
    Account_type_id INT PRIMARY KEY AUTO_INCREMENT,
    Account_type VARCHAR(100)
);

select * FROM Account_type;

-- Create Account table
CREATE TABLE Account_ (
    Account_id INT PRIMARY KEY AUTO_INCREMENT,
	Account_type_id INT, FOREIGN KEY (Account_type_id) REFERENCES Account_type(Account_type_id),
    Username VARCHAR(100),
    Password_ VARCHAR(100),
    Reading_Level_ID INT NULL, FOREIGN KEY (Reading_Level_ID) REFERENCES Reading_Level(Reading_Level_ID)
);

select * FROM account_;

-- Create Reading_progress table
CREATE TABLE Reading_progress (
    Account_id INT, FOREIGN KEY (Account_id) REFERENCES Account_(Account_id),
    Book_ID INT, FOREIGN KEY (Book_ID) REFERENCES Book_List(Book_ID),
    Start_Date DATE NULL,
    Current_page INT NULL,
    Completed_Date DATE NULL,
	Rating ENUM('1', '2', '3', '4', '5') NULL,
    UNIQUE KEY unique_reading_progress (Account_id, Book_ID)
);

select * FROM reading_progress;




