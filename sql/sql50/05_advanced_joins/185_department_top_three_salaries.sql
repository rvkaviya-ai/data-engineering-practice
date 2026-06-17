-- Problem: Department Top Three Salaries
-- Link: https://leetcode.com/problems/department-top-three-salaries/
-- Difficulty: Hard
-- Topic: Window Functions, CTE, Joins

-- Solution:
WITH emp AS (
    SELECT name AS employee,
        departmentId,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
),
filtered AS (
    SELECT * FROM emp
    WHERE rnk <= 3
)
SELECT d.name AS Department, f.employee AS Employee, f.salary AS Salary
FROM filtered f
JOIN Department d ON f.departmentId = d.id;
