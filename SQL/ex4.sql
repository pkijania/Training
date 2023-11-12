-- 4. Data from both tables

-- Question:

-- Design query to present data (id, name, surname, age, salary, type_of_contract) in one table

-- Solution:

SELECT employee.employee_id, name, surname, age, salary, type_of_contract
FROM employee
JOIN CONTRACT ON (employee.employee_id = contract.employee_id)