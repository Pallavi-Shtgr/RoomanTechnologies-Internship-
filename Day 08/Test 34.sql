""" DBMS """

-- Create a table named Books with the following columns:
--            BookID (INT, Primary Key, Auto Increment)
--            Title (VARCHAR)
--            Author (VARCHAR)
--            Genre (VARCHAR)
--            YearPublished (INT)

-- After creating the table, insert the following books:
--            "The Alchemist" | "Paulo Coelho" | "Fiction" | 1988
--             "1984" | "George Orwell" | "Dystopian" | 1949

-- Write a SQL query to retrieve all books

-- Write a SQL query to delete the book with BookID = 2.

-- Write a SQL query to retrieve all books. It should return only one row with BookID = 1.
-- Constraint
-- The table should be created from scratch.
-- Ensure that the book with BookID = 2 exists before attempting to delete it.

CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Genre VARCHAR(255),
    YearPublished INT
);

INSERT INTO Books (Title, Author, Genre, YearPublished) VALUES 
('The Alchemist', 'Paulo Coelho', 'Fiction', 1988),
('1984', 'George Orwell', 'Dystopian', 1949);

SELECT * FROM Books;

SELECT *FROM Books
WHERE BooKID=2;

DELETE FROM Books where BookID =2;

SELECT *FROM BOOKS;