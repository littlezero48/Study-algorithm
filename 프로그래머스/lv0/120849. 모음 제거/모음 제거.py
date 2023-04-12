def solution(my_string):
    vowel = ['a', 'i', 'u', 'e', 'o']
    answer = ''
    
    for i in range(0, len(my_string)) :
        if my_string[i] not in vowel :
            answer += my_string[i]

    return answer