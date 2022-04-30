CREATE TABLE IF NOT EXISTS accounts (
   accountNumber INT,
    accountType VARCHAR(13) ,
    balance NUMERIC(10, 2),
    blockDirectEntries VARCHAR(5) ,
    debitCredit ENUM ('debit', 'credit') ,
   name VARCHAR(44) ,   
);