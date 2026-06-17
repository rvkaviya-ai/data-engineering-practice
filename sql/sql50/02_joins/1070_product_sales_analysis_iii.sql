-- Problem: Product Sales Analysis III
-- Link: https://leetcode.com/problems/product-sales-analysis-iii/
-- Difficulty: Medium
-- Topic: Joins, CTE

-- Solution:
WITH first_year AS (
    SELECT product_id, MIN(year) AS fy
    FROM Sales
    GROUP BY product_id
)
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN first_year f 
    ON s.product_id = f.product_id 
    AND s.year = f.fy;
