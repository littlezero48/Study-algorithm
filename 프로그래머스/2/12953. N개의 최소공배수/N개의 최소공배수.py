def solution(arr):
    # 배열 수 중 보다 가장 큰 수를 기준으로 배수를 구하고
    # 커지는 배수마다 배열의 수로 나누어 모두 나누어 떨어지는 순간의 수를 최소공배수
        
    max_num = max(arr) # 가장 큰 수
    i = 1
    while True :
        multi_num = max_num * i # 큰 수의 배수
        flag = True             # 배수 판별 플래그
        for one in arr :
            if multi_num % one != 0: # 하나의 수라도 나누어 떨어지지 않으면 false
                flag = False

        if flag :               # 모두 나누어 떨어지면 true
            return multi_num    # 최소공배수 return
        else :
            i += 1