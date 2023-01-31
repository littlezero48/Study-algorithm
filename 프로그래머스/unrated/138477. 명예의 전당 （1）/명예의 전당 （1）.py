def solution(k, score):
    answer_List = []
    k_List = []
    for i in range(0, len(score)):
        k_List.append(score[i])
        k_List.sort()
        k_len = len(k_List)

        if len(k_List) > k:
            k_List.remove(k_List[0])
            answer_List.append(k_List[0])
        else :
            answer_List.append(k_List[0])

    return answer_List