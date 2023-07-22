def solution(num_list, n):
    answer = []
    arr_len = len(num_list)
    num = int(arr_len / n) + 1 if arr_len % n != 0 else int(arr_len/n)
    for i in range(num):
        answer.append(num_list[i*n:i*n+n])
    
    return answer