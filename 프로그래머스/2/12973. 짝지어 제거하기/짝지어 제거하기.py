def solution(s):
    # 짝지어 제거하는건 stack 이용
    
    stack = []    
    for i in range(len(s)):             
        # stack이 비어있다면 무조건 push
        if not stack: 
            stack.append(s[i])
        else :
            # stack이 비어있지 않다면  
            if s[i] == stack[-1]:   # stack의 top과 비교해 동일하면
                stack.pop()         # top을 pop
            else :                  # 아니면 push
                stack.append(s[i]) 
            
    if stack : return 0             # stack이 비어있지 않으면 0
    else : return 1                 # stack이 비어있으면 1