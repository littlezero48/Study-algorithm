def solution(sides):
    max_num = sides.pop(sides.index(max(sides)))
    sum_num = 0
    for side in sides :
        sum_num += side
    
    if max_num < sum_num :
        return 1
    else :
        return 2