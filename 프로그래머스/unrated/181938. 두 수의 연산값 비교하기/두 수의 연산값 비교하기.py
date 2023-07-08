def solution(a, b):
    num = b
    time = 0
    while num > 0 :
        num = int(num/10)
        time += 1
    a_result = (a*(10**time)) + b
    b_result = 2*a*b
    return a_result if a_result >= b_result else b_result