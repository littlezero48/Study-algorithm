def solution(n):
    n_list = [0] * n

    for i in range(n):
        if i == 0 :
            n_list[i] = 1
        elif i == 1 :
            n_list[i] = 2
        else:
            n_list[i] = n_list[i-1] + n_list[i-2]

    return n_list[n-1] % 1234567