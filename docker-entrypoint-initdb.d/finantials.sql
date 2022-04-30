CREATE TABLE IF NOT EXISTS accounts (
   accountNumber INT,
    accountType VARCHAR(13) ,
    balance NUMERIC(10, 2),
    blockDirectEntries VARCHAR(5) ,
    debitCredit ENUM ('debit', 'credit') ,
   name VARCHAR(44) ,
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