-- https://school.programmers.co.kr/learn/courses/30/lessons/299305

SELECT P.ID, COUNT(C.ID) AS CHILD_COUNT
FROM ECOLI_DATA AS P
LEFT JOIN ECOLI_DATA AS C ON P.ID = C.PARENT_ID
GROUP BY P.ID
ORDER BY P.ID