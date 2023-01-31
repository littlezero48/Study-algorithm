def solution(s):

    answer_List = []
    for i in range(0, len(s)):
        same_Idx = 0
        cnt = 0
        if i == 0:
            answer_List.append(-1)
            continue
        for x in range(0, i):
            if s[i] == s[x]:
                cnt += 1
                same_Idx = x

        if same_Idx == 0 and cnt == 0:
            answer_List.append(-1)
        else:
            answer_List.append(i - same_Idx)

    return answer_List