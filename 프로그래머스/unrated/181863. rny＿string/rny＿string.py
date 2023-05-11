def solution(rny_string):
    answer = ''
    for i in rny_string:
        if i != "m":
            answer += i
        else :
            answer += "rn"
        
    return answer