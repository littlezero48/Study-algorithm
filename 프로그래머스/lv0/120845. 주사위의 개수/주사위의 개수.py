def solution(box, n):
    
    first = int(box[0] / n)
    second = int(box[1] / n)
    third = int(box[2] / n)
        
    answer = first * second * third
        
    return answer