-- Problem: Consecutive Numbers
-- Link: https://leetcode.com/problems/consecutive-numbers/
-- Difficulty: Medium
-- Topic: Subqueries, Window Functions, CTE

-- Solution:
WITH cte AS (
    SELECT num,
        id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS bucket_num
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM cte
GROUP BY num, bucket_num
HAVING COUNT(*) >= 3;
