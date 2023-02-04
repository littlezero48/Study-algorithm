import math
def solution(number, limit, power):
    result = 0
    cnt = 0
    for i in range(1, number+1):
        if i == 1:
            result = 1
            continue

        for x in range(1, int(math.sqrt(i))+1):
            if i%x == 0:
                cnt += 1
                if x*x != i:
                    cnt += 1

        if cnt > limit:
            result += power
            cnt = 0
        else:
            result += cnt
            cnt = 0

    return result