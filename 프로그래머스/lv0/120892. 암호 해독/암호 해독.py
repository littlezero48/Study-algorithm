def solution(cipher, code):
    answer = ''
    for i in range(0,len(cipher)):
        if (i+1)%code == 0: 
            answer += cipher[i]
            
    return answer