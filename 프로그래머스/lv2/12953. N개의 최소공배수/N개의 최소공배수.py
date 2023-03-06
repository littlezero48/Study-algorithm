def solution(arr):
    max_num = max(arr)
    i = 1
    while True :
        multi_num = max_num * i
        flag = True
        for one in arr :
            if multi_num % one != 0:
                flag = False

        if flag :
            return multi_num
        else :
            i += 1