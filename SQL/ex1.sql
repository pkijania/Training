-- 1. Employee - Supervisor link

-- Question:

-- Design query to present employee and supervisor in one row:

-- Solution:

SELECT CONCAT(emp.name, ' ', emp.surname) AS employee_name, CONCAT(sup.name, ' ', sup.surname) AS supervisor_name
FROM EMPLOYEE emp
LEFT JOIN EMPLOYEE sup ON (sup.employee_id = emp.supervisor_id)