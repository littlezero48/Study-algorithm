def solution(arr, k):
    answer = []
    if k % 2 == 0 :
        for one in arr :
            answer.append(one + k)
    else :
        for one in arr :
            answer.append(one * k)
            
    return answer