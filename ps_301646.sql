# https://school.programmers.co.kr/learn/courses/30/lessons/301646

SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE (CONV(GENOTYPE, 10, 2) & 1 OR CONV(GENOTYPE, 10, 2) & 4) AND NOT CONV(GENOTYPE, 10, 2) & 2