-- 9. View

-- Question:

-- Design view which will contain information about number of employed personel in each year

-- Solution:

CREATE OR REPLACE VIEW employed AS
SELECT EXTRACT(YEAR FROM start_of_employment) AS rok, count(*) AS sum_of_employees
FROM date 
GROUP BY EXTRACT(YEAR FROM start_of_employment)