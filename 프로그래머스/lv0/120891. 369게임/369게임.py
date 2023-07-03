def solution(order):
    answer = 0
    while True:      
        if order == 0 :
            break;        
        if (order % 10) % 3 == 0 and (order % 10) != 0 :
            answer += 1            
        order = int (order / 10)
    return answer