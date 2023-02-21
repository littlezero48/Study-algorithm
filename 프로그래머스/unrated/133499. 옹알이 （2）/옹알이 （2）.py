def solution(babbling):
    basic = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for one in babbling:
        i = 0
        if one.isspace() :
            continue

        while i < len(basic) :
            if basic[i] * 2 in one:
                break

            if one.isspace() :
                cnt += 1
                break

            start_idx = one.find(basic[i])

            if start_idx != -1 :
                one = one.replace(basic[i], " ", 1)
            else:
                i += 1

    return cnt