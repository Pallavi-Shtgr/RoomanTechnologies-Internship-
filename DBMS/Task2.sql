-- In MySQL, a primary key automatically creates a clustered index. Ensure that CustomerID is set as the primary key in the Customers table.
-- • To create a primary key on the CustomerID column, you can use the following syntax: ALTER TABLE Customers ADD PRIMARY KEY (CustomerID);
-- • Non-clustered indexes can be created using the syntax: CREATE INDEX IX_Products_ProductName ON Products (ProductName);
-- • Check if the Customers and Products tables already have the necessary columns before creating indexes.
-- • If the CustomerID column is already a primary key, there is no need to create a clustered index explicitly; it is implicitly created by the primary key.

-- Step 1: Ensure the Customers Table Exists
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT NOT NULL,
    CustomerName VARCHAR(50),
    CustomerAddress VARCHAR(50),
    PRIMARY KEY (CustomerID)  -- Automatically creates a clustered index
);

-- Step 2: Ensure the Products Table Exists
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT NOT NULL,
    ProductName VARCHAR(50),
    PRIMARY KEY (ProductID)  -- Automatically creates a clustered index
);

-- Step 3: Insert Data into Customers Table (if not already inserted)
INSERT INTO Customers (CustomerID, CustomerName, CustomerAddress) 
VALUES 
(1, 'Alice', '123 Maple Street'),
(2, 'Bob', '456 Oak Avenue'),
(3, 'Charlie', '789 Pine Road')
ON DUPLICATE KEY UPDATE 
    CustomerName = VALUES(CustomerName),
    CustomerAddress = VALUES(CustomerAddress);

-- Step 4: Insert Data into Products Table (if not already inserted)
INSERT INTO Products (ProductID, ProductName) 
VALUES 
(1, 'Laptop'),
(2, 'Smartphone'),
(3, 'Headphones')
ON DUPLICATE KEY UPDATE 
    ProductName = VALUES(ProductName);

-- Step 5: Add a Non-Clustered Index on ProductName in the Products Table
CREATE INDEX IX_Products_ProductName 
ON Products (ProductName);

-- Step 6: Verify the Existence of CustomerID in Customers Table
SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Customers' AND COLUMN_NAME = 'CustomerID';

-- Step 7: Verify the Existence of ProductName in Products Table
SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Products' AND COLUMN_NAME = 'ProductName';

-- Step 8: Confirm Indexes for Customers Table
SHOW INDEX FROM Customers;

-- Step 9: Confirm Indexes for Products Table
SHOW INDEX FROM Products;