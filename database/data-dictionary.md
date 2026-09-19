# Data Dictionary 

## Customers 
1) customer_id = Unique ID for each customer -- INTEGER (PRIMARY KEY)
2) customer_name = Customers' name -- VARCHAR(100)
3) phone = Customers' phone number -- VARCHAR(30)
4) email = Customers' email -- VARCHAR(150)
5) city = Customers' city -- VARCHAR(100)
6) country = Customers' country -- VARCHAR(100)
7) customer_type = Type of customer -- VARCHAR(50)
8) status = Active or Inactive -- VARCHAR(20) -- NOT NULL
9) created_at = Data the customer record was created -- TIMESTAMP -- NOT NULL 

## Products 
1) product_id = Unique ID for each product -- INTEGER - PRIMARY KEY 
2) product_name = Product's name -- VARCHAR(150) -- NOT NULL
3) category = Product category -- VARCHAR(150) -- NOT NULL
4) unit_price = Price of each unit -- VARCHAR(100) - NOT NULL
5) stock_quantity = Current quantity in stock - INTEGER - NOT NULL
6) supplier_id = ID of the vendor supplying the product -- INTEGER -- FOREIGN KEY
7) status = active or inactive -- VARCHAR(20)
8) created_at = Date the product record was created -- TIMESTAMP

## Vendors
1) vendor_id = Unique id for each vendor -- INTEGER -- PRIMARY KEY 
2) vendor_name = Vendor's name -- VARCHAR(150) - NOT NULL
3) contact_name = Main contact person's name -- VARCHAR(100)
4) phone = Vendor's phone number -- VARCHAR(30) 
5) email = Vendor's email -- VARCHAR(150)
6) city = Vendor's city -- VARCHAR(150)
7) status = Active or Inactive -- VARCHAR(20) NOT NULL

## Sales 
1) sales_id = Unique id for sales -- INTEGER -- PRIMARY KEY 
2) customer_id = ID of the customer who made the purchase -- INTEGER -- FOREIGN KEY 
3) product_id = ID of the product that was sold -- INTEGER -- FOREIGN KEY
4) quantity = Number of units sold -- INTEGER -- NOT NULL
5) unit_price = Price per unit at the time of sale -- DECIAML(12,2) -- NOT NULL
6) sale_date = Date of the sale -- DATE -- NOT NULL 
7) sales_channel = Channel through which the sales occured -- VARCHAR(50) -- NOT NULL

