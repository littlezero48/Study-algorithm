def solution(N, road, K):
    answer = 0

    # 노드 개수 +1 만큼 배열 준비 (+1한건 인덱스 자체를 노드로 사용하기 위함)
    # 2차원 배열을 사용하는 이유는 각 노드에서 다른 노드로 이동하는 거리을 저장하기 위함
    # 원래는 빈값으로 초기화해주려고 했으나 노드끼리 이동거리 합치는 과정에서 배열이 비어있으면 더 복잡해지므로 
    # 최대시간인 500000 에서 1 더한 값으로 조건 불가한 값으로 초기화
    graph = [[500001 for _ in range(N+1)] for _ in range(N+1)] 
    
    # 자기 자신에게로 가는 거리는 0으로 초기화
    for i in range(1, N+1):
        graph[i][i] = 0
        
    # 노드 사이의 이동 거리 정리 / (node1 -> node2) = (node2 -> node1) 이므로 양쪽 다 저장
    for node1, node2, length in road:
        # 같은 노드를 잇는 도로가 여러개가 있을 수 있기 때문에 그 중 가장 최단거리 도로 값을 저장
        graph[node1][node2] = min(graph[node1][node2], length)
        graph[node2][node1] = min(graph[node2][node1], length)
    
    # nodeStart -> nodeEnd 로 가는 경우와 nodeStart -> nodeMiddle -> nodeEnd 가는 경우의 수를 비교해 
    # nodeStart -> nodeEnd 로 갈수 있는 최단거리를 구함
    for Middle in range(1, N+1):
        for Start in range(1, N+1):
            for End in range(1, N+1):
                graph[Start][End] = min(graph[Start][End], graph[Start][Middle] + graph[Middle][End])
    
    # 기준이 1번 마을 이라는 걸 여기서 사용
    # graph[1] 이 1번 마을에서 n개의 마을로 이동하는 거리의 합이 저장되어 있으므로
    # graph[1]의 모든 값을 K값과 비교하여 k보다 작거나 같으면 배달가능한 마을!!
    for j in graph[1]:
        if j <= K :
            answer += 1

    return answer