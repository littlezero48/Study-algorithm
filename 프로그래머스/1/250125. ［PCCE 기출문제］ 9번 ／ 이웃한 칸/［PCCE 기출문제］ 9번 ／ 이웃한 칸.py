def solution(board, h, w):
    count = 0
    
    n = len(board)
    
    # 좌표 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 고른 칸의 색상
    color = board[h][w]
    
    # 위, 아래, 왼쪽, 오른쪽을 체크
    for i in range(len(dx)):
        # 고른 칸 기준으로 좌표 이동
        nx = h + dx[i]
        ny = w + dy[i]
        # 이동한 칸이 격자보드판을 나가지 않는지 판단
        if 0 <= nx < n and 0 <= ny < n:
            # 해당 색상이 고른 칸이랑 같은지 판단
            if board[nx][ny] == color:
                count += 1
    return count