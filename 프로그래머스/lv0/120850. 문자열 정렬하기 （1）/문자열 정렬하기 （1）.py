import re

def solution(my_string):
    answer = []
    my_string = re.sub(r'[^0-9]', '', my_string)
    answer = [int(one) for one in my_string]
    answer.sort()
    return answer