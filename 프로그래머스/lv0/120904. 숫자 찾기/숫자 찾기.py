def solution(num, k):
    answer = -1
    num_arr = [int(a) for a in str(num)]
    for i in range(len(num_arr)):
        if num_arr[i] == k:
            return i+1
    return answer