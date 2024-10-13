""" DBMS """

-- Create Table and Retrieve Books Published After 2000
-- Question Text:

-- Create a table named Books with the following columns:
--           BookID (INT, Primary Key, Auto Increment)
--           Title (VARCHAR)
--           Author (VARCHAR)
--           Genre (VARCHAR)
--           YearPublished (INT)

-- After creating the table, insert the following books:

--        "The Alchemist" | "Paulo Coelho" | "Fiction" | 1988
--        "The Da Vinci Code" | "Dan Brown" | "Fiction" | 2003

-- Write a SQL query to retrieve all books published after the year 2000.

-- Constraint
-- The table should be created from scratch.
-- The query should return the BookID, Title, Author, and YearPublished columns.

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(255) NOT NULL,
    YearPublished INT NOT NULL
);

INSERT INTO Books (Title, Author, Genre, YearPublished)
VALUES 
    ('The Alchemist', 'Paulo Coelho', 'Fiction', 1988),
    ('The Da Vinci Code', 'Dan Brown', 'Fiction', 2003);
    
SELECT BookID, Title, Author, YearPublished
FROM Books
WHERE YearPublished > 2000;