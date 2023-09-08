-- 4. Data from both tables

-- Question:

-- Design query to present data (id, name, surname, age, salary, type_of_contract) in one table

-- Solution:

SELECT EMPLOYEE.employee_id, name, surname, age, salary, type_of_contract
FROM EMPLOYEE
JOIN CONTRACT ON (EMPLOYEE.employee_id = CONTRACT.employee_id)