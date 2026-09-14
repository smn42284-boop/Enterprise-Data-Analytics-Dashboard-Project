
ALTER TABLE customers
ALTER COLUMN created_at TYPE TIMESTAMP
USING CURRENT_DATE;

ALTER TABLE products
ALTER COLUMN created_at TYPE TIMESTAMP
USING CURRENT_DATE;

-- Customer seed data


-- ============================================
-- CUSTOMERS
-- ============================================

INSERT INTO customers (
    customer_id,
    customer_name,
    phone,
    email,
    city,
    country,
    customer_type,
    status,
    created_at
)
VALUES
(101, 'ABC Trading Co.', '09123456789', 'contact@abctrading.com', 'Yangon', 'Myanmar', 'Business', 'Active', '2026-01-10'),
(102, 'Golden Star Retail', '09234567890', 'info@goldenstar.com', 'Mandalay', 'Myanmar', 'Business', 'Active', '2026-01-15'),
(103, 'Mya Mya', '09345678901', 'myamya@email.com', 'Yangon', 'Myanmar', 'Individual', 'Active', '2026-02-01'),
(104, 'Shwe Retail Group', '09456789012', 'sales@shweretail.com', 'Naypyidaw', 'Myanmar', 'Business', 'Active', '2026-02-05'),

-- Intentional duplicate customer
(105, 'ABC Trading Co.', '09123456789', NULL, 'Yangon', 'Myanmar', 'Business', 'Active', '2026-02-10'),

(106, 'Mandalay Electronics', '09567890123', 'contact@mandalayelectronics.com', 'Mandalay', 'Myanmar', 'Business', 'Active', '2026-02-12'),
(107, 'Hlaing Retail', '09678901234', 'hlaingretail@email.com', 'Yangon', 'Myanmar', 'Business', 'Active', '2026-02-15'),
(108, 'Future Tech Myanmar', '09789012345', NULL, 'Yangon', 'Myanmar', 'Business', 'Inactive', '2026-02-20');


-- ============================================
-- VENDORS
-- ============================================

INSERT INTO vendors (
    vendor_id,
    vendor_name,
    contact_name,
    phone,
    email,
    city,
    status
)
VALUES
(301, 'Myanmar Tech Supply', 'Aung Min', '09111111111', 'sales@myanmartech.com', 'Yangon', 'Active'),
(302, 'Global Electronics Ltd.', 'John Lee', '09222222222', 'john@globalelectronics.com', 'Yangon', 'Active'),
(303, 'Mandalay Components', 'Ko Zaw', '09333333333', 'contact@mandalaycomponents.com', 'Mandalay', 'Active'),
(304, 'Asia Office Solutions', 'May Thu', '09444444444', 'sales@asiaoffice.com', 'Yangon', 'Active'),

-- Intentional inactive vendor
(305, 'Old Supply Company', 'Hla Hla', '09555555555', 'old@supply.com', 'Naypyidaw', 'Inactive');


-- ============================================
-- PRODUCTS
-- ============================================

INSERT INTO products (
    product_id,
    product_name,
    category,
    unit_price,
    stock_quantity,
    supplier_id,
    status,
    created_at
)
VALUES
(201, 'Business Laptop', 'Electronics', 1250000.00, 25, 301, 'Active', '2026-01-05'),
(202, 'Office Monitor 24 Inch', 'Electronics', 450000.00, 40, 302, 'Active', '2026-01-08'),
(203, 'Wireless Keyboard', 'Accessories', 85000.00, 100, 302, 'Active', '2026-01-10'),
(204, 'Wireless Mouse', 'Accessories', 45000.00, 150, 302, 'Active', '2026-01-10'),
(205, 'Office Chair', 'Furniture', 280000.00, 30, 304, 'Active', '2026-01-12'),
(206, 'Office Desk', 'Furniture', 450000.00, 20, 304, 'Active', '2026-01-12'),

-- Intentional suspicious values for later data-quality practice
(207, 'USB-C Cable', 'Accessories', -5000.00, 80, 303, 'Active', '2026-01-15'),
(208, 'Network Router', 'Networking', 350000.00, -5, 301, 'Active', '2026-01-18'),

(209, 'Server Rack', 'Networking', 950000.00, 10, 301, 'Active', '2026-01-20'),
(210, 'Printer', 'Office Equipment', 600000.00, 15, 304, 'Active', '2026-01-22');


-- ============================================
-- SALES
-- ============================================

INSERT INTO sales (
    sale_id,
    customer_id,
    product_id,
    quantity,
    unit_price,
    sale_date,
    sales_channel
)
VALUES
(5001, 101, 201, 2, 1250000.00, '2026-03-01', 'Direct'),
(5002, 102, 202, 5, 450000.00, '2026-03-02', 'Online'),
(5003, 103, 203, 3, 85000.00, '2026-03-03', 'Retail'),
(5004, 104, 205, 4, 280000.00, '2026-03-05', 'Direct'),
(5005, 106, 204, 10, 45000.00, '2026-03-06', 'Online'),
(5006, 107, 206, 2, 450000.00, '2026-03-08', 'Direct'),
(5007, 101, 209, 1, 950000.00, '2026-03-10', 'Direct'),
(5008, 102, 210, 3, 600000.00, '2026-03-12', 'Online'),
(5009, 103, 203, 5, 85000.00, '2026-03-15', 'Retail'),
(5010, 104, 201, 1, 1250000.00, '2026-03-18', 'Direct');