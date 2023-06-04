def solution(my_string):
    answer = ''
    return ''.join(one.lower() if one == one.upper() else one.upper() for one in my_string)