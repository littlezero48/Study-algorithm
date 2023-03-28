def solution(k, tangerine):
    
    answer = 0
    tangerine_arr = [0] * (max(tangerine) + 1)
    
    for one in tangerine :
        tangerine_arr[one] += 1
        
    if k < max(tangerine_arr) :
        return 1
        
    tangerine_arr.sort()
    tangerine_arr.reverse()
    
    for one in tangerine_arr :
        k -= one
        answer += 1
        if k <= 0 :
            break
    
    return answer