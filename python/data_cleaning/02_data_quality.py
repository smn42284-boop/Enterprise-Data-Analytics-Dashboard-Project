import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def generate_data_quality_checks():

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

    inactive_customers = customers[customers["status"] == "Inactive"]

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
    ## Loading sales

    sales = pd.read_sql("SELECT * FROM sales", engine)
    sales_customer = sales.merge(
        customers, on="customer_id", how="left", suffixes=("_sales", "_customer")
    )
    invalid_sales_customers = sales_customer[sales_customer["customer_name"].isnull()]
    sales_product = sales.merge(
        products, on="product_id", how="left", suffixes=("_sales", "_product")
    )
    invalid_sales_products = sales_product[sales_product["product_name"].isnull()]
    invalid_sales_quantity = sales[sales["quantity"] < 0]

    ## Final Reporting
    print("Missing customer emails: ", len(missing_email))
    print("Duplidated customers: ", len(duplicate_customers))
    print("Negative product prices: ", len(invalid_price))
    print("Negative product stocks: ", len(invalid_stock))
    print("Inactive vendors: ", len(inactive_vendors))
    print("Products from inactive vendors: ", len(inactive_supplier_products))
    print("Sales with invalid customers: ", len(invalid_sales_customers))
    print("Sales with invalid products:", len(invalid_sales_products))

    report = [
        {
            "check": "Missing customer emails",
            "issues": len(missing_email),
            "status": "PASS" if len(missing_email) == 0 else "REVIEW",
        },
        {
            "check": "Duplicate customers",
            "issues": len(duplicate_customers),
            "status": "PASS" if len(duplicate_customers) == 0 else "REVIEW",
        },
        {
            "check": "Negative product prices",
            "issues": len(invalid_price),
            "status": "PASS" if len(invalid_price) == 0 else "REVIEW",
        },
        {
            "check": "Negative product stock",
            "issues": len(invalid_stock),
            "status": "PASS" if len(invalid_stock) == 0 else "REVIEW",
        },
        {
            "check": "Inactive vendors",
            "issues": len(inactive_vendors),
            "status": "PASS" if len(inactive_vendors) == 0 else "REVIEW",
        },
        {
            "check": "Invalid supplier references",
            "issues": len(invalid_suppliers),
            "status": "PASS" if len(invalid_suppliers) == 0 else "REVIEW",
        },
        {
            "check": "Products from inactive vendors",
            "issues": len(inactive_supplier_products),
            "status": "PASS" if len(inactive_supplier_products) == 0 else "REVIEW",
        },
        {
            "check": "Inactive customers",
            "issues": len(inactive_customers),
            "status": "PASS" if len(inactive_customers) == 0 else "REVIEW",
        },
        {
            "check": "Sales with invalid customers",
            "issues": len(invalid_sales_customers),
            "status": "PASS" if len(invalid_sales_customers) == 0 else "REVIEW",
        },
        {
            "check": "Sales with invalid products",
            "issues": len(invalid_sales_products),
            "status": "PASS" if len(invalid_sales_products) == 0 else "REVIEW",
        },
        {
            "check": "Negative sales quantities",
            "issues": len(invalid_sales_quantity),
            "status": "PASS" if len(invalid_sales_quantity) == 0 else "REVIEW",
        },
    ]

    report_df = pd.DataFrame(report)
    report_df.to_csv("../output/data_quality_report.csv", index=False)
    return report_df


report = generate_data_quality_checks()
review_row = report[report["status"] == "REVIEW"]
review_count = len(review_row)
pass_row = report[report["status"] == "PASS"]
pass_count = len(pass_row)
total_checks = len(report)
quality_percentage = pass_count / total_checks * 100
print(quality_percentage)
summary = {
    "total_checks": total_checks,
    "passed": pass_count,
    "needs_review": review_count,
    "quality_percentage": quality_percentage,
}
summary_df = pd.DataFrame([summary])
summary_df.to_csv("../output/data_summary_output.csv", index=False)
