def solution(cards):
    answer = []
    # 방문 체크
    box_visited = [False] * (len(cards)+1) 
    
    # 게임 시작
    for num in cards:
        # 처음 시작할때 해당 카드 방문했는지 여부 확인 (이전 방문했다면 종료)
        if not box_visited[num]:
            group = []
            # 이번 그룹에서 방문하지 않았던 카드라면 진행, 이전 방문했다면 종료
            while num not in group:
                group.append(num)
                num = cards[num-1]      # 0부터 1로 봐야해서
                box_visited[num] = True # 방문 체크
            # 서클의 종료 후 이번 서클에서 열어본 상자수를 추가    
            answer.append(len(group))
            
    # 1번 상자 그룹 서클에 모든 카드를 방문했다면
    if answer[0] == len(cards):
        return 0
    else:
        # 범희가 이 게임에서 얻을 수 있는 최고점을 위해 상자 그룹이 큰 케이스 1,2위를 선택하기 위해 정렬
        answer.sort(reverse=True)

    # 1번 그룹과 2번 그룹에 속한 상자 수 곱한 게임 점수
    return answer[0] * answer[1]