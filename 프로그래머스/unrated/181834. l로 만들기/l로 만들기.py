def solution(myString):
    answer = ''
    for char in myString:
        if ord(char) < ord('l') :
            answer += "l"
        else :
            answer += char
    return answer