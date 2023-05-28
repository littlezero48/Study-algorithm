def solution(num_list):
    num_before = num_list[-2]
    num_last = num_list[-1]
    
    if num_before < num_last :
        num_list.append(num_last - num_before)
    else :
        num_list.append(num_last * 2)
    
    return num_list