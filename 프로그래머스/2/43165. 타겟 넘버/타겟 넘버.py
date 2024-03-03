from collections import deque
def solution(numbers, target):
    # 인덱스 당 +,- 값이 존재한다고 여겨 모두 방문하고 결과 값이 target과 일치하는 케이스 수를 결과값으로 리턴
    answer = 0
    queue = deque()
    n = len(numbers)
    
    # ex) [4,1,2,1] 이라면
    queue.append([numbers[0],0]) # 첫 값1 (+값, idx) = (4, 0)
    queue.append([-1*numbers[0],0]) # 첫 값2 (-값, idx) = (-4, 0)
    
    while queue: # queue가 빌때까지 반복
        temp, idx = queue.popleft()
        idx += 1
        if idx < n: # 인덱스가 numbers 길이 보다 작다면 계속
            queue.append([temp+numbers[idx], idx]) # 지금 인덱스값에 + 값, 다음 인덱스
            queue.append([temp-numbers[idx], idx]) # 지금 인덱스값에 - 값, 다음 인덱스
        else: # 인덱스가 numbers 길이와 같다면 최종 결과
            if temp == target: # 최종 결과 값이 targer과 동일하다면 일치 케이스 +1
                answer += 1
    return answer