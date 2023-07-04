def solution(binomial):
    answer = 0
    bi_arr = binomial.split(' ')
    a = int(bi_arr[0])
    b = int(bi_arr[2])
    if bi_arr[1] == '+':
        answer = a + b
    elif bi_arr[1] == '-':
        answer = a - b
    elif bi_arr[1] == '*' :
        answer = a * b
    return answer