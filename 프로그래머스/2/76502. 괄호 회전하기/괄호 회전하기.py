def solution(s):
    answer = 0
    bracket = ['(',')', '[',']', '{','}']
    s_list = list(s)
    for i in range(len(s)):
        if i != 0:
            s_list.append(s_list.pop(0))

        stack = []
        for one in s_list:
            stack.append(one)
            stack_len = len(stack)
            if stack_len >= 2:
                for x in range(0,len(bracket),2) :
                    if stack[stack_len-2:stack_len] == bracket[x:x+2]:
                        stack = stack[:stack_len-2]

        if len(stack) == 0 :
            answer += 1

    return answer