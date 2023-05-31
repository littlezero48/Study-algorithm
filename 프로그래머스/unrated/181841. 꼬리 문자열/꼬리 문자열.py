def solution(str_list, ex):
    answer = ''
    
    for one in str_list :
        if ex not in one :
            answer += one
            
    return answer