-- Problem: Restaurant Growth
-- Link: https://leetcode.com/problems/restaurant-growth/
-- Difficulty: Medium
-- Topic: Window Functions, CTE, Date Functions

-- Solution:
WITH each_day_sum AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
total_sum AS (
    SELECT visited_on,
        amount,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS running_sum
    FROM each_day_sum
)
SELECT visited_on,
    running_sum AS amount,
    ROUND((running_sum / 7), 2) AS average_amount
FROM total_sum
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + INTERVAL 6 DAY;
