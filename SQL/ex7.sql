-- 7. All data

-- Question:

-- Design query to present all data from all tables

-- Solution:

SELECT date.employee_id, name, surname, supervisor_id, age, salary, type_of_contract, start_of_employment, end_of_employment
FROM date JOIN employee ON (employee.employee_id = date.employee_id) JOIN contract ON (contract.employee_id = date.employee_id)