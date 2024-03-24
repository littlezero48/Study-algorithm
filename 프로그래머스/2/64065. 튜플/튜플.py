def solution(s):
    answer = []
    # 문자열을 숫자만 남기기 위해 1차 단계 문자열 앞뒤 {{}}를 제거
    step1_s = s[2:-2]
    # 문자열을 숫자만 남기기 위해 2차 단계로 숫자 사이의 문자열 },{ 기준으로 배열 만들기
    step2_s = step1_s.split("},{")
    # {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
    # 이런 식으로 정렬해야 하기 때문에 배열안의 길이로 정렬
    step2_s.sort(key=len)
    
    for one in step2_s:
        # 각 집합의 원소들로 나눔
        num_arr = one.split(",")
        for num in num_arr:
            # 숫자가 answer에 없다면 
            if int(num) not in answer: 
                answer.append(int(num))    
    
    return answer