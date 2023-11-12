CREATE TABLE employee
(employee_id int PRIMARY KEY,
name varchar(50),
surname varchar(50),
supervisor_id int,
age int);

INSERT INTO employee (employee_id, name, surname, supervisor_id, age) VALUES
(1, 'John', 'Smith', 5, 25),
(2, 'Jake', 'Doe', 7, 38),
(3, 'James', 'Davis', 5, 28),
(4, 'Emily', 'Milles', 2, 31),
(5, 'Robert', 'Jones', 7, 35),
(6, 'Michelle', 'Williams', 2, 32),
(7, 'Karen', 'Brown', 8, 56),
(8, 'Martin', 'Johnson', NULL, 62);

CREATE TABLE contract
(employee_id int PRIMARY KEY,
salary int,
type_of_contract varchar(50));

INSERT INTO contract (employee_id, salary, type_of_contract) VALUES
(1, 5000, 'contract_of_employment'),
(2, 7500, 'business_to_business'),
(3, 5000, 'contract_of_employment'),
(4, 5000, 'business_to_business'),
(5, 6000, 'contract_of_employment'),
(6, 5000, 'contract_of_employment'),
(7, 10000, 'business_to_business'),
(8, 15000, 'contract_of_employment');

CREATE TABLE date
(employee_id int PRIMARY KEY,
start_of_employment date NOT NULL,
end_of_employment date);

INSERT INTO date (employee_id, start_of_employment, end_of_employment) VALUES
(1, '11-04-2020', '11-01-2023'),
(2, '21-03-2016', '02-01-2020'),
(3, '11-02-2021', '05-11-2024'),
(4, '03-09-2010', NULL),
(5, '04-07-2007', NULL),
(6, '12-06-2011', '01-02-2026'),
(7, '16-03-2012', '21-07-2021'),
(8, '01-02-2005', NULL)