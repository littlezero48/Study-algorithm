def solution(num_list):
    odd = ''
    even = ''
    odd = ''.join(str(one) if one % 2 != 0 else '' for one in num_list)
    even = ''.join(str(one) if one % 2 == 0 else '' for one in num_list)
    return int(odd) + int(even)