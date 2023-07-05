def solution(arr, intervals):
    answer = []
    for one in intervals :
        answer += arr[one[0]:one[1]+1]
    return answer