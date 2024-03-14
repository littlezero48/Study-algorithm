def solution(s):
    answerArr = []
    
    # 문자열이 하나 인경우 1 반환
    if len(s) == 1 :
        return 1
    
    # 최소 1개 반복, 최대 len(s)의 절반 반복 가능
    for i in range(1, (len(s) // 2) + 1) :  # +1 하지 않으면 len(s)의 절반이 불포함되므로 주의
        result = ''
        
        temp = s[:i] # 반복 판별 문자열
        cnt = 1
        
        # i 단위에 따라 문자열 압축 결과를 기록
        for j in range(i, len(s), i) :  # 단위만큼 잘라 판별하기 위해 3번째 파라미터를 i로 설정
            if temp == s[j:j+i] :       # 다음 차례에 단위만큼을 잘라 반복 판별 문자열과 비교
                cnt = cnt + 1           # 같다면 카운트
            else :
                if cnt > 1 :            # 같지않다면 반복된 회수를 확인하고, 이를 압축 문자열에 반영
                    result = result + str(cnt) + temp
                else :
                    result = result + temp              
                cnt = 1 # 새로운 판별을 위해 반복수 초기화
                temp = s[j:j+i]
                
        # 만약 바로 위 for문에서 최대 len(s)의 절반으로 반복이 가능해 else로 빠지지 않는 케이스라면 여기서 결과를 기록    
        if cnt > 1 :            # 같지않다면 반복된 회수를 확인하고, 이를 압축 문자열에 반영
            result = result + str(cnt) + temp
        else :
            result = result + temp   
                    
        # 모든 압축 케이스를 기록
        answerArr.append(len(result))
        
    return min(answerArr) # 그중 가장 작은 걸 반환