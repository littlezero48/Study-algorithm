def solution(arr):
    flag = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == arr[j][i]:
                flag = 1
            else :
                return 0
    return flag