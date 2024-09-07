-- https://school.programmers.co.kr/learn/courses/30/lessons/276035

SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN SKILLCODES AS S
WHERE S.CATEGORY = 'Front End' AND D.SKILL_CODE & S.CODE != 0
ORDER BY 1