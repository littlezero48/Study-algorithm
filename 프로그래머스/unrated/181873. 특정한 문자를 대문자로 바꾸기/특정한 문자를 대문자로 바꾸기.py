def solution(my_string, alp):
    return ''.join(one.upper() if one == alp else one.lower() for one in my_string)