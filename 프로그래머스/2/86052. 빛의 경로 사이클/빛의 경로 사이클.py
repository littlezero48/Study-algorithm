#     상, 우, 하, 좌
dx = [-1, 0, 1,  0]
dy = [ 0, 1, 0, -1]

def move(x, y, dir, pos) :
    # x, y 현재 행, 열
    # 가려고 하는 방향(pos)
    # 들어온 방향(dir)
    
    if pos == 'L' :
        # 만약 위(0)로 가는 빛이 L을 만나 좌회전할 경우 (0-1)%4 = (좌)3 로  
        # 만약 우(1)로 가는 빛이 L을 만나 좌회전할 경우 (1-1)%4 = (상)0 로
        # 만약 우(2)로 가는 빛이 L을 만나 좌회전할 경우 (2-1)%4 = (우)1 로
        # 만약 좌(3)로 가는 빛이 L을 만나 좌회전할 경우 (3-1)%4 = (하)2 로
        dir = (dir - 1) % 4  
    elif pos == 'R' :
        dir = (dir + 1) % 4 
        
    # 다음 좌표 설정
    nx = (x + dx[dir]) % row
    ny = (y + dy[dir]) % col

    return nx, ny, dir

def solution(grid) :
    answer = []
    
    # 전체 행, 열
    global row, col     
    row = len(grid)
    col = len(grid[0])
    
    # 방문체크 플래그
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]

    for i in range(row) :
        for j in range(col) :
            for k in range(4) : # 네 방향에 대하여 확인
                if not visited[i][j][k] :
                    route = 0   # 길이
                    x, y, dir = i, j, k
                    
                    # 같은 좌표, 같은 방향으로 또 방문하게 되면 바로 break 사이클 종료
                    while not visited[x][y][dir] :              
                        route += 1                              # 길이 추가
                        visited[x][y][dir] = True               # 방문 체크
                        x, y, dir = move(x, y, dir, grid[x][y]) # 이동

                    answer.append(route) # 완료된 사이클을 기록

    answer.sort() # 사이클 길이를 오름차순 정렬
    return answer