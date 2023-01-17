def solution(numbers):
    answer = ''
    numbers_arr = []
    strNum = ''
    
    for number in numbers :
        strNum += str(number)*3             # 한자리 수를 최대값으로 만들때 3번 곱해야 해서 *3
        numbers_arr.append(strNum)          # 배열에 추가
        strNum =''                          # 새로운 숫자를 위해 초기화
        
    numbers_arr.sort(reverse=True)          # 내림차순으로 정렬
    
    for number in numbers_arr :             
        answer += number[:len(number)//3]   # 3번 곱해서 자리수가 얼마만큼 늘어났느냐에 따라 잘라냄
        
    if int(answer) == 0 :                   # 테스트 케이스 11번 : 00000 을 0으로 처리
        answer = '0'
        
    return answer