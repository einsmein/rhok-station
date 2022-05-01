CREATE TABLE IF NOT EXISTS accounts (
   accountNumber INT,
    accountType VARCHAR(255) ,
    balance NUMERIC(10, 2),
    blockDirectEntries VARCHAR(255) ,
    debitCredit VARCHAR(255) ,
   name VARCHAR(255)
);

CREATE TABLE projects (
   number             INTEGER 
  ,name               VARCHAR(255)
  ,projectGroupNumber Integer 
  ,customerNumber     INTEGER 
  ,isClosed           boolean
  ,mileage            Integer 
  ,isBarred           boolean
  ,isMainProject      boolean
  ,isMileageInvoiced  boolean
  ,lastUpdated        timestamp
  ,description        VARCHAR(255)
  ,deliveryDate       timestamp
  ,contactPersonId    Integer 
  ,objectVersion      VARCHAR(255)
);

CREATE TABLE departments(
   number           INTEGER  NOT NULL PRIMARY KEY 
  ,name             VARCHAR(255) NOT NULL
);