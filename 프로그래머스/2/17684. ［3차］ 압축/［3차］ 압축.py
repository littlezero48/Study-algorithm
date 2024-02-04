def solution(msg):
    answer = []
    
    # 사전 초기화
    # 아스키코드 65: 대문자A ~  대문자Z (26개)의 길이1 사전 생성
    # A, B, C, D ... Z
    # 딕셔너리로 단어:인덱스 값
    dt = { chr(i+65):i+1 for i in range(26) }
    
    # 단어 체크
    while True:
        if msg in dt :
            answer.append(dt[msg]) # 단어 그대로가 사전에 있다면 그 단어 인덱스를 바로 추가
            break
        
        for i in range(1, len(dt)) : 
            if msg[:i+1] not in dt : # 0부터 시작해 한글자씩 늘려가며 단어 여부 확인 
                # 없다면 사전에 추가
                dt[msg[:i+1]] = len(dt)+1
                # 사전에 추가하고 출력
                answer.append(dt[msg[:i]])
                # 출력한 단어는 제외
                msg = msg[i:]   
                break
    
    return answer