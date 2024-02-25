# n진수로 변환하는 함수
def convert(number, n): # number: 순서, n: 진법
    if number == 0: # 0이면 해당 처리없이 바로 출력
        return '0'
    
    NUMBERS = "0123456789ABCDEF" # 16진수
    
    res = ""  
    while number > 0: # 진법 계산
        mod = number % n 
        number = number // n
        res += NUMBERS[mod] # 나머지로 NUMBERS 문자열에서 해당 인덱스 문자값 가져와 문자 추가 
        
    return res[::-1] # 문자열을 거꾸로 출력하여 진법 순서대로 반환

def solution(n, t, m, p):
    answer = ''
    game = ''
    
    tube_turn = p - 1 # 인덱스는 0부터 시작하므로 tube턴에 -1
    
    for num in range(t * m): # 인원수와 튜브가 미리 구해야할 숫자 만큼을 곱하면 전체 턴수
        game += convert(num, n) # 게임 전체의 문자열 구하기
        
    while 1:
        if len(answer) == t: # 길이가 튜브가 미리 구해야할 숫자 만큼이 되면 빠져나옴
            break
        answer += game[tube_turn] # 전체 문자열에서 튜브 턴의 문자열만 뽑아오기
        tube_turn += m # 현재 튜브턴 + 전체 인원 = 다음 튜브턴        
        
    return answer