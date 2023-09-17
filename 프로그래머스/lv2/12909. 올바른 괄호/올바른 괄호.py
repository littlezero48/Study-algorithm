def solution(s):
    answer = False
    stack = []
    
    # 짝 판별을 위해 꼭 다 저장해야한다는 내 편견을 부순 문제
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else :                  # )을 만나면 바로 (를 삭제하여 남는걸 보는 방식
            if len(stack) == 0 :
                return False    # stack이 비어있는 상태에서 )가 있다는 건 절대 짝이 불가함으로 False
            stack.pop()
    
    if len(stack) == 0 :
        answer = True

    return answer