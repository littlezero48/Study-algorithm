def solution(my_string):
    answer = [one for one in my_string.lower()]
    answer.sort()
    return "".join(answer)