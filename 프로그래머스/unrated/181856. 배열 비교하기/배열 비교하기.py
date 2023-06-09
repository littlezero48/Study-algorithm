def solution(arr1, arr2):
    answer = 0
    arr1_sum = 0
    arr2_sum = 0
    if len(arr1) != len(arr2) :
        if len(arr1) > len(arr2) :
            answer = 1
        else :
            answer = -1
    else :
        for i in range(len(arr1)) :
            arr1_sum += arr1[i]
            arr2_sum += arr2[i]
        
        if arr1_sum > arr2_sum :
            answer = 1
        elif arr1_sum < arr2_sum :
            answer = -1
            
    return answer