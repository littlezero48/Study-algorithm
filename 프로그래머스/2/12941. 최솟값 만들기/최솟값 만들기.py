def solution(A,B):
    answer = 0
    # 배열끼리 한 숫자씩 곱해 값을 누적하는 거라면
    # 가장 최솟값 = A 배열에서 가장 작은 값 * B 배열에서 가장 큰 값
    
    A.sort()
    B.sort(reverse = True)

    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer