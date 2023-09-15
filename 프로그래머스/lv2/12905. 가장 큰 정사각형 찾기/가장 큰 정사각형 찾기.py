def solution(board):
    row_size = len(board)
    col_size = len(board[0])
    max = 0
    
    if row_size == 1 and col_size == 1 and board[0][0] == 1 : # 사이즈가 가로세로1 그리고 값이 1인 경우 별도처리 
        return 1
    
                                    # dp로 판단한 곳의 값을 저장할 이중배열을 준비    
    dp = [[0 for i in range(col_size)] for i in range(row_size)]
    
                                    # 가장 첫번째 행과 열은 먼저 저장
    dp[0] = board[0]                # 첫번째 행
    for i in range(row_size):           # 첫번째 열 
        dp[i][0] = board[i][0]

                                    # 첫번째 행과 열은 저장했으니 [1][1]부터 시작
    for i in range(1,row_size):
        for j in range(1,col_size):
            if board[i][j] == 1 :   # 지금 위치가 1일 경우 판단시작
                # 현재 위치에서 위, 왼쪽 대각선, 왼쪽의 값 중 가장 작은 값을 찾아 + 1 = 그 자리에서 만들 수 있는 정사각형 크기
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1            
                                   
                if(max < dp[i][j]): # 보다 큰값이 나오면 갱신 
                    max = dp[i][j]
    
    return max * max                # 넓이