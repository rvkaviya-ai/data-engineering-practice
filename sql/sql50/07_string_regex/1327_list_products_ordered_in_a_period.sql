-- Problem: List the Products Ordered in a Period
-- Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period/
-- Difficulty: Easy
-- Topic: CTE, Aggregation, Date Functions

-- Solution:
WITH cte AS (
    SELECT product_id, SUM(unit) AS total
    FROM Orders
    WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
    GROUP BY product_id
    HAVING SUM(unit) >= 100
)
SELECT p.product_name, t.total AS unit
FROM cte t
JOIN Products p ON t.product_id = p.product_id;
