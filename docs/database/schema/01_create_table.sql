-- Enterprise Master Data & Analytics Dashboard
-- Stage 1: Database Schema

-- Customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(30),
    email VARCHAR(150),
    city VARCHAR(100),
    country VARCHAR(100),
    customer_type VARCHAR(50),
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL
);
-- Vendors
CREATE TABLE vendors (
    vendor_id INTEGER PRIMARY KEY,
    vendor_name VARCHAR(150) NOT NULL,
    contact_name VARCHAR(100),
    phone VARCHAR(30),
    email VARCHAR(150),
    city VARCHAR(100),
    status VARCHAR(20) NOT NULL
);
-- Products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100) NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    stock_quantity INTEGER NOT NULL,
    supplier_id INTEGER,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_products_vendor
        FOREIGN KEY (supplier_id)
        REFERENCES vendors(vendor_id)
);

-- Sales
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    sale_date DATE NOT NULL,
    sales_channel VARCHAR(50) NOT NULL,

    CONSTRAINT fk_sales_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_sales_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);