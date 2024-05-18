from collections import deque

def solution(n,wires):
    answer = 100 # 송신탑 개수가 최대 100개이므로 가능 최대차는 99, 임의 값은 +1인 100으로
    
    for i in range(len(wires)):        
        wire = wires[:i] + wires[i+1:] # 이번 전력망을 제외(끊기)한 나머지 전력망을 할당 = 해당 전선을 끊었을 경우를 보기위해
        
        # 송신탑을 인덱스로 하여 간선 정보 정리 
        graph = [[] for _ in range(n+1)]
        for w in wire:
            graph[w[0]].append(w[1])
            graph[w[1]].append(w[0])
                
        # 송신탑을 인덱스로 하여 송신탑 방문체크를 위한 플래그
        visited = [False for _ in range(n+1)]
        
        # 초기화 
        queue = deque()     # 연결된 송신탑 사이를 이동하기 위한 queue
        queue.append((1))   # 시작은 인덱스1(송신탑#1)                
        cnt = 1             # 연결되어 있는 송신탑 개수
        visited[1] = True   # 시작이 송신탑#1 이므로 방문체크 배열 1번 인덱스는 바로 True로 시작
        
        # 송전탑 개수 체크
        while queue:        # 더이상 갈 곳이 없으면 break
            now = queue.popleft()   # 송신탑 번호
            for v in graph[now]:    # 그 송신탑에 연결된 연결 정보
                if visited[v] == False: # 방문하지 않았다면
                    visited[v] = True   # 방문했음을 표시
                    cnt +=1             # 연결된 송신탑 개수
                    queue.append(v)     # 다음에 방문시도할 송신탑 정보 추가

        # 나뉜 트리를 A,B라고 할 때 A의 송전탑의 개수를 체크하면 
        # 다른쪽은 n-A 개가 되고 둘의 차이는 n-A-A가 되므로 n-(2*A)의 절대값이 된다
        # 그 절대값이 가장 작은 케이스를 대입
        answer = min(answer,abs(n-(2*cnt)))
        
    return answer