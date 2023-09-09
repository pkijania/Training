-- 6. Employees with surname longer than 5 letters

-- Question:

-- Design query to present name, surname and age of employees with surname longer than 5 letters ordered by their age (descending)

-- Solution:

SELECT name, surname, age
FROM employee
WHERE lENGTH(surname) > 5
ORDER BY age DESC