-- Problem: Friend Requests II: Who Has the Most Friends
-- Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Difficulty: Medium
-- Topic: CTE, Union, Aggregation

-- Solution:
WITH cte AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT id, COUNT(*) AS num
FROM cte
GROUP BY id
ORDER BY COUNT(*) DESC
LIMIT 1;
