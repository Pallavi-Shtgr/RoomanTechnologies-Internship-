""" DBMS """

-- Create a table named Books with the following columns:
--           BookID (INT, Primary Key, Auto Increment)
--           Title (VARCHAR)
--           Author (VARCHAR)
--           Genre (VARCHAR)
--           YearPublished (INT)

-- After creating the table, insert the following book:
--             "The Alchemist" | "Paulo Coelho" | "Fiction" | 1988

-- Write a SQL query to retrieve the book with  BookID = 1 

-- Write a SQL query to update the genre of the book with BookID = 1 to "Adventure".

-- Write a SQL query to retrieve the book with  BookID = 1 It should output the book details with updated genre value

-- Constraint
-- The table should be created from scratch.
-- Ensure that the BookID = 1 exists before updating the genre.
-- The genre must be a valid non-empty string.

CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Genre VARCHAR(100),
    YearPublished INT
);

INSERT INTO Books (Title, Author, Genre, YearPublished)
VALUES ('The Alchemist', 'Paulo Coelho', 'Fiction', 1988);

SELECT * FROM Books
WHERE BookID = 1;

UPDATE Books
SET Genre = 'Adventure'
WHERE BookID = 1;


SELECT * FROM Books
WHERE BookID = 1;
