def solution(strArr):
    answer = []
    for one in strArr :
        if "ad" not in one :
            answer.append(one)
    return answer