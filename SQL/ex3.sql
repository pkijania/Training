-- 3. Employees with salary higher than employee with id 5

-- Question:

-- Design query to present employees with salary higher than employee with id 5

-- Solution:

SELECT COUNT(employee_id) AS salary
FROM contract
WHERE salary > (SELECT salary FROM contract WHERE employee_id = 5)