-- https://school.programmers.co.kr/learn/courses/30/lessons/284528

WITH AG AS (
    SELECT EMP_NO, 
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT HE.EMP_NO, HE.EMP_NAME, AG.GRADE, 
    CASE
        WHEN AG.GRADE = 'S' THEN (SAL * 0.2)
        WHEN AG.GRADE = 'A' THEN (SAL * 0.15)
        WHEN AG.GRADE = 'B' THEN (SAL * 0.1)
        ELSE 0
    END AS BONUS
FROM HR_EMPLOYEES AS HE
JOIN AG ON HE.EMP_NO = AG.EMP_NO
ORDER BY HE.EMP_NO