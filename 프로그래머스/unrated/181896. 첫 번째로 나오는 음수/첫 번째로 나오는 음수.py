def solution(num_list):
    for i in range(0,len(num_list)) :
        if num_list[i] < 0 :
            return i
        
    return -1