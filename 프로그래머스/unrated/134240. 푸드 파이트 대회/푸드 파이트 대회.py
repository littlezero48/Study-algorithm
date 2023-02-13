def solution(food):
    left = ""
    for i in range(1, len(food)) :
        left += str(i) * int(food[i] / 2)

    right = left[::-1]

    return left + "0" + right