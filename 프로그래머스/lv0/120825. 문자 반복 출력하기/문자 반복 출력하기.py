def solution(my_string, n):
    answer = ''
    for one in my_string :
        answer += one * n
    return answer