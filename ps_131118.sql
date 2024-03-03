# https://school.programmers.co.kr/learn/courses/30/lessons/131118

SELECT RR.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_REVIEW AS RR
JOIN REST_INFO AS RI ON RR.REST_ID = RI.REST_ID
GROUP BY RR.REST_ID
HAVING RI.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, RI.FAVORITES DESC