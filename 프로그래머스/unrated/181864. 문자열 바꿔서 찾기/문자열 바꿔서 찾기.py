def solution(myString, pat): 
    answer = ''.join("B" if one == "A" else "A" for one in myString)
    return 1 if answer.find(pat) != -1 else 0