def solution(my_string):
    str = ''
    answer = []
    
    for i in range(len(my_string)):
        str_one = my_string[i]
        if str_one != " " :
            str += str_one
            if i == len(my_string)-1 :
                answer.append(str)
            
        elif len(str) != 0 and str_one == " ":
            answer.append(str)
            str = ''
        
    return answer