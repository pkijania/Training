-- 2. Employees aged between 29 and 55 years old

-- Question:

-- Design query to present id, name and surname of employees aged between 29 and 55 years old ordered by column "name"

-- Solution:

SELECT employee_id, name, surname
FROM EMPLOYEE
WHERE age BETWEEN 29 AND 55
ORDER BY name