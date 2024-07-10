-- https://school.programmers.co.kr/learn/courses/30/lessons/301649

WITH VT AS (
    SELECT ID, PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER
    FROM ECOLI_DATA
)
SELECT ID, 
    CASE 
        WHEN PER <= 0.25 THEN 'CRITICAL'
        WHEN PER <= 0.50 THEN 'HIGH'
        WHEN PER <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM VT
ORDER BY 1