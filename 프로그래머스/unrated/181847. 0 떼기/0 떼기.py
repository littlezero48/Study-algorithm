def solution(n_str):
    answer = ''
    flag = False
    for str_one in n_str:
        if str_one == "0":
            if flag == True :
                answer += str_one
            else: 
                continue
        else:
            flag = True
            answer += str_one
    return answer