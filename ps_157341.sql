-- https://school.programmers.co.kr/learn/courses/30/lessons/157341

SELECT RH.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS RH
JOIN CAR_RENTAL_COMPANY_CAR AS C ON RH.CAR_ID = C.CAR_ID
WHERE CAR_TYPE = '세단' AND START_DATE LIKE '2022-10%'
GROUP BY RH.CAR_ID
ORDER BY RH.CAR_ID DESC