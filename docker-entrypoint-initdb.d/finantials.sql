CREATE TABLE IF NOT EXISTS accounts (
   accountNumber INT PRIMARY KEY,
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

CREATE TABLE distributions(
   departmentalDistributionNumber INTEGER  NOT NULL PRIMARY KEY
  ,name                           VARCHAR(255) NOT NULL
  ,barred                         BOOLEAN NOT NULL
  ,distributionType               VARCHAR(255) NOT NULL
);

CREATE TABLE department_distribution(
   department INTEGER NOT NULL,
   distribution INTEGER NOT NULL,
   percentage INTEGER NOT NULL,
   FOREIGN KEY(department) 
   REFERENCES departments(number),
   FOREIGN KEY(distribution) 
   REFERENCES distributions(departmentalDistributionNumber),
   PRIMARY KEY(department,distribution)
);

CREATE TABLE entries(
   account                  INTEGER 
  ,amount                   NUMERIC(100,2)
  ,amountInBaseCurrency     NUMERIC(1000,1)
  ,currency                 VARCHAR(255)
  ,date                     DATE 
  ,dueDate                  DATE 
  ,departmentalDistribution INTEGER 
  ,entryNumber              INTEGER 
  ,text                     VARCHAR(255)
  ,entryType                VARCHAR(255)
  ,vatAccount               VARCHAR(255)
  ,voucherNumber            INTEGER 
  ,quantity1                INTEGER 
  ,quantity2                INTEGER 
  ,bookedInvoice            INTEGER 
  ,invoiceNumber            INTEGER
  ,FOREIGN KEY(account) 
   REFERENCES accounts(accountNumber)
  ,FOREIGN KEY(departmentalDistribution) 
   REFERENCES distributions(departmentalDistributionNumber)
);