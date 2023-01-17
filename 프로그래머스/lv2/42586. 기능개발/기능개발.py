def solution(progresses, speeds):
    release_cnt = 0
    day = 0
    answer = []
    
    while len(progresses) > 0 :                         # progresses배열이 존재하는 한 계속 진행
        if (progresses[0] + speeds[0] * day) >= 100 :   # 100을 달성하면
            release_cnt = release_cnt + 1               # cnt 추가
            progresses.pop(0)                           # 배열에서 제거하므로써 while을 줄여감
            speeds.pop(0)                               # 배열에서 제거
        else :                                          # 100 달성 못하면
            if release_cnt > 0 :                        # cnt가 0이면 그냥 패스
                                                        # cnt가 존재하고 100달성을 못한 걸 만났다면 이전 달성케이스까지를 answer에 append
                answer.append(release_cnt)      
                release_cnt = 0                         # 다시 cnt 초기화
            day = day + 1                               # 조건 달성을 위해 day를 하나하나 늘려감 
    
    answer.append(release_cnt)                          # 배열 모두 pop하고 처리되지 못한 마지막 결과를 넣기 위한 append              
            
    return answer


    
    
    