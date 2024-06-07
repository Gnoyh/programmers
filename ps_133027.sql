-- https://school.programmers.co.kr/learn/courses/30/lessons/133027

SELECT F.FLAVOR
FROM FIRST_HALF AS F
JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER FROM JULY GROUP BY FLAVOR) AS J ON F.FLAVOR = J.FLAVOR
ORDER BY (F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
LIMIT 3