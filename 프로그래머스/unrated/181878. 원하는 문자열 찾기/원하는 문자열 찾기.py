def solution(myString, pat):
    myString = myString.lower()
    if myString.find(pat.lower()) != -1 :
        return 1
    return 0