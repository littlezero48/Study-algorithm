def solution(n):
    a, b = 0, 1 # 0일때와 1일때는 그 이전 값이 모자라므로 미리 준비 
    for i in range(n):
        # 더하는 숫자 중 두번째 숫자는 다음 식의 첫번째가 되므로 first로 옮김
        # second는 더한 값을 대입
        a, b = b, a + b
    
    # 여기서 왜 b값이 아니라 a값을 일까?
    # 처음에 이미 0과 1번째에 값을 미리 대입 그래서 for문에 포함이 안되었음에도 결과로는 포함이 됨
    # 따라서 range(n)으로 n-1번을 돌지만 여기서 0번째와 1번째를 만드는 2번을 포함하여
    # 생각하면 마지막 값a,b에는 n, n+1에 해당하는 값이 된다. 그래서 a 값을 출력 
    return a % 1234567 