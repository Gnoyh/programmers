-- https://school.programmers.co.kr/learn/courses/30/lessons/273712

SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO AS I
WHERE NOT EXISTS (SELECT 1 FROM ITEM_TREE AS T WHERE I.ITEM_ID = T.PARENT_ITEM_ID)
ORDER BY 1 DESC