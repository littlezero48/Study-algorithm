from itertools import permutations

def solution(expression):
    answer = 0
    # 세가지 연산자로 만들수 있는 모든 조합을 생성
    ops_arr = list(permutations(['*','+','-']))  
    # 모든 연산자 조합으로 값을 계산해 최대값을 answer로 대입
    for i in ops_arr:
        # 기존 answer와 새로 계산한 값을 절대값을 비교해 큰 값을 저장 
        answer = max(answer, abs(int(calculate(expression, i))))
    return answer

# 받은 연산자 문자열에 따라 계산하는 함수
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

# ==================== expression에서 숫자와 연산자 구분
def seperate(expression, op) :
    cal_tmp = []
       
    for i in expression:
        # 연산자에 포함이 안되어 있다면 = 숫자
        if not i in op:
            # 구분된 표현들이 이미 있고, 마지막 배열요소가 연산자가 아니라면
            if len(cal_tmp) != 0 and not cal_tmp[-1] in op:
                # 현재 숫자형문자열을 마지막 배열요소 문자열에 합침
                cal_tmp[-1] = cal_tmp[-1] + i
            # 위 if 조건만 아니라면 새로운 배열요소로 추가
            else:
                cal_tmp.append(i)

        # 연산자에 포함되어 있다면 = 연산자
        else:
            cal_tmp.append(i)
    
    return cal_tmp

# ==================== 실질 계산
def calculate(expression, op):
    cal_tmp = seperate(expression, op)  
    result = [] # 계산 결과를 위한 배열
    stack = []  # 각 연산자 계산 과정을 위한 배열(스택)
    # 연산자 조합에서 하나씩 연산자를 꺼냄
    for o in op : 
        while True:            
            # 더이상 계산 배열요소가 없다면 종료
            if len(cal_tmp) == 0:
                break
            # 있다면 계산 배열요소를 pop    
            tmp = cal_tmp.pop(0)
            # 계산 배열요소가 해당 연산자와 일치하면
            if tmp == o:
                # 직전에 stack에 들어간 숫자와 계산 배열요소에서 다음 숫자, 그리고 현재 연산자를 가지고 계산하여 stack에 다시 push
                stack.append(operation(stack.pop(-1), cal_tmp.pop(0), o))
            else:
                # 연산자가 아니라면 바로 push
                stack.append(tmp)
        
        # 해당 연산자에 대한 결과와 미계산된 숫자와 연산자가 함께 stack에 정리되고 결과에 저장
        result.append(stack)
        # 다음 연산자 계산을 위해 일부 계산된 배열을 cal_tmp에 대입
        cal_tmp = stack
        # 다음 연산자 계산을 위해 초기화
        stack = []
            
    return result[-1][0] # 최종 결과 안 마지막 stack에서 값을 출력