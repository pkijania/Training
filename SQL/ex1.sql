-- 1. Employee - Supervisor link

-- Question:

-- Design query to present employee and his/her supervisor in one row

-- Solution:

SELECT CONCAT(emp.name, ' ', emp.surname) AS employee_name, CONCAT(sup.name, ' ', sup.surname) AS supervisor_name
FROM employee emp
LEFT JOIN employee sup ON (sup.employee_id = emp.supervisor_id)