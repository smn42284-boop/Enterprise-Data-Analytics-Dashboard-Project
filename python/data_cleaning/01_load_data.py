import pandas as pd
import psycopg2

## connecting with postgresql database
connection = psycopg2.connect(
    host="localhost",
    database="enterprise_master_data",
    user="postgres",
    password="1a!2s@3d#4f$",
)
customers = pd.read_sql("SELECT * FROM customers", connection)
print(customers)
connection.close()
## getting some examples
print(customers.head())
print(customers.info())
print(customers.isnull().sum())
## finding customers with missing emails
missing_email = customers[customers["email"].isnull()]
print(missing_email)

## finding duplicated customers
duplicates = customers[
    customers.duplicated(subset=["customer_name", "phone"], keep=False)
]

print(duplicates)

## products table
products = pd.read_sql("SELECT * FROM products", connection)

invalid_prices = products[products["unit_price"] < 0]

print(invalid_prices)

invalid_stock = products[products["stock_quantity"] < 0]

print(invalid_stock)
