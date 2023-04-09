def solution(sides):
    sum_num = sum(sides) - max(sides)
    if max(sides) < sum_num :
        return 1 
    else :
        return 2