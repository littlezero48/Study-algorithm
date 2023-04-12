def solution(hp):
    answer = 0
    
    if (hp / 5) >= 1 :
        answer += int(hp / 5)
        hp = hp % 5
        
    if (hp / 3) >= 1 :
        answer += int(hp / 3)
        hp %= 3
    
    return answer + hp