def solution(a, b, n):
    bottle = 0

    while n / a >= 1 :
        remain = n % a
        n = (int(n / a)) * b
        bottle += n
        n = n + remain

    return bottle