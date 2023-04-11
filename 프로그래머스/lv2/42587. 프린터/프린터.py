def solution(priorities, location):
    answer = 0 
    queue = [(i,priorities[i]) for i in range(0,len(priorities))]
    
    while True: 
        one = queue.pop(0)
        max_num = max(priorities)
        if one[1] != max_num :
            queue.append(one)
        else :
            priorities.pop(priorities.index(max_num))
            answer += 1
            if location == one[0] :
                return answer