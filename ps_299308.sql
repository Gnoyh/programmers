# https://school.programmers.co.kr/learn/courses/30/lessons/299308

SELECT CONCAT(QUARTER(DIFFERENTIATION_DATE), "Q") AS QUARTER, COUNT(ID) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY 1
ORDER BY 1