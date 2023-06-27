def solution(n):
    answer = []
    for i in range(n):
        answer2 = []
        for j in range(n):
            if j == i :
                answer2.append(1)
            else :
                answer2.append(0)
        answer.append(answer2)
    return answer