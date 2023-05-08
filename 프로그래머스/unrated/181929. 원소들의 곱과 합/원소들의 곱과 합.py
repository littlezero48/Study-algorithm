def solution(num_list):
    multi_num = 1
    sum_num = 0
    answer = 0
    
    for i in num_list :
        multi_num *= i
        sum_num += i
    
    print(multi_num)
    print(sum_num)
    
    if multi_num < sum_num*sum_num :
        answer = 1

    return answer