-- Problem: Confirmation Rate
-- Link: https://leetcode.com/problems/confirmation-rate/
-- Difficulty: Medium
-- Topic: Joins, CTE, Case When

-- Solution:
WITH cte AS (
    SELECT s.user_id, c.action
    FROM Signups s
    LEFT JOIN Confirmations c ON s.user_id = c.user_id
)
SELECT user_id,
    IFNULL(ROUND(SUM(CASE
        WHEN action = 'timeout' THEN 0
        WHEN action = 'confirmed' THEN 1
    END) / COUNT(*), 2), 0) AS confirmation_rate
FROM cte
GROUP BY user_id;
