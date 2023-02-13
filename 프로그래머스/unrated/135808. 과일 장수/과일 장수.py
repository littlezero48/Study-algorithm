def solution(k, m, score):
    score.sort()
    result = 0

    while int(len(score) / m) > 0 :
        p = 0
        for x in range(0, m) :
            p = score.pop()

        result += p * m

    return result