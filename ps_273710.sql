# https://school.programmers.co.kr/learn/courses/30/lessons/273710

SELECT II.ITEM_ID, II.ITEM_NAME
FROM ITEM_INFO AS II
JOIN ITEM_TREE AS IT ON II.ITEM_ID = IT.ITEM_ID
WHERE IT.PARENT_ITEM_ID IS NULL
ORDER BY II.ITEM_ID