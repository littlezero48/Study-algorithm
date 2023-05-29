def solution(n, k):
    answer = []
    for i in range(k,n+1,k):
        answer.append(i)
    return answer