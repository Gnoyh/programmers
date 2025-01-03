-- https://school.programmers.co.kr/learn/courses/30/lessons/284527

WITH MS AS (
    SELECT SUM(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT SUM(HG.SCORE) AS SCORE, HG.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM HR_GRADE AS HG
JOIN HR_EMPLOYEES AS HE ON HG.EMP_NO = HE.EMP_NO
GROUP BY HG.EMP_NO
HAVING SCORE = (SELECT MAX(SCORE) FROM MS)