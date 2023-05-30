def solution(my_string, is_prefix):
    return 1 if is_prefix == my_string[:len(is_prefix)] else 0