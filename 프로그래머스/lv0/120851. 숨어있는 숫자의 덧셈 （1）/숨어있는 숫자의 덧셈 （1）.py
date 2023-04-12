def solution(my_string):
    answer = 0
    for i in range(0,len(my_string)) :
        if my_string[i].isdigit() :
            answer += int(my_string[i])
            
    return answer