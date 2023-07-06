def solution(n):
    answer = []
    for i in range(1,int(n/2)+1):
        if n % i == 0 :
            answer.append(i)
    answer.append(n)
    return answer