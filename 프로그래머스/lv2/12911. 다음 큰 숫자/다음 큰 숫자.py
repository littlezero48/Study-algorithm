def solution(n):
    answer = 0

    # bin() 숫자를 2진수 형태의 '문자열'로 만들어줌. 앞에 2진수를 알리는 0b 문자열 포함 
    # 그 문자열 안에서 1의 개수를 get
    n_cnt1 = bin(n).count('1')

    while True:  # 숫자를 하나씩 올려 2진수를 구하고 가장 먼저 처음n과 같은 1의 개수인 수를 return
        n = n + 1
        if n_cnt1 == bin(n).count('1'):
            answer = n
            break;

    return answer