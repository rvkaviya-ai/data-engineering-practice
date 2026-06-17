-- Problem: Patients With a Condition
-- Link: https://leetcode.com/problems/patients-with-a-condition/
-- Difficulty: Easy
-- Topic: Select, String Matching

-- Solution:
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'
OR conditions LIKE '% DIAB1%';
