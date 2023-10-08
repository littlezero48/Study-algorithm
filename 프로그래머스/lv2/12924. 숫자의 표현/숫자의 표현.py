def solution(n):
    answer = 0
    for i in range(1, n+1): # 1부터 값 더해보기
        sum = 0
        for j in range(i, n+1): 
            sum += j
            if sum == n : # 합이 표현 할 수와 같으면 표현 방법 +1
                answer += 1
            if sum > n : # 합이 표현 할 수를 넘으면 break
                break
                
    return answer