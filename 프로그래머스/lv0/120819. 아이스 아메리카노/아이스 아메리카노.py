def solution(money):
    answer = []
    cup = int(money / 5500)
    answer.append(cup)
    remain = money % 5500
    answer.append(remain)
    return answer