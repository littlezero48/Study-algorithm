def solution(rows, columns, queries):
    # 값이 들어간 다차원배열 생성
    arr = [[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)] 
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(change(x1-1, y1-1, x2-1, y2-1, arr))
    return result

def change(x1, y1, x2, y2, arr):
    # 가장 큰 수부터 비교하며 최소 숫자를 찾아가야하므로 이 조건에서 들어올 수 있는 가장 큰 수를 할당 
    # rows 최대 100 columns 최대 100 이니 될수 있는 가장 큰 수 10000
    min_value = 10000 
    
    # 시작 좌표 저장
    temp = arr[x1][y1]
    # 왼 > 오 로 이동하며 하나씩 당겨 값을 저장
    # 가장 첫번째 값은 temp에서 저장하고 있으므로 첫번째 값이 덮어지는 것은 괜찮음
    for k in range(x1, x2):
        arr[k][y1] = arr[k+1][y1] 
        min_value = min(min_value, arr[k+1][y1]) # 이동 중 가장 작은 값을 비교해서 저장
    # 위 > 아래 로 이동하며 하나씩 당겨 값을 저장
    for k in range(y1, y2):
        arr[x2][k] = arr[x2][k+1]
        min_value = min(min_value, arr[x2][k+1])
    # 오 > 왼
    for k in range(x2, x1, -1):
        arr[k][y2] = arr[k-1][y2]
        min_value = min(min_value, arr[k-1][y2])
    # 아래 > 위
    for k in range(y2, y1+1, -1):
        arr[x1][k] = arr[x1][k-1]
        min_value = min(min_value, arr[x1][k-1])
    # 기록했던 처음값을 처음자리 아래에 업데이트하여 전체 회전 적용 완료
    arr[x1][y1+1] = temp
    
    # 최초 값까지 포함하여 비교해 이동한 값 중 가장 작은 값 저장
    min_value = min(min_value, temp)
    return min_value