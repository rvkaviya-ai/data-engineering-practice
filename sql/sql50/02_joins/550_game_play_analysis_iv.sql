-- Problem: Game Play Analysis IV
-- Link: https://leetcode.com/problems/game-play-analysis-iv/
-- Difficulty: Medium
-- Topic: Joins, CTE, Date Functions

-- Solution:
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
)
SELECT ROUND(COUNT(a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a
JOIN first_login f 
    ON a.player_id = f.player_id 
    AND a.event_date = DATE_ADD(f.event_date, INTERVAL 1 DAY);
