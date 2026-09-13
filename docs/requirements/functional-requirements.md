# Functional Requirements 

## 1. Customer Management 
### FR-CUST-001 — View Customers
The system shall allow users to view a list of customers.

### FR-CUST-002 — View Customer Details
The system shall allow users to view a customer's details, including name, phone, email, city, type, and status.

### FR-CUST-003 — Identify Customer Records
Each customer shall have a unique customer ID.

### FR-CUST-004 — Display Customer Status
The system shall display whether a customer is Active or Inactive.

## 2. Product Management 

### FR-PROD-001 — View Products
The system shall allow users to view a list of products.

### FR-PROD-002 — View Product Details
The system shall display product name, category, price, stock quantity, supplier, and status.

### FR-PROD-003 — Identify Products
Each product shall have a unique product ID.

### FR-PROD-004 — Display Product Status
The system shall display whether a product is Active or Inactive.

## 3. Vendor Management 

### FR-VEND-001 — View Vendors
The system shall allow users to view a list of vendors.

### FR-VEND-002 — View Vendor Details
The system shall display vendor name, contact name, phone, email, city, and status.

### FR-VEND-003 — Identify Vendors
Each vendor shall have a unique vendor ID.

### FR-VEND-004 — Display Vendor Status
The system shall display whether a vendor is Active or Inactive.
## 4. Sales Transactions

### FR-SALE-001 — View Sales
The system shall allow users to view sales transactions.

### FR-SALE-002 — View Sale Details
The system shall display customer, product, quantity, price, date, and sales channel.

### FR-SALE-003 — Identify Sales
Each sale shall have a unique sale ID.

### FR-SALE-004 — Link Sales Data
Each sale shall be linked to an existing customer and product.

## 5. Data Quality 
### FR-DQ-001 — Identify Missing Data
The system shall identify records with missing required information.

### FR-DQ-002 — Identify Duplicates
The system shall identify possible duplicate records.

### FR-DQ-003 — Identify Invalid Data
The system shall identify invalid or suspicious values.

### FR-DQ-004 — Display Data Quality Issues
The system shall allow users to view identified data quality issues.
## 6. System Navigation 
### FR-NAV-001 — Main Navigation
The system shall provide navigation to Customers, Products, Vendors, and Sales.

### FR-NAV-002 — Return to Main Page
The system shall allow users to return to the main page from each section.

## 7. Functional Functional Requirements 
### FR-FUT-001 — Data Cleaning
The system may later provide Python-based data cleaning tools.

### FR-FUT-002 — Analytics Dashboard
The system may later provide sales and business analytics.

### FR-FUT-003 — REST API
The system may later provide a REST API for communication between the frontend and database.

### FR-FUT-004 — Advanced Data Quality
The system may later provide automated data-quality checks and reporting.
