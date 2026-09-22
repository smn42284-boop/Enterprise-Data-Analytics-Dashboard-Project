import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()
db_url = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(db_url)

customers = pd.read_sql("SELECT * FROM customers", engine)

## checking length of the database

print(len(customers))

## data quality check

missing_email = customers[customers["email"].isnull()]
print(missing_email)

duplicate_customers = customers[
    customers.duplicated(subset=["customer_name", "phone"], keep=False)
]

## Loading products

products = pd.read_sql("SELECT * FROM products", engine)

invalid_price = products[products["unit_price"] < 0]

invalid_stock = products[products["stock_quantity"] < 0]

vendors = pd.read_sql("SELECT * FROM vendors", engine)

inactive_vendors = vendors[vendors["status"] == "Inactive"]

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
print("Inactive vendors: ", len(inactive_vendors))
print("Products from inactive vendors: ", len(inactive_supplier_products))

## Loading sales

sales = pd.read_sql("SELECT * FROM sales", engine)
sales_customer = sales.merge(
    customers, on="customer_id", how="left", suffixes=("_sales", "_customer")
)
invalid_sales_customers = sales_customer[sales_customer["customer_name"].isnull()]
print(invalid_sales_customers)
