-- https://school.programmers.co.kr/learn/courses/30/lessons/299310

WITH A AS (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MS
    FROM ECOLI_DATA
    GROUP BY YEAR
)

SELECT YEAR(B.DIFFERENTIATION_DATE) AS YEAR, (A.MS - B.SIZE_OF_COLONY) AS YEAR_DEV, B.ID
FROM ECOLI_DATA AS B
JOIN A ON YEAR(B.DIFFERENTIATION_DATE) = A.YEAR
ORDER BY YEAR, YEAR_DEV