-- 코드를 입력하세요
SELECT hour(datetime) as hour, count(*) from animal_outs group by hour having 9 <= hour and hour < 20 order by hour;