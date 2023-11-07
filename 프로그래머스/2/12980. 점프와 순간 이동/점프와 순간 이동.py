def solution(n):
    jump = 0
    
    if n == 1:
        return 1
    
    while n > 1 :
        jump += n % 2
        n = int(n / 2)        
        
        if n == 1 :
            jump += 1

    return jump