import os
from dotenv import load_dotenv

load_dotenv()

import pandas as pd
import psycopg2

connection = psycopg2.connect(
    host="DB_HOST",
    database="DB_NAME",
    user="DB_USER",
    password="DB_PASSWORD",
)
customers = pd.read_sql("SELECT * FROM customers", connection)

## checking length of the database

print(len(customers))

## data quality check

missing_email = customers[customers["email"].isnull()]
print(missing_email)

duplicate_customers = customers[
    customers.duplicated(subset=["customer_name", "phone"], keep=False)
]

## Loading products

products = pd.read_sql("SELECT * FROM products", connection)

invalid_price = products[products["unit_price"] < 0]

invalid_stock = products[products["stock_quantity"] < 0]

vendors = pd.read_sql("SELECT * FROM vendors", connection)

inavtive_vendors = vendors[vendors["status"] == "Inactive"]

product_vendor = products.merge(
    vendors,
    left_on="supplier_id",
    right_on="vendor_id",
    how="left",
    suffixes=("_product", "_vendor"),
)

## checking products with invalid supplier references
invalid_suppliers = product_vendor[product_vendor["vendor_id"].isnull()]

## products whose vendor is inactive
inactive_supplier_products = product_vendor[
    product_vendor["status_vendor"] == "Inactive"
]
## Final Reporting
print("Missing customer emails: ", len(missing_email))
print("Duplidated customers: ", len(duplicate_customers))
print("Negative product prices: ", len(invalid_price))
print("Negative product stocks: ", len(invalid_stock))
print("Inactive vendors: ", len(inavtive_vendors))
print("Products from inactive vendors: ", len(inactive_supplier_products))
