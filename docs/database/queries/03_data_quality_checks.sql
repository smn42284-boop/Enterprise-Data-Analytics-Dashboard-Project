-- Enterprise Master Data & Analytics Dashboard
-- Stage 3: Data Quality Checks


-- ============================================
-- 1. Missing Customer Emails
-- ============================================

SELECT
    customer_id,
    customer_name,
    email
FROM customers
WHERE email IS NULL;


-- ============================================
-- 2. Duplicate Customers
-- ============================================

SELECT
    customer_name,
    phone,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_name, phone
HAVING COUNT(*) > 1;


-- ============================================
-- 3. Negative Product Prices
-- ============================================

SELECT
    product_id,
    product_name,
    unit_price
FROM products
WHERE unit_price < 0;


-- ============================================
-- 4. Negative Stock Quantities
-- ============================================

SELECT
    product_id,
    product_name,
    stock_quantity
FROM products
WHERE stock_quantity < 0;


-- ============================================
-- 5. Inactive Vendors
-- ============================================

SELECT
    vendor_id,
    vendor_name,
    status
FROM vendors
WHERE status = 'Inactive';


-- ============================================
-- 6. Inactive Customers
-- ============================================

SELECT
    customer_id,
    customer_name,
    status
FROM customers
WHERE status = 'Inactive';


-- ============================================
-- 7. Products With Inactive Vendors
-- ============================================

SELECT
    p.product_id,
    p.product_name,
    v.vendor_name,
    v.status AS vendor_status
FROM products AS p
JOIN vendors AS v
    ON p.supplier_id = v.vendor_id
WHERE v.status = 'Inactive';


-- ============================================
-- 8. Sales With Invalid Customer References
-- ============================================

SELECT
    s.sale_id,
    s.customer_id
FROM sales AS s
LEFT JOIN customers AS c
    ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL;


-- ============================================
-- 9. Sales With Invalid Product References
-- ============================================

SELECT
    s.sale_id,
    s.product_id
FROM sales AS s
LEFT JOIN products AS p
    ON s.product_id = p.product_id
WHERE p.product_id IS NULL;


-- ============================================
-- 10. Negative Sales Quantity
-- ============================================

SELECT
    sale_id,
    product_id,
    quantity
FROM sales
WHERE quantity < 0;