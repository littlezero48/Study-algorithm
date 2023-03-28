def solution(n, m, section):
    answer = 0
    if m == 1 :
        return len(section)
    
    first_num = 0
    for i in range(0, len(section)) :
        if i == 0 : 
            first_num = section[i]
            answer += 1
        
        if m <= section[i] - first_num :
            answer += 1
            first_num = section[i]       
    
    return answer