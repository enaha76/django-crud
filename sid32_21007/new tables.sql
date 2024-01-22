use myinpc;

-- Create ProductFamily Table
CREATE TABLE ProductFamily (
    ProductFamilyID INT PRIMARY KEY,
    FamilyName VARCHAR(255),
    Description TEXT
);

-- Create Product Table
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    ProductDescription TEXT,
    ProductFamilyID INT,
    FOREIGN KEY (ProductFamilyID) REFERENCES ProductFamily(ProductFamilyID)
);

-- Create Basket Table
CREATE TABLE Basket (
    BasketID INT PRIMARY KEY,
    UserID INT,
    PurchaseDate DATE
);

-- Create Price Table
CREATE TABLE Price (
    PriceID INT PRIMARY KEY,
    ProductID INT,
    PriceAmount DECIMAL(10, 2),
    Currency VARCHAR(3),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Create Ponderation Table
CREATE TABLE Ponderation (
    PonderationID INT PRIMARY KEY,
    ProductID INT UNIQUE,
    ImportanceScore INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Create SellingPoint Table
CREATE TABLE SellingPoint (
    SellingPointID INT PRIMARY KEY,
    ProductID INT,
    PointDescription TEXT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
