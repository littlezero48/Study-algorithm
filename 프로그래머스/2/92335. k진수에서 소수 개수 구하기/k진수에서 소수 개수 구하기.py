def solution(n, k):    
    # 모든 조건이 0을 기준으로 나눠 소수를 판단하므로 0기준으로 숫자를 분리 
    
    answer = 0

    # 숫자n을 k진법 문자열로 변환
    strNum=""
    while n:            
        strNum = str(n%k) + strNum
        n = n//k
        
    # 진법을 표현한 문자열을 0을 기준으로 분리해 배열
    numsArr = strNum.split("0")  
    
    for num in numsArr:                
        # 0으로 분리한 값이 빈값이거나 1인경우 (1은 소수가 아님) 판단 패스
        if (num == "") or (int(num) == 1) :   
            continue
            
        intNum = int(num)
          
        # 소수 판단 : 
        # 1과 자기자신 만을 약수로 가지므로 1부터 자기자신 사이의 값으로 나눠지는 약수는 갖는다면 그건 소수가 아님
        # 약수가 된다면 최대 제곱근 이하이므로 그 이후 숫자는 약수 판단에서 제외
        primeChk = True        
        for i in range(2,int(intNum**0.5)+1): 
            if intNum%i == 0: 
                primeChk = False
                break
            
        # 소수 개수 갱신
        if primeChk: 
            answer+=1
            
    return answer