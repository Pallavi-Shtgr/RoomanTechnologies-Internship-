CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    CustomerAddress VARCHAR(50)
);
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50)
);

INSERT INTO Customers (CustomerID, CustomerName, CustomerAddress) 
VALUES 
(1, 'Alice', '123 Maple Street'),
(2, 'Bob', '456 Oak Avenue'),
(3, 'Charlie', '789 Pine Road');
INSERT INTO Products (ProductID, ProductName) 
VALUES 
(1, 'Laptop'),
(2, 'Smartphone'),
(3, 'Headphones');