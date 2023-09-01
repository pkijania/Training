## Setup

Please execute setup.sql script before running any below queries. 

### 1. Employee - Supervisor link

##### Question:

Design query to present employee and supervisor in one row:

##### Solution:

```
SELECT CONCAT(emp.name, ' ', emp.surname) AS employee_name, CONCAT(sup.name, ' ', sup.surname) AS supervisor_name
FROM EMPLOYEE emp
LEFT JOIN EMPLOYEE sup ON (sup.employee_id = emp.supervisor_id)
```
### 2. Employees aged between 29 and 55 years old

##### Question:

Design query to present employees aged between 29 and 55 years old ordered by column "name":

##### Solution:

```
SELECT employee_id, name, surname
FROM EMPLOYEE
WHERE age BETWEEN 29 AND 55
ORDER BY name
```
### 3. Employees with salary higher than employee with id 5

##### Question:

Design query to present employees with salary higher than employee with id 5:

##### Solution:

```
SELECT COUNT(employee_id) AS salary
FROM CONTRACT
WHERE salary > (SELECT salary FROM CONTRACT WHERE employee_id = 5)
```
### 4. Data from both tables

##### Question:

Design query to present data from both tables:

##### Solution:

```
SELECT EMPLOYEE.employee_id, name, surname, age, salary, type_of_contract
FROM EMPLOYEE
JOIN CONTRACT ON (EMPLOYEE.employee_id = CONTRACT.employee_id)
```