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