-- https://school.programmers.co.kr/learn/courses/30/lessons/77487

WITH VT AS (
    SELECT *
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) > 1
    )
SELECT P.*
FROM PLACES AS P
JOIN VT ON P.HOST_ID = VT.HOST_ID