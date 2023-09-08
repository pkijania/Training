-- 5. Number of contracts

-- Question:

-- Design query to show the number of b2b contracts and contracts of employment

-- Solution:

SELECT 
SUM(CASE WHEN type_of_contract = 'contract_of_employment' THEN 1 ELSE 0 END) AS "Number_of_employment_contracts", 
SUM(CASE WHEN type_of_contract = 'business_to_business' THEN 1 ELSE 0 END) AS "Number_of_b2b_contracts"
FROM contract