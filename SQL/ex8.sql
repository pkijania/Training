-- 8. Materialized view

-- Question:

-- Design materialized view which will contain information about currently employed employees

-- Solution:

CREATE MATERIALIZED VIEW currently_employed AS
SELECT date.employee_id, name, surname, salary, start_of_employment, end_of_employment
FROM date JOIN employee ON (employee.employee_id = date.employee_id) JOIN contract ON (contract.employee_id = date.employee_id)
WHERE (start_of_employment < NOW()) AND (end_of_employment IS NULL OR end_of_employment > NOW())