def solution(myString):
    return ''.join(one.upper() if one == "a" or one == "A" else one.lower() for one in myString)