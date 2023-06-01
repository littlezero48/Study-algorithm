def solution(my_string, is_suffix):
    return 1 if my_string[len(is_suffix)*-1:] == is_suffix else 0