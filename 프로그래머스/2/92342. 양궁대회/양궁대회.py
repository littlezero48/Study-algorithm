from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0   # 가장 큰 점수차이를 만들기 위한 변수   

    # 중복 조합을 이용해 과녁의 점수를 중복적으로 선택하여 n발을 꽂아 라이언의 점수 경우를 만들고 비교
    # 총 n발 즉, n번의 기회 중 해당 번째에 range(0,11) 0~10점 사이에 득점한 경우의 모든 조합 중 어피치의 득점 비교
    for res in list(combinations_with_replacement(range(0, 11), n)):
        # 점수판 횟수를 초기화
        now = [0 for _ in range(11)]
        
        # 라이언이 어느 점수에 몇번 맞췄는지를 정리
        for r in res:            
            now[10 - r] += 1       
        
        lion = 0
        peach = 0
        
        # 라이언 점수와 어피치 점수 비교
        # i 해당 점수, l은 라이언이 맞춘횟수, p는 어피치가 맞춘횟수
        for i, (l, p) in enumerate(zip(now, info)):
            # 둘 다 맞추지 못했으므로 누구도 점수 획득 못함
            if l == p == 0:
                continue
            # 어피치의 횟수가 많았으므로 어피치가 획득
            if p >= l:
                peach += (10 - i) # 점수판 출력이 10점부터 0점으로 내림차순이라 10 - i가 되는 것 
            # 라이언 횟수가 많았으므로 라이언이 획득
            elif l > p:
                lion += (10 - i)
                
        # 총 점수를 비교 라이언이 크면 승리했으므로 그 차이를 기록
        if lion > peach:
            win = True
            if (lion - peach) > max_num:
                max_num = lion - peach
                answer = now
                
    # 승리를 못했다면 [-1]            
    if not win:
        return [-1]
    
    return answer