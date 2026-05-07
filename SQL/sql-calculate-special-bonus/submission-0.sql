-- Write your query below
SELECT 
    employee_id, 
    (
        CASE 
            WHEN name not LIKE 'M%' and employee_id % 2 = 1 
            THEN salary
            ELSE 0 
        END
    ) AS bonus 
FROM employees order by employee_id;