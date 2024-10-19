""" DBMS """

-- Create a table named Books with the following columns:
-- 1) BookID (INT, Primary Key, Auto Increment)
-- 2) Title (VARCHAR)
-- 3) Author (VARCHAR)
-- 4) Genre (VARCHAR)
-- 5) YearPublished (INT)
-- After creating the table, write a SQL query to insert a new book with the following details:
-- 1. Title: "The Alchemist"
-- 2. Author: "Paulo Coelho"
-- 3. Genre: "Fiction"
-- 4. Year Published: 1988

-- Write a SQL query to retrieve all books

-- Constraint
-- The table should be created from scratch.
-- The BookID should be auto-incremented.
-- All columns must be non-empty when inserting a new book.

CREATE table BOOKS(
    BookID INT AUTO_INCREMENT PRIMARY KEY, 
    Title VARCHAR(255) NOT NULL, 
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(255) NOT NULL,
    YearPublished INT NOT NULL
    );

insert into BOOKS(Title,Author,Genre,YearPublished)
Values('The Alchemist','Paulo Coelho','Fiction',1988);