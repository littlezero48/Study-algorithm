def solution(age):
    answer = ''
    while age != 0 :
        remain = age % 10
        answer = chr(remain + 97) + answer
        age = int(age / 10)
    
    return answer