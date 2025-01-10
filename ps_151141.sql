-- https://school.programmers.co.kr/learn/courses/30/lessons/151141

WITH VT AS(
    SELECT H.HISTORY_ID, C.DAILY_FEE, DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS DATEDIFF, IFNULL(P.DISCOUNT_RATE, 0) AS DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    JOIN CAR_RENTAL_COMPANY_CAR AS C ON H.CAR_ID = C.CAR_ID
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P ON C.CAR_TYPE = P.CAR_TYPE AND
    (
    CASE 
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE NULL
    END
    ) = P.DURATION_TYPE
    WHERE C.CAR_TYPE = '트럭'
)

SELECT HISTORY_ID, TRUNCATE(DAILY_FEE * (1 - (DISCOUNT_RATE / 100)) * DATEDIFF, 0) AS FEE
FROM VT
ORDER BY 2 DESC, 1 DESC