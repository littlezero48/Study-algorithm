def solution(name):
    answer = 0
    # 상하는 아스키코드를 사용
    # 알파벳들 중 가운데 N을 기준으로해서 계산
    # N보다 이전이면 ord(x)-ord('A')
    # N보다 이후면 ord('Z')-ord(x)+1
    # 둘 중 더 작은 값으로 더하기
    min_move = len(name)-1
    
    for i, x in enumerate(name):
        answer += min(ord(x)-ord('A'), ord('Z')-ord(x)+1)
        
        # 문제의 핵심은 연속된 A, A는 수정할 필요가 없음 
        # 좌우이동에서 가장 긴 연속A를 피해 가장 효율적인 방법을 찾아야함
        # 연속 A 먼저 판단
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
                
        # 비교 1) min_move는 최초 처음부터 끝까지 기본 좌우 값이 설정되나 추후에 계속 갱신됨
        # 비교 2) 가장 긴 연속A의 왼쪽 부분을 기준으로 계산
        #        가장 긴 연속A의 왼쪽 부분을 찾아가고 거기서 시작해 다시 거꾸로 돌아가기 때문에
        #        앞부분은 2*i 그리고 여기에 뒤에서부터 연속A의 오른쪽까지인 len(name)-next을 더함
        # 비교 3) 가장 긴 연속A의 오른쪽 부분을 기준으로 계산
        #        뒤에서부터 연속A 오른쪽 부분까지 갔다가 다시 뒤로 돌아가기 때문에 
        #        뒷부분은 2*(len(name)-next) 그리고 여기서 앞에서부터 연속A의 왼쪽까지가니까 i 더함 
        # 이 3가지 경우에서 가장 작은걸 찾아 min_move에 갱신
        
        min_move = min(min_move, 2*i+(len(name)-next), 2*(len(name)-next)+i)
    
    # 모든 알파벳에서 최적의 좌우 경우수를 찾아 min_move에 갱신하므로 상하값이 기록된 answer + min_move
    # 하면 최솟값을 반환하게 된다.
    return answer + min_move