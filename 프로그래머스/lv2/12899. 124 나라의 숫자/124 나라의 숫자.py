def solution(n):
    numbers = ['4','1','2'] 
    answer= ""
    
    while n : 
        answer += numbers[n%3]    
        if n % 3 != 0:
            n //= 3
        else:
            n = n//3 - 1            # 다른 수들은 나머지가 몫에 포함되지 않지만 3은 3으로 나누면 몫+1이됨
                                    # 그래서 이후 수에 영향을 미치므로 -1 처리해서 몫에 영향을 주지 않게함
        
    return answer[::-1]             # 문자열 역순 쉽게 하는법