# Data Quality Rules 

## Customer Data 
 
### Missing Customer Email

**Problem**
Somes customers do not have an email address 

**Rule**
Customer email should be provided when available 

**Detection**
Find customer records when email is NULL

**Action**
Flag the record for review. Do not create or guess an email address 

### Duplicated Customers 

**Problem**
Multiple customer records may represent the same customer
**Rule** 
Customer name and phone number should identify a unique customer record
**Detection**
Find record with the samme name and phone number 
**Action**
Flag the records for review before deciding whether thye should be merged or corrected. 

## Product Data 
### Negative Product Price 
**Problem**
A product has a negative unit price 
**Rule** 
Product unit price should be zero or greater 
**Detection**
Find products where unit price is less than 0 
**Action** 
Flag the product for review and verify the correct price. 

### Negative Stock Quantity 
**Problem**
A product has a negative stock quantity 
**Rule**
Stock quantity should be zero or greater 
**Detection**
Find products where stock quantity is less than 0 
**Action**
Flag the product for review and verify the inventory record 

### Invalid Supplier Reference 
**Problem**
A product may reference a supplier that does not exist in the vendor master 
**Rule** 
Every 'supplier id' in the product table should match existing 'vendor id'
**Detection**
Compare product supplier IDs with vendor IDs and identify products with no matching vendor
**Action**
Flag the product for review and verify the supplier information 

### Inactive Vendor 

**Problem**
A vendor may be marked as inactive but still exist in the vendor master data 
**Rule** 
Inactive vendors should be reviewed before used for new business transformation 

**Detection**
Find vendors where status = Inactive

**Action**
Flag the vendor for review. Do not automatically delete the vendor record. 

## Sales Data 

### Negative Sales Quantity 
**Problem** 
A sales transction may contain a negative quantity 
**Rules**
Sales quantity should be zero or greater 
**Detection**
Find sales records where quantity < 0 
**Action**
Flag the transaction for review and verify the orginal sales record
