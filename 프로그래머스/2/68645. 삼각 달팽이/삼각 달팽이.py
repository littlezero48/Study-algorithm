def solution(n):
    answer = []
    
    temp = [[0] * n for _ in range(n)]      # 모든 값이 0인 n행 n열의 다차원 배열을 생성
    x, y = -1, 0                            # 초기값 세팅 (for문 시작시 0행에 값을 적용하기 위해 초기 셋팅을 -1행으로 설정)
    num = 1                                 # 들어갈 숫자값 초기 세팅

    for i in range(n): 
        for j in range(i, n):
            # 3으로 분기 타는 이유는 달팽이 채우기시 운동방향이 아래, 오른쪽, 위로 움직이기 때문
            if i % 3 == 0:          
                x += 1  # 아래
            elif i % 3 == 1:
                y += 1  # 오른쪽
            elif i % 3 == 2:
                x -= 1  # 위
                y -= 1

            temp[x][y] = num        # 다차원 배열에 들어갈 숫자 대입
            num += 1                # 그 다음 숫자

    for i in temp:
        for j in i:
            if j != 0:              # 값이 없는 부분은 삼각형에 해당하는 부분이 아니므로 제외
                answer.append(j)    # 다차원 배열을 하나의 배열로 정리

    return answer