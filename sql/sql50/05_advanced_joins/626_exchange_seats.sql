-- Problem: Exchange Seats
-- Link: https://leetcode.com/problems/exchange-seats/
-- Difficulty: Medium
-- Topic: Window Functions, CTE, Case When

-- Solution:
WITH cte AS (
    SELECT id,
        student,
        LAG(student) OVER (ORDER BY id) AS prev,
        LEAD(student) OVER (ORDER BY id) AS next
    FROM Seat
)
SELECT id,
    CASE
        WHEN id % 2 != 0 THEN IFNULL(next, student)
        WHEN id % 2 = 0 THEN prev
    END AS student
FROM cte;
