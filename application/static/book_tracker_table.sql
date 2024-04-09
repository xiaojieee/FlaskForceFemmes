CREATE DATABASE BOOK_TRACKER;

USE BOOK_TRACKER;

-- Create Book_List table
CREATE TABLE Book_List (
    Book_ID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(100),
    Pages INT,
    Reading_Level VARCHAR(100),
    Book_image VARCHAR(255),
    Blurb VARCHAR(1000)
);

select * FROM Book_list;

-- Create account_type table
CREATE TABLE Account_type (
    Account_type_id INT PRIMARY KEY AUTO_INCREMENT,
    Account_type VARCHAR(100)
);

select * FROM account_type;

-- Create Account table
CREATE TABLE Account_ (
    Account_id INT PRIMARY KEY AUTO_INCREMENT,
	Account_type_id INT, FOREIGN KEY (Account_type_id) REFERENCES Account_type(Account_type_id),
    Username VARCHAR(100),
    Password_ VARCHAR(100)
);

select * FROM account_;

-- Create Reading_progress table
CREATE TABLE Reading_progress (
    Account_id INT, FOREIGN KEY (Account_id) REFERENCES Account_(Account_id),
    Book_ID INT, FOREIGN KEY (Book_ID) REFERENCES Book_List(Book_ID),
    Start_Date DATE,
    Current_page INT,
    Completed_Date DATE NULL
);

select * FROM reading_progress;




