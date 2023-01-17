import heapq # 모듈사용 

def solution(scoville, K):
    cnt = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1 :
            cnt = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        cnt += 1

    return cnt

    