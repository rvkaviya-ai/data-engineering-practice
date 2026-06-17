-- Problem: User Activity for the Past 30 Days I
-- Link: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- Difficulty: Easy
-- Topic: Aggregation, Date Functions

-- Solution:
SELECT activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;
