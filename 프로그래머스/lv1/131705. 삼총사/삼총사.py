def solution(number):
    cnt = 0
    for i in range(len(number)):
        for x in range(i+1,len(number)):
            for y in range(x+1,len(number)) :
                if (number[i] + number[x] + number[y]) == 0 :
                    cnt += 1

    return cnt