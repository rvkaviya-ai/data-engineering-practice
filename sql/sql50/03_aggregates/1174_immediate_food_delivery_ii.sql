-- Problem: Immediate Food Delivery II
-- Link: https://leetcode.com/problems/immediate-food-delivery-ii/
-- Difficulty: Medium
-- Topic: Aggregation, Window Functions, Subqueries

-- Solution:
SELECT ROUND(
    (
        SELECT COUNT(*)
        FROM (
            SELECT customer_id, order_date, customer_pref_delivery_date,
                ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS row_num
            FROM Delivery
        ) immediate_order
        WHERE immediate_order.row_num = 1
        AND immediate_order.order_date = immediate_order.customer_pref_delivery_date
    ) /
    (
        SELECT COUNT(*)
        FROM (
            SELECT customer_id, order_date, customer_pref_delivery_date,
                ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS row_num
            FROM Delivery
        ) first_order
        WHERE first_order.row_num = 1
    ) * 100, 2) AS immediate_percentage;
