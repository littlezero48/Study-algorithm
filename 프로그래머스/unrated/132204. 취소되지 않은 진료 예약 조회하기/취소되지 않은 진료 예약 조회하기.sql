-- 코드를 입력하세요

SELECT AP.APNT_NO, AP.PT_NAME, AP.PT_NO, AP.MCDP_CD, D.DR_NAME, AP.APNT_YMD
FROM 
    (SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, A.MDDR_ID, A.APNT_YMD
     FROM (SELECT APNT_NO, PT_NO, MCDP_CD, MDDR_ID, APNT_YMD 
            FROM APPOINTMENT
            WHERE APNT_YMD LIKE '2022-04-13%' 
                AND MCDP_CD = 'CS' 
                AND APNT_CNCL_YN != 'Y'
         ) AS A # 필요없는 예약 먼저 필터링
    INNER JOIN PATIENT AS P
    ON A.PT_NO = P.PT_NO) AS AP
INNER JOIN DOCTOR AS D
ON AP.MDDR_ID = D.DR_ID
ORDER BY AP.APNT_YMD ASC
