def solution(numbers):
    answer = ''
    numbers_arr = []
    strNum = ''
    
    for number in numbers :
        strNum += str(number)*3
        numbers_arr.append(strNum)
        strNum =''
        
    numbers_arr.sort(reverse=True)
    
    for number in numbers_arr :
        answer += number[:len(number)//3]
        
    if int(answer) == 0 :
        answer = '0'
        
    return answer