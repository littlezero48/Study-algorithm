import math
def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    parking = {}
    using_time = {}
    
    # 기록 하나씩 처리
    for record in records:
        time, car_num, io = record.split()
        # 시간 문자열 > 숫자로 변환
        hour, minute = map(int,time.split(":"))
        time = hour * 60 + minute
        
        # 입차했으면 
        if io == "IN":
            parking[car_num] = time
        elif io == "OUT":
            # 출차 시 후의 추가 시간이 있을때를 대비해 사용시간을 저장해둠
            if car_num in using_time:
                using_time[car_num] += (time - parking[car_num])
            else:
                using_time[car_num] = time - parking[car_num]
            # 현재 주차 된 기록은 삭제
            del parking[car_num]
            
    # 출차 기록이 없는 케이스 경우 IN 기록만 남아 있으므로 parking 기록을 조회해 파킹 제한시간에서 입차한 시간을 차감에 기록
    for car_num, time in parking.items():
        if car_num in using_time:
            using_time[car_num] += 1439 - time
        else:
            using_time[car_num] = 1439 - time
            
    # 차량번호 작은 순서대로 딕셔너리를 정렬 x[0] = car_num
    sorted_d = sorted(using_time.items(), key = lambda x:x[0])
    
    # 사용시간에 따른 요금 계산 
    for car_num, time in sorted_d:
        # 기본요금 + 추가요금(올림((이용시간-기본시간)/단위시간))*요금)
        answer.append(default_fee+ max(0,math.ceil((time-default_time)/unit_time)) * unit_fee)
        
    return answer