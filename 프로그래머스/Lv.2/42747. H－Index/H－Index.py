def solution(citations):
    answer = 0
    
    # 내림차순으로 만들어 인덱스+1 번호가 최초로 해당 인덱스 값을 넘지 않는 순간 H-Index 값이 된다.
    citations.sort(reverse=True) 
    
    for i in range(len(citations)) :
        if citations[i] < i+1 :
            return i
        
    # 예외처리 : 참조된 모든 수가 인덱스 번호가 모두 같고,
    #           인덱스 값보다 크게 되면 위의 식에선 H-Index값이 0이 된다
    #           이 경우 그 논문 편수가 바로 H-Index 값이 된다.            
    return len(citations)