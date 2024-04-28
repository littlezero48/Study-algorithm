from collections import deque

def bfs(p):
    start = []    
    for i in range(5):                      # 시작점이 되는 응시자 자리 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':              # 응시자라면 
                start.append([i, j])        # 시작점에 추가
    
    for s in start:
        queue = deque([s])                    # 응시자 좌표
        visited = [[0]*5 for i in range(5)]   # 방문 처리
        distance = [[0]*5 for i in range(5)]  # 경로 길이(맨해튼거리) 
        visited[s[0]][s[1]] = 1               # 시작점에 먼저 방문표시
        
        while queue:
            y, x = queue.popleft() # 시작점 또는 while문에서 추가한 좌표를 받아옴
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):  # 이동방향이 상하좌우 4개이기 때문
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0: # 대기실 최소 최대 안이라면 , 방문하지 않았다면
                    
                    if p[ny][nx] == 'O':                        # 빈테이블
                        queue.append([ny, nx])                  # 다음 좌표를 queue에 추가하여 이동하게끔 만든다
                        visited[ny][nx] = 1                     # 방문체크   
                        distance[ny][nx] = distance[y][x] + 1   # 맨해튼 거리 +1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:    # 다른 응시자를 만났으나 맨해튼 거리가 1이하인 경우
                        return 0
    return 1

def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer