def solution(my_string):
    answer = []
    for one in my_string:
        if one not in answer:
            answer.append(one)
    return ''.join(answer)