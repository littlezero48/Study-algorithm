-- 코드를 입력하세요
SELECT H.FLAVOR
FROM FIRST_HALF AS H 
INNER JOIN ICECREAM_INFO AS I
ON H.FLAVOR = I.FLAVOR
WHERE INGREDIENT_TYPE = 'fruit_based'
    AND TOTAL_ORDER > 3000
ORDER BY TOTAL_ORDER DESC