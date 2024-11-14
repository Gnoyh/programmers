-- https://school.programmers.co.kr/learn/courses/30/lessons/131535

SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND 20 <= AGE AND AGE <= 29