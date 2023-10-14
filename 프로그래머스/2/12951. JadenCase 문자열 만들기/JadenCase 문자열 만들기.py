def solution(s):
    answer = ''
    flag = False
    for one in s :
        # 공백을 만나면 대문자 전환 플래그를 false 시킨다
        if one == ' ' :
            flag = False
            answer += one
        else :
            # 대문자 플래그가 false 상황에서 공백이 아니라면 대문자로 변환 아니면 전부 소문자
            if one != ' ' and flag == False :
                flag = True
                answer += one.upper()
            else :
                answer += one.lower()
        
    return answer