def solution(s):
    answer = ''
    flag = False
    for one in s :
        if one == ' ' :
            flag = False
            answer += one
        else :
            if one != ' ' and flag == False :
                flag = True
                answer += one.upper()
            else :
                answer += one.lower()
        
    return answer