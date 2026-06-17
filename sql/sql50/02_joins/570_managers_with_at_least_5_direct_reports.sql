-- Problem: Managers with at Least 5 Direct Reports
-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Difficulty: Medium
-- Topic: Joins

-- Solution:
SELECT e.name 
FROM Employee e
JOIN (
    SELECT managerId, COUNT(*) 
    FROM Employee 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5
) AS t ON e.id = t.managerId;
