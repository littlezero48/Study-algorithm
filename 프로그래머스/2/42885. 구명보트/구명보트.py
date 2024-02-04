from collections import deque

def solution(people, limit):
    answer = 0
    
    # 무거운 사람과 가벼운 사람을 같이 많이 구출하는 게 포인트
    # limit에서 무거운사람부터 해서 무게를 빼면서 사람을 추가
    dq = deque()

    # 오름차순으로 정렬
    arr=sorted(people)

    for i in range(0, len(arr)):
        dq.append(arr[i])


    front = 0

    while(len(dq) > 1):
        if(dq[front] + dq[-1] > limit):
            answer += 1
            dq.pop()

        else:
            dq.pop()
            dq.popleft()
            answer+=1

    if(len(dq) == 1):       
        dq.popleft()
        answer+=1


    return answer