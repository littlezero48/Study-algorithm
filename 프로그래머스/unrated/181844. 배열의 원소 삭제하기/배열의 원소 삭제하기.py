def solution(arr, delete_list):
    answer = []
    for one in arr :
        if one in delete_list :
            continue
        else :
            answer.append(one)
    return answer