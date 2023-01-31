def solution(s):
    x = ""
    start_Idx = 0
    x_Cnt = 0
    x_Not_Cnt = 0
    answer_list = []
    for i in range(0, len(s)):
        if x == "":
            x = s[i]
            start_Idx = i
            x_Cnt += 1
            continue

        if x == s[i]:
            x_Cnt += 1
        else :
            x_Not_Cnt += 1

        if x_Cnt == x_Not_Cnt:
            answer_list.append(s[start_Idx: i+1])
            x_Cnt = 0
            x_Not_Cnt = 0
            x = ""

    if x_Cnt != 0 or x_Not_Cnt != 0:
        answer_list.append(s[start_Idx: i + 1])

    return len(answer_list)