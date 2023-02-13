def solution(ingredient):
    burger = [1, 2, 3, 1]
    cnt = 0

    stack = []
    for one in ingredient :
        stack.append(one)
        length = len(stack)
        if length >= 4 :
            if stack[length-4: length] == burger :
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                cnt += 1


    return cnt